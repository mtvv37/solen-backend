"""Sound design for the Solen vision film (55 s), synthesized with numpy.

Writes sfx.wav (effects + a fallback music bed). Event times follow the final cut.
If music.wav / echo*.wav / solen.wav exist next to this file, they are mixed in too.
"""
import os
import wave
import numpy as np

SR = 48000
DUR = 55.0
N = int(SR * DUR)
rng = np.random.default_rng(7)
L = np.zeros(N)
R = np.zeros(N)


def env_exp(n, tau):
    return np.exp(-np.arange(n) / (tau * SR))


def add(sig, t, gain=1.0, pan=0.0):
    i = int(t * SR)
    if i >= N:
        return
    sig = sig[: N - i]
    gl, gr = gain * np.sqrt((1 - pan) / 2), gain * np.sqrt((1 + pan) / 2)
    L[i:i + len(sig)] += sig * gl
    R[i:i + len(sig)] += sig * gr


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for k in range(len(x)):
        acc = (1 - a) * x[k] + a * acc
        y[k] = acc
    return y


def lp_fast(x, cutoff):
    # frequency-domain brickwall-ish lowpass with soft knee (fast for long signals)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / cutoff) ** 4)
    return np.fft.irfft(X, len(x))


def hp_fast(x, cutoff):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 - 1 / np.sqrt(1 + (f / cutoff) ** 4)
    return np.fft.irfft(X, len(x))


def sine(freq, dur, phase=0.0):
    t = np.arange(int(dur * SR)) / SR
    if callable(freq):
        ph = 2 * np.pi * np.cumsum(freq(t)) / SR
        return np.sin(ph + phase)
    return np.sin(2 * np.pi * freq * t + phase)


def noise(dur):
    return rng.standard_normal(int(dur * SR))


# ---------- elements ----------
def ping():
    d = 0.6
    s = 0.6 * sine(1318.5, d) + 0.4 * sine(1975.5, d) + 0.15 * sine(2637, d)
    s *= env_exp(len(s), 0.12)
    s2 = (0.5 * sine(1760, d) + 0.3 * sine(2637, d)) * env_exp(int(d * SR), 0.15)
    out = np.zeros(int(0.8 * SR)); out[:len(s)] += s; out[int(0.09 * SR):int(0.09 * SR) + len(s2)] += s2
    return out * 0.5


def swipe(dur=0.32, lo=600, hi=5000):
    n = noise(dur)
    t = np.linspace(0, 1, len(n))
    e = np.sin(np.pi * t) ** 2
    return hp_fast(lp_fast(n * e, hi), lo) * 0.35


def whoosh(dur=0.7, cut=2500):
    n = noise(dur)
    t = np.linspace(0, 1, len(n))
    e = np.sin(np.pi * t ** 0.7) ** 3
    return lp_fast(n * e, cut) * 0.6


def thump(f0=62):
    d = 0.35
    s = sine(lambda t: f0 * (1 + 1.2 * np.exp(-t / 0.03)), d) * env_exp(int(d * SR), 0.09)
    return s


def heartbeat():
    out = np.zeros(int(0.7 * SR))
    a = thump(60); b = thump(52) * 0.7
    out[:len(a)] += a; out[int(0.26 * SR):int(0.26 * SR) + len(b)] += b
    return out * 0.9


def impact(big=1.0):
    d = 2.5
    sub = sine(lambda t: 38 + 70 * np.exp(-t / 0.08), d) * env_exp(int(d * SR), 0.6)
    crack = lp_fast(noise(d) * env_exp(int(d * SR), 0.05), 3500) * 0.7
    body = lp_fast(noise(d) * env_exp(int(d * SR), 0.5), 400) * 0.6
    return (sub * 1.1 + crack + body) * big


def riser(dur):
    t = np.arange(int(dur * SR)) / SR
    x = t / dur
    tone = sine(lambda tt: 180 + 1400 * (tt / dur) ** 2, dur) * 0.25 + sine(lambda tt: 90 + 700 * (tt / dur) ** 2, dur) * 0.2
    n = hp_fast(noise(dur), 1500) * 0.35
    e = x ** 2.2
    return (tone + n * x) * e


def click(f=3200, d=0.03, g=0.5):
    s = sine(f, d) * env_exp(int(d * SR), 0.004) + noise(d) * env_exp(int(d * SR), 0.002) * 0.4
    return s * g


def pop(f0=520, f1=980):
    d = 0.12
    s = sine(lambda t: f0 + (f1 - f0) * np.minimum(1, t / 0.05), d) * env_exp(int(d * SR), 0.03)
    return s * 0.55


def chime(base=880, d=1.8, g=0.5):
    s = sum(a * sine(base * m, d) for a, m in [(1, 1), (0.5, 1.5), (0.35, 2), (0.2, 3.01)])
    return s * env_exp(int(d * SR), 0.45) * g / 2


def glitch():
    d = 0.5
    n = noise(d)
    step = 60
    n = np.repeat(n[::step], step)[: int(d * SR)]
    gate = (np.sin(np.arange(int(d * SR)) / SR * 2 * np.pi * 23) > 0.2).astype(float)
    return lp_fast(n * gate * np.linspace(1, 0, int(d * SR)), 6000) * 0.35


def alert():
    d = 0.6
    s = (sine(220, d) + 0.5 * sine(233, d)) * (0.6 + 0.4 * np.sin(np.arange(int(d * SR)) / SR * 2 * np.pi * 14))
    return s * env_exp(int(d * SR), 0.25) * 0.45


# ---------- dark bed (0 → 12.45) ----------
def drone():
    d = 12.6
    t = np.arange(int(d * SR)) / SR
    rise = np.clip(t / 11, 0, 1)
    s = (np.sin(2 * np.pi * 41 * t) * 0.5 + np.sin(2 * np.pi * 61.7 * t + 1) * 0.3 + np.sin(2 * np.pi * (82 + 6 * rise) * t) * 0.15)
    s *= (0.55 + 0.45 * rise) * (0.85 + 0.15 * np.sin(2 * np.pi * 0.25 * t))
    air = lp_fast(noise(d), 300) * 0.25 * rise
    fade = np.minimum(1, t / 1.5) * np.where(t > 12.35, np.clip((12.6 - t) / 0.25, 0, 1), 1)
    return (s + air) * fade * 0.5


# ---------- fallback music bed (12.45 → 55) ----------
BPM = 112
BEAT = 60 / BPM
NOTE = {'A2': 110.0, 'C3': 130.81, 'E3': 164.81, 'F2': 87.31, 'G2': 98.0, 'A3': 220.0, 'C4': 261.63, 'E4': 329.63,
        'F3': 174.61, 'G3': 196.0, 'B3': 246.94, 'D4': 293.66, 'D3': 146.83, 'G4': 392.0, 'F4': 349.23, 'C5': 523.25, 'E5': 659.25, 'A4': 440.0, 'B4': 493.88, 'D5': 587.33, 'G5': 783.99}
CHORDS = [('A2', ['E3', 'A3', 'C4', 'E4']), ('F2', ['C3', 'F3', 'A3', 'C4']), ('C3', ['G3', 'C4', 'E4', 'G4']), ('G2', ['D3', 'G3', 'B3', 'D4'])]
ARP = [['A4', 'C5', 'E5', 'C5'], ['A4', 'C5', 'F4', 'C5'], ['G4', 'C5', 'E5', 'C5'], ['G4', 'B4', 'D5', 'B4']]


def pad_tone(f, d):
    t = np.arange(int(d * SR)) / SR
    s = np.zeros_like(t)
    for det in (-0.0035, 0, 0.0035):
        for h in range(1, 7):
            s += np.sin(2 * np.pi * f * (1 + det) * h * t + h) / (h ** 1.4)
    e = np.minimum(1, t / 0.35) * np.minimum(1, (d - t) / 0.4)
    return s * e / 8


def pluck(f, d=0.45):
    t = np.arange(int(d * SR)) / SR
    s = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    return s * np.exp(-t / 0.12) * 0.3


def kick():
    d = 0.4
    return sine(lambda t: 48 + 110 * np.exp(-t / 0.035), d) * env_exp(int(d * SR), 0.12) * 0.9


def hat():
    d = 0.06
    return hp_fast(noise(d), 7000) * env_exp(int(d * SR), 0.012) * 0.25


def music_bed():
    start = 12.45
    t = start
    bar = 4 * BEAT
    k = 0
    while t < 50.2:
        root, tones = CHORDS[k % 4]
        for nt in tones:
            add(pad_tone(NOTE[nt], bar + 0.4), t, 0.16, pan=rng.uniform(-0.4, 0.4))
        add(pad_tone(NOTE[root] / 2, bar + 0.2), t, 0.22)  # sub
        for b in range(4):
            bt = t + b * BEAT
            if bt >= 50.2:
                break
            if bt > 15.6:
                add(kick(), bt, 0.55 if bt < 30.8 else 0.7)
            if bt > 25.0:
                add(hat(), bt + BEAT / 2, 0.6, pan=0.3)
            if bt > 15.6:
                for s8 in range(2):
                    nt = ARP[k % 4][(b * 2 + s8) % 4]
                    add(pluck(NOTE[nt]), bt + s8 * BEAT / 2, 0.22 if bt < 30.8 else 0.3, pan=-0.35 + 0.7 * s8)
        t += bar
        k += 1
    # final resolve: C major held
    for nt in ['C3', 'G3', 'C4', 'E4', 'G4']:
        add(pad_tone(NOTE[nt], 4.8), 50.2, 0.2)
    add(pad_tone(NOTE['C3'] / 2, 4.8), 50.2, 0.25)


# ---------- timeline (final cut times) ----------
add(drone(), 0, 1.0)
for f in (0.55, 1.2, 1.8):
    add(swipe(), f, 0.8, pan=0.2)
for k in range(4):
    add(ping(), 2.25 + k * 0.42, 0.55, pan=-0.2 + 0.13 * k)
add(whoosh(0.6, 1500), 4.35, 0.6)
for k in range(9):
    add(heartbeat(), 6.2 + k * (0.85 + k * 0.04), 0.8 * (1 - k * 0.06))
add(glitch(), 10.25, 0.9)
add(riser(2.4), 10.05, 0.9)
add(impact(1.0), 12.45, 1.0)
add(chime(660, 2.2, 0.35), 12.5, 0.8)
q = "Solen, why isn't my store selling?"
for i in range(len(q)):
    if q[i] != ' ':
        add(click(rng.uniform(2600, 3600), 0.025, 0.25), 13.6 + 0.9 * i / len(q), 1.0, pan=0.25)
add(pop(), 14.7, 0.9, pan=-0.2)
add(whoosh(1.2, 3000), 15.5, 0.7)
ts = 16.1
for i in range(40):
    u = i / 40
    tt = 16.1 + 2.3 * (1 - (1 - u) ** 1.8)
    add(click(1200 + 1800 * u, 0.02, 0.18), tt, 1.0)
add(impact(0.45), 18.4, 0.8)
add(chime(990, 1.4, 0.3), 18.42, 0.8)
add(click(1800, 0.04, 0.6), 21.25, 1.0)
add(alert(), 21.65, 1.0)
add(pop(400, 700), 22.2, 0.8)
for i in range(30):
    add(click(rng.uniform(2500, 4500), 0.015, 0.08), 25.05 + i * 0.028, 1.0, pan=rng.uniform(-0.6, 0.6))
add(chime(1320, 1.2, 0.3), 26.2, 0.8)
for i in range(99):
    add(click(rng.uniform(500, 900), 0.02, 0.12), 26.3 + i * 0.021, 1.0, pan=rng.uniform(-0.5, 0.5))
for k in range(4):
    add(pop(300, 450), 26.4 + k * 0.5, 0.6)
add(whoosh(0.8, 2500), 28.55, 0.8)
add(impact(0.35), 29.2, 0.8)
add(chime(880, 1.6, 0.35), 29.25, 0.8)
add(whoosh(0.6, 2000), 30.85, 0.5)
add(chime(1760, 1.0, 0.2), 31.7, 0.7)
add(riser(0.8) * 0.6, 32.15, 0.6)
for k in range(4):
    add(pop(), 33.1 + k * 0.3, 0.7, pan=-0.45 + 0.3 * k)
add(riser(1.7) * 0.5, 35.9, 0.5)
add(impact(0.3), 37.6, 0.7)
add(chime(1046.5, 1.6, 0.4), 37.62, 0.8)
for k in range(3):
    add(pop(450, 800), 38.0 + k * 0.35, 0.6)
for i in range(7):
    add(click(2200, 0.02, 0.2), 40.65 + i * 0.07, 1.0, pan=-0.6 + 0.2 * i)
    add(pop(500, 900), 41.1 + i * 0.16, 0.45, pan=-0.6 + 0.2 * i)
add(whoosh(0.7, 1800), 42.3, 0.35)
add(click(2400, 0.04, 0.8), 43.15, 1.0)
add(chime(1318.5, 1.4, 0.45), 43.18, 0.8)
add(whoosh(1.1, 3000), 45.55, 0.8)
for k in range(4):
    add(pop(500, 850), 46.7 + k * 0.12, 0.5, pan=-0.6 + 0.4 * k)
add(whoosh(1.5, 2500), 49.5, 0.6)
add(impact(0.9), 50.2, 1.0)
add(chime(523.25, 3.5, 0.45), 50.22, 0.9)

have_music = os.path.exists('music.wav')
if not have_music:
    music_bed()


# ---------- simple stereo reverb ----------
def reverb(x, t60=1.8, wet=0.18):
    n = int(t60 * SR)
    ir = rng.standard_normal(n) * np.exp(-6.9 * np.arange(n) / n)
    ir = lp_fast(ir, 5000); ir /= np.sqrt((ir ** 2).sum())
    size = len(x) + n
    nfft = 1 << (size - 1).bit_length()
    y = np.fft.irfft(np.fft.rfft(x, nfft) * np.fft.rfft(ir, nfft), nfft)[:len(x)]
    return x + wet * y


L = reverb(L, wet=0.22)
R = reverb(np.roll(R, 37), wet=0.22)


def read_wav(path):
    with wave.open(path) as w:
        sr, ch, n = w.getframerate(), w.getnchannels(), w.getnframes()
        a = np.frombuffer(w.readframes(n), dtype=np.int16).astype(float) / 32768
    a = a.reshape(-1, ch)
    if ch == 1:
        a = np.repeat(a, 2, axis=1)
    assert sr == SR, (path, sr)
    return a


if have_music:
    m = read_wav('music.wav')[:N]
    ml, mr = np.zeros(N), np.zeros(N)
    ml[:len(m)] = m[:, 0]; mr[:len(m)] = m[:, 1]
    tt = np.arange(N) / SR
    # dark, muffled until Solen arrives, then the filter opens on the impact
    pre = tt < 12.45
    ml = np.where(pre, lp_fast(ml, 500), ml); mr = np.where(pre, lp_fast(mr, 500), mr)
    g = np.where(pre, 0.5, 0.75) * np.clip((DUR - tt) / 2.5, 0, 1)
    L += ml * g; R += mr * g

# voices: echoes with a long, washed-out tail; Solen's line clean
for name, t0, pan in [('echo1', 5.3, -0.4), ('echo2', 6.6, 0.4), ('echo3', 7.9, 0.0)]:
    if os.path.exists(name + '.wav'):
        v = read_wav(name + '.wav').mean(axis=1)
        v = hp_fast(v, 180)
        wet = reverb(np.concatenate([v, np.zeros(SR * 2)]), t60=2.6, wet=0.9)
        dly = np.zeros(len(wet) + int(0.32 * SR))
        dly[:len(wet)] += wet; dly[int(0.32 * SR):] += wet * 0.45
        add(dly, t0, 0.9, pan=pan)
if os.path.exists('solen.wav'):
    v = read_wav('solen.wav').mean(axis=1)
    add(reverb(np.concatenate([v, np.zeros(SR)]), t60=1.0, wet=0.12), 14.75, 1.1)

mix = np.stack([L, R], axis=1)
mix /= np.max(np.abs(mix)) / 0.89
with wave.open('sfx.wav', 'w') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((mix * 32767).astype(np.int16).tobytes())
print('ok', 'music' if have_music else 'fallback bed')

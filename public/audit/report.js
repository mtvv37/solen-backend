(function () {
  'use strict';
  var root = document.getElementById('report');
  var id = (location.pathname.match(/^\/r\/([A-Za-z0-9_-]{22})$/) || [])[1];
  var storageKey = 'solen-audit-' + id;

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === 'class') node.className = attrs[k];
      else if (k === 'text') node.textContent = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) { if (c) node.appendChild(typeof c === 'string' ? document.createTextNode(c) : c); });
    return node;
  }
  function readToken() { try { return localStorage.getItem(storageKey) || ''; } catch (e) { return ''; } }
  function saveToken(t) { try { localStorage.setItem(storageKey, t); } catch (e) { /* private mode */ } }
  function euros(n) { return n.toLocaleString('fr-FR') + ' €'; }
  function colorFor(ratio) { return ratio >= 0.75 ? '#7BC88F' : ratio >= 0.5 ? '#F5A524' : '#F07A5F'; }

  function ring(score) {
    var r = 70, c = 2 * Math.PI * r, ns = 'http://www.w3.org/2000/svg';
    var svg = document.createElementNS(ns, 'svg');
    svg.setAttribute('viewBox', '0 0 160 160');
    svg.setAttribute('aria-hidden', 'true');
    [['#243049', c], [colorFor(score / 100), c * score / 100]].forEach(function (p, i) {
      var circle = document.createElementNS(ns, 'circle');
      circle.setAttribute('cx', '80'); circle.setAttribute('cy', '80'); circle.setAttribute('r', String(r));
      circle.setAttribute('fill', 'none'); circle.setAttribute('stroke-width', '12');
      circle.setAttribute('stroke', p[0]);
      if (i === 1) { circle.setAttribute('stroke-linecap', 'round'); circle.setAttribute('stroke-dasharray', p[1] + ' ' + c); }
      svg.appendChild(circle);
    });
    return el('div', { class: 'ring', role: 'img', 'aria-label': 'Score ' + score + ' sur 100' }, [
      svg, el('div', { class: 'value' }, [el('b', { text: String(score) }), el('span', { text: 'sur 100' })]),
    ]);
  }

  function leakCard(leak, index) {
    if (leak.locked) {
      return el('article', { class: 'leak locked', 'aria-label': 'Fuite ' + (index + 1) + ' verrouillée' }, [
        el('span', { class: 'rank', text: String(index + 1) }),
        el('span', { class: 'cat', text: leak.categoryLabel || 'Fuite' }),
        el('h3', { class: 'blur', 'aria-hidden': 'true', text: 'Fuite de conversion détectée sur votre fiche' }),
        el('p', { class: 'blur', 'aria-hidden': 'true', text: 'Débloquez le rapport pour lire le constat, le test à lancer et le manque à gagner estimé.' }),
      ]);
    }
    return el('article', { class: 'leak' }, [
      el('span', { class: 'rank', text: String(index + 1) }),
      el('span', { class: 'cat', text: categoryLabel(leak.category) }),
      el('h3', { text: leak.title }),
      el('div', {}, [
        el('p', { text: leak.explanation }),
        el('p', { class: 'test' }, [el('b', { text: 'À tester : ' }), leak.test]),
        el('p', { class: 'money' }, [
          'Manque à gagner estimé : ' + euros(leak.monthlyLossEur.low) + ' à ' + euros(leak.monthlyLossEur.high) + ' par mois ',
          el('em', { text: '[hypothèse]' }),
        ]),
      ]),
    ]);
  }

  var labels = {};
  function categoryLabel(id) { return labels[id] || ''; }

  function unlockForm(report) {
    var error = el('p', { class: 'error', role: 'alert', hidden: '' });
    var email = el('input', { type: 'email', id: 'email', name: 'email', autocomplete: 'email', required: '', placeholder: 'vous@maboutique.fr', 'aria-label': 'Votre email' });
    var consent = el('input', { type: 'checkbox', id: 'consent', name: 'consent' });
    var button = el('button', { class: 'btn', type: 'submit', text: 'Débloquer le rapport complet' });
    var form = el('form', { class: 'unlock', novalidate: '' }, [
      el('h3', { text: (report.leakCount - report.leaks.filter(function (l) { return !l.locked; }).length) + ' autres fuites à débloquer' }),
      el('p', { text: 'Recevez le rapport complet : toutes les fuites, les tests à lancer et le manque à gagner estimé pour chacune.' }),
      email,
      el('label', { class: 'consent', for: 'consent' }, [consent, el('span', { text: 'J’accepte que Solen utilise mon email pour m’envoyer ce rapport et des conseils pour améliorer ma boutique. Désinscription possible à tout moment.' })]),
      error,
      button,
      el('p', { class: 'form-note', text: 'Votre email n’est ni vendu ni partagé.' }),
    ]);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      error.hidden = true;
      if (!consent.checked) { error.textContent = 'Cochez la case pour recevoir le rapport complet.'; error.hidden = false; return; }
      button.disabled = true;
      fetch('/api/audits/' + id + '/unlock', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email.value, consent: true }),
      })
        .then(function (res) { return res.json().then(function (d) { return { ok: res.ok, data: d }; }); })
        .then(function (r) {
          if (!r.ok) throw new Error(r.data.error || 'Erreur');
          saveToken(r.data.token);
          render(r.data.report);
        })
        .catch(function (err) { button.disabled = false; error.textContent = err.message; error.hidden = false; });
    });
    return form;
  }

  function shareBlock(report) {
    var url = location.origin + '/r/' + id;
    var text = report.shopDomain + ' : ' + report.score + '/100 à l’audit de conversion Solen.';
    var copy = el('button', { class: 'btn ghost', type: 'button', text: 'Copier le lien' });
    copy.addEventListener('click', function () {
      var done = function () { copy.textContent = 'Lien copié'; };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () { prompt('Copiez ce lien :', url); });
      else prompt('Copiez ce lien :', url);
    });
    return el('div', { class: 'share' }, [
      copy,
      el('a', { class: 'btn ghost', target: '_blank', rel: 'noopener', href: 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(text) + '&url=' + encodeURIComponent(url), text: 'Partager sur X' }),
      el('a', { class: 'btn ghost', target: '_blank', rel: 'noopener', href: 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url), text: 'Partager sur LinkedIn' }),
    ]);
  }

  function render(report) {
    labels = {};
    (report.categories || []).forEach(function (c) { labels[c.id] = c.label; });
    root.textContent = '';
    var date = new Date(report.createdAt);
    root.appendChild(el('section', { class: 'report-head' }, [
      ring(report.score),
      el('div', { class: 'meta' }, [
        el('span', { class: 'eyebrow', text: 'Audit de conversion' }),
        el('h1', { class: 'domain', text: report.shopDomain }),
        el('p', { class: 'summary', text: report.summary }),
        el('p', { class: 'small' }, ['Fiche analysée : ', el('a', { href: report.productUrl, target: '_blank', rel: 'noopener nofollow', text: report.productName || report.productUrl }),
          isNaN(date) ? '' : ' · ' + date.toLocaleDateString('fr-FR', { day: 'numeric', month: 'long', year: 'numeric' })]),
      ]),
    ]));
    if (report.isShopify === false) {
      root.appendChild(el('p', { class: 'warning', text: 'Ce site ne semble pas tourner sur Shopify. L’audit fonctionne, mais certains critères sont pensés pour Shopify.' }));
    }

    var bars = el('div', { class: 'bars' });
    (report.categories || []).forEach(function (c) {
      var ratio = c.max ? c.score / c.max : 0;
      var fill = el('i', {});
      fill.style.width = Math.round(ratio * 100) + '%';
      fill.style.background = colorFor(ratio);
      bars.appendChild(el('div', { class: 'bar-row' }, [
        el('div', { class: 'top' }, [el('b', { text: c.label }), el('span', { text: String(c.score).replace('.', ',') + ' / ' + c.max })]),
        el('div', { class: 'track' }, [fill]),
      ]));
    });
    root.appendChild(el('section', { class: 'section' }, [el('h2', { text: 'Le score en détail' }), bars]));

    var list = el('div', { class: 'leaks' });
    report.leaks.forEach(function (leak, i) { list.appendChild(leakCard(leak, i)); });
    var leakSection = el('section', { class: 'section' }, [
      el('h2', { text: report.leakCount ? 'Les fuites à corriger en priorité' : 'Aucune fuite majeure détectée' }),
      el('p', { class: 'muted', text: 'Classées par impact estimé. Chaque fuite est une hypothèse à vérifier par un test, pas un résultat.' }),
      list,
    ]);
    if (!report.unlocked && report.leaks.some(function (l) { return l.locked; })) leakSection.appendChild(unlockForm(report));
    root.appendChild(leakSection);

    var notes = el('ul', { class: 'notes' });
    ((report.assumptions && report.assumptions.notes) || []).forEach(function (n) { notes.appendChild(el('li', { text: n })); });
    root.appendChild(el('section', { class: 'section' }, [
      el('h2', { text: 'Comment lire les montants' }),
      el('p', { class: 'muted', text: 'Les montants appliquent un gain relatif estimé à un chiffre d’affaires mensuel supposé. Ils servent à prioriser, pas à prédire.' }),
      notes,
    ]));

    root.appendChild(el('section', { class: 'section' }, [el('h2', { text: 'Partager ce rapport' }), shareBlock(report)]));
    root.appendChild(el('section', { class: 'section' }, [el('div', { class: 'cta-solen' }, [
      el('span', { class: 'eyebrow', text: 'Et après ?' }),
      el('h2', { text: 'Solen teste ces corrections pour vous' }),
      el('p', { text: 'Solen propose les changements, les teste sur une partie de votre trafic et garde ce qui fait vraiment vendre plus. Vous validez chaque changement.' }),
      el('a', { class: 'btn', href: '/audit#solen', text: 'Découvrir Solen' }),
    ])]));
    document.title = report.shopDomain + ' : ' + report.score + '/100 · Audit Solen';
  }

  if (!id) { root.textContent = 'Ce rapport n’existe pas.'; return; }
  var token = readToken();
  fetch('/api/audits/' + id + (token ? '?t=' + encodeURIComponent(token) : ''))
    .then(function (res) { return res.json().then(function (d) { return { ok: res.ok, data: d }; }); })
    .then(function (r) {
      if (!r.ok) { root.textContent = r.data.error || 'Rapport introuvable.'; return; }
      render(r.data);
    })
    .catch(function () { root.textContent = 'Impossible de charger le rapport. Rechargez la page.'; });
})();

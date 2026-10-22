(function () {
  'use strict';
  var form = document.getElementById('audit-form');
  var submit = document.getElementById('submit');
  var errorEl = document.getElementById('form-error');
  var progress = document.getElementById('progress');
  var bar = document.getElementById('progress-bar');
  var label = document.getElementById('progress-label');
  var steps = [
    [8, 'Lecture du fichier robots.txt…'],
    [25, 'Lecture de la page d’accueil…'],
    [45, 'Lecture de la fiche produit…'],
    [65, 'Calcul du score…'],
    [85, 'Rédaction des fuites de conversion…'],
  ];
  var timer = null;

  function showError(message) {
    errorEl.textContent = message;
    errorEl.hidden = false;
  }

  function startProgress() {
    var i = 0;
    progress.classList.add('on');
    bar.style.width = steps[0][0] + '%';
    label.textContent = steps[0][1];
    timer = setInterval(function () {
      i = Math.min(i + 1, steps.length - 1);
      bar.style.width = steps[i][0] + '%';
      label.textContent = steps[i][1];
    }, 2600);
  }

  function stopProgress() {
    clearInterval(timer);
    progress.classList.remove('on');
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    errorEl.hidden = true;
    var url = form.url.value.trim();
    if (!url) { showError('Indiquez l’adresse de votre boutique.'); form.url.focus(); return; }
    var payload = { url: url };
    var visitors = Number(form.monthlyVisitors.value);
    var aov = Number(form.averageOrderValue.value);
    if (visitors > 0) payload.monthlyVisitors = visitors;
    if (aov > 0) payload.averageOrderValue = aov;

    submit.disabled = true;
    submit.textContent = 'Analyse en cours…';
    startProgress();

    fetch('/api/audits', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
      .then(function (res) { return res.json().then(function (data) { return { ok: res.ok, data: data }; }); })
      .then(function (r) {
        if (!r.ok) throw new Error(r.data.error || 'L’audit n’a pas pu aboutir.');
        bar.style.width = '100%';
        label.textContent = 'Rapport prêt.';
        window.location.href = r.data.reportUrl;
      })
      .catch(function (err) {
        stopProgress();
        submit.disabled = false;
        submit.textContent = 'Lancer l’audit';
        showError(err.message && err.message !== 'Failed to fetch' ? err.message : 'Connexion impossible. Vérifiez votre réseau et réessayez.');
      });
  });
})();

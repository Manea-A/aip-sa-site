/* AIP – aip-sa.com. Small progressive-enhancement script, no dependencies.
   Every page works without it (Arabic content, links and mailto forms). */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js');

  var MAIL_TO = 'info@aip-sa.com';
  var LANG_KEY = 'aip-lang';

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $all(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }
  function currentLang() { return root.lang === 'en' ? 'en' : 'ar'; }

  function readStored() { try { return window.localStorage.getItem(LANG_KEY); } catch (e) { return null; } }
  function writeStored(v) { try { window.localStorage.setItem(LANG_KEY, v); } catch (e) { /* ignore */ } }

  /* ---------- Language (Arabic RTL / English LTR) ---------- */
  function setLang(lang) {
    lang = lang === 'en' ? 'en' : 'ar';
    root.lang = lang;
    root.dir = lang === 'ar' ? 'rtl' : 'ltr';
    $all('[data-ar]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang);
      if (v !== null) { el.textContent = v; }
      // Some pricing blocks were Arabic-only in the original and are marked lang="ar";
      // translated items inside them need their own lang while English is shown.
      var arParent = el.parentElement && el.parentElement.closest('[lang="ar"]');
      if (lang === 'en' && arParent && arParent !== root) { el.setAttribute('lang', 'en'); }
      else if (el.getAttribute('lang') === 'en' && v !== null && el.hasAttribute('data-en')) { el.removeAttribute('lang'); }
    });
    $all('[data-ar-alt]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang + '-alt');
      if (v !== null) { el.setAttribute('alt', v); }
    });
    $all('[data-ar-label]').forEach(function (el) {
      var v = el.getAttribute('data-' + lang + '-label');
      if (v !== null) { el.setAttribute('aria-label', v); }
    });
    var title = root.getAttribute('data-title-' + lang);
    if (title) { document.title = title; }
    var btn = $('#langToggle');
    if (btn) {
      btn.textContent = lang === 'ar' ? 'EN' : 'عربي';
      btn.setAttribute('lang', lang === 'ar' ? 'en' : 'ar');
      btn.setAttribute('aria-label', lang === 'ar' ? 'Switch to English' : 'التبديل إلى العربية');
    }
  }

  var params = new URLSearchParams(window.location.search);
  var initial = params.get('lang') || readStored();
  if (initial === 'en') { setLang('en'); }

  var langBtn = $('#langToggle');
  if (langBtn) {
    langBtn.addEventListener('click', function () {
      var next = currentLang() === 'ar' ? 'en' : 'ar';
      setLang(next);
      writeStored(next);
    });
  }

  /* ---------- Navigation ---------- */
  var navbar = $('#navbar');
  var menuBtn = $('#menuToggle');
  var menu = $('#navMenu');
  function closeMenu() {
    if (!menuBtn) { return; }
    menuBtn.setAttribute('aria-expanded', 'false');
    menu.classList.remove('is-open');
  }
  if (menuBtn && menu) {
    menuBtn.addEventListener('click', function () {
      var open = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!open));
      menu.classList.toggle('is-open', !open);
    });
    $all('a', menu).forEach(function (a) { a.addEventListener('click', closeMenu); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) { closeMenu(); menuBtn.focus(); }
    });
  }

  var scrollTop = $('#scrollTop');
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (navbar) { navbar.classList.toggle('is-scrolled', y > 10); }
    if (scrollTop) { scrollTop.classList.toggle('is-visible', y > 600); }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Forms: open the visitor's mail app addressed to MAIL_TO ---------- */
  function labelFor(form, field) {
    var l = form.querySelector('label[for="' + field.id + '"]');
    return (l ? l.textContent : field.name).replace('*', '').trim();
  }
  function sendByMail(form, subject) {
    var lines = [];
    $all('input, textarea', form).forEach(function (f) {
      if (f.type === 'submit' || !f.name || !f.value.trim()) { return; }
      lines.push(labelFor(form, f) + ': ' + f.value.trim());
    });
    window.location.href = 'mailto:' + MAIL_TO +
      '?subject=' + encodeURIComponent(subject) +
      '&body=' + encodeURIComponent(lines.join('\n'));
  }

  var contactForm = $('#contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = (contactForm.elements.name && contactForm.elements.name.value.trim()) || '';
      sendByMail(contactForm, (currentLang() === 'ar' ? 'تواصل من موقع AIP' : 'AIP website enquiry') + (name ? ' - ' + name : ''));
    });
  }

  /* ---------- Pricing page ---------- */
  // Agents: show the first 20, button reveals all
  var agentsGrid = $('#fath-agents-grid');
  var showAll = $('#showAllAgentsBtn');
  if (agentsGrid && showAll) {
    agentsGrid.classList.add('is-collapsed');
    showAll.setAttribute('aria-expanded', 'false');
    showAll.addEventListener('click', function () {
      agentsGrid.classList.remove('is-collapsed');
      showAll.setAttribute('aria-expanded', 'true');
      showAll.hidden = true;
      var firstHidden = agentsGrid.children[20];
      if (firstHidden) { firstHidden.focus(); }
    });
  }

  // Agents: click to select, selection is copied into the request form
  var selectedAgents = $('#selectedAgents');
  function syncAgents() {
    if (!selectedAgents) { return; }
    selectedAgents.value = $all('.agent-card[aria-pressed="true"] .agent-name').map(function (n) {
      return n.textContent.trim();
    }).join('، ');
  }
  $all('.agent-card').forEach(function (card) {
    card.addEventListener('click', function () {
      card.setAttribute('aria-pressed', String(card.getAttribute('aria-pressed') !== 'true'));
      syncAgents();
    });
  });

  // Carousels
  $all('.pricing-grid-wrapper').forEach(function (wrap) {
    var track = $('.pricing-grid', wrap);
    if (!track) { return; }
    function update() { wrap.classList.toggle('has-overflow', track.scrollWidth > track.clientWidth + 4); }
    function step(dir) {
      var card = track.firstElementChild;
      var amount = card ? card.getBoundingClientRect().width + 22 : 300;
      var physical = root.dir === 'rtl' ? -dir : dir; // "next" moves toward the reading direction
      track.scrollBy({ left: physical * amount, behavior: 'smooth' });
    }
    $all('.carousel-arrow', wrap).forEach(function (b) {
      b.addEventListener('click', function () { step(b.classList.contains('next') ? 1 : -1); });
    });
    window.addEventListener('resize', update);
    update();
  });

  // Package request dialog
  var modal = $('#contactModal');
  var packageForm = $('#packageForm');
  if (modal && packageForm && typeof modal.showModal === 'function') {
    var lastTrigger = null;
    $all('[data-package]').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        lastTrigger = btn;
        $('#packageName').value = btn.getAttribute('data-package');
        syncAgents();
        modal.showModal();
        $('#fullName').focus();
      });
    });
    $('#closeModal').addEventListener('click', function () { modal.close(); });
    modal.addEventListener('click', function (e) { if (e.target === modal) { modal.close(); } });
    modal.addEventListener('close', function () { if (lastTrigger) { lastTrigger.focus(); } });
    packageForm.addEventListener('submit', function (e) {
      e.preventDefault();
      sendByMail(packageForm, 'طلب باقة: ' + ($('#packageName').value || ''));
      modal.close();
    });
  }
})();

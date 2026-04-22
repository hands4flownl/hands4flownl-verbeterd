---
layout: default
title: "Contact"
description: "Neem contact op met hands4flow in Emmen – afspraak maken voor massage, coaching of Reiki."
permalink: /contact/
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{ '/' | absolute_url }}">Home</a>
    <span>Contact</span>
  </div>
  <span class="section-label">Afspraak of vraag?</span>
  <h1 class="section-title">Neem contact op</h1>
  <p class="section-sub">Ik help je graag verder. Stuur een bericht of WhatsApp mij direct.</p>
</section>

<section style="background:var(--white);">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:start;max-width:1000px;margin:0 auto;">

    <!-- Contactgegevens + social -->
    <div>
      <span class="section-label">Bereikbaarheid</span>
      <h2 class="section-title">hands4flow<br>Emmen</h2>

      <div class="about-values">
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">
            <strong>Adres:</strong> Laan van de Marel 55, 7823 BN Emmen<br/>
            <em style="font-size:.82rem;">(Praktijk aan huis, eerste etage)</em>
          </p>
        </div>
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">
            <strong>Telefoon:</strong>
            <a href="tel:+31659111456">06 59 11 14 56</a>
          </p>
        </div>
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">
            <strong>E-mail:</strong>
            <a href="mailto:info@hands4flow.nl">info@hands4flow.nl</a>
          </p>
        </div>
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text"><strong>KVK:</strong> 97209341</p>
        </div>
        {% if site.data.contact.gegevens.openingstijden %}
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text"><strong>Beschikbaarheid:</strong><br/>{{ site.data.contact.gegevens.openingstijden }}</p>
        </div>
        {% endif %}
        {% if site.data.contact.gegevens.beschikbaarheid_melding and site.data.contact.gegevens.beschikbaarheid_melding != "" %}
        <div style="background:var(--oker-xlt);border-left:3px solid var(--oker);border-radius:0 8px 8px 0;padding:.7rem 1rem;margin-top:.5rem;">
          <p style="font-size:.88rem;color:var(--bruin);margin:0;">📅 {{ site.data.contact.gegevens.beschikbaarheid_melding }}</p>
        </div>
        {% endif %}
      </div>

      <br/>
      <a href="https://api.whatsapp.com/send?phone=31659111456"
         target="_blank" rel="noopener"
         class="btn-primary">💬 Direct WhatsApp sturen</a>

      <!-- Social media -->
      <div style="margin-top:2.5rem;">
        <p style="font-size:.82rem;font-weight:500;color:var(--bruin);margin-bottom:.8rem;">Volg mij ook op:</p>
        <div style="display:flex;gap:.6rem;flex-wrap:wrap;">

          <a href="https://www.facebook.com/elsemarie.vanderploeg" target="_blank" rel="noopener"
             style="display:inline-flex;align-items:center;gap:.4rem;background:#1877F2;color:#fff;padding:.45rem 1rem;border-radius:50px;font-size:.82rem;font-weight:500;text-decoration:none;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073C0 18.1 4.388 23.094 10.125 24v-8.437H7.078v-3.49h3.047V9.413c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.49h-2.796V24C19.612 23.094 24 18.1 24 12.073z"/></svg>
            Facebook
          </a>

          <a href="https://www.instagram.com/hands4flow" target="_blank" rel="noopener"
             style="display:inline-flex;align-items:center;gap:.4rem;background:radial-gradient(circle at 30% 107%,#fdf497 0,#fdf497 5%,#fd5949 45%,#d6249f 60%,#285AEB 90%);color:#fff;padding:.45rem 1rem;border-radius:50px;font-size:.82rem;font-weight:500;text-decoration:none;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
            Instagram
          </a>

          <a href="https://www.linkedin.com/in/elsemarie-van-der-ploeg-8a06a29a" target="_blank" rel="noopener"
             style="display:inline-flex;align-items:center;gap:.4rem;background:#0A66C2;color:#fff;padding:.45rem 1rem;border-radius:50px;font-size:.82rem;font-weight:500;text-decoration:none;">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            LinkedIn
          </a>

        </div>
      </div>

      <div class="info-box" style="margin-top:2rem;">
        <strong>Praktische info:</strong><br/>
        Alle tarieven zijn BTW vrij.<br/>
        Behandelingen worden niet vergoed door de zorgverzekering.<br/>
        Jouw gegevens worden nooit aan derden verstrekt.
      </div>
    </div>

    <!-- Formulier -->
    <div>
      <span class="section-label">Afspraak maken</span>
      <h2 class="section-title">Stuur een bericht</h2>
      <p class="section-sub" style="margin-bottom:1.5rem;">
        Vul het formulier in en ik neem zo snel mogelijk contact met je op.
      </p>

      <form action="https://formspree.io/f/JOUW_FORMSPREE_ID"
            method="POST"
            style="display:flex;flex-direction:column;gap:1rem;">

        <input type="hidden" name="_next" value="{{ '/contact/' | absolute_url }}?bedankt=1"/>
        <input type="hidden" name="_subject" value="Nieuwe afspraakaanvraag – hands4flow"/>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
          <div>
            <label for="naam" style="font-size:.82rem;font-weight:500;color:var(--bruin);display:block;margin-bottom:.3rem;">Naam *</label>
            <input id="naam" type="text" name="naam" required placeholder="Jouw naam"
              style="width:100%;padding:.75rem 1rem;border:1.5px solid var(--oker-lt);border-radius:10px;font-family:inherit;font-size:.92rem;background:var(--creme);color:var(--text);outline:none;transition:border-color .2s;"
              onfocus="this.style.borderColor='var(--oker)'"
              onblur="this.style.borderColor='var(--oker-lt)'"/>
          </div>
          <div>
            <label for="tel" style="font-size:.82rem;font-weight:500;color:var(--bruin);display:block;margin-bottom:.3rem;">Telefoon</label>
            <input id="tel" type="tel" name="telefoon" placeholder="06 ..."
              style="width:100%;padding:.75rem 1rem;border:1.5px solid var(--oker-lt);border-radius:10px;font-family:inherit;font-size:.92rem;background:var(--creme);color:var(--text);outline:none;transition:border-color .2s;"
              onfocus="this.style.borderColor='var(--oker)'"
              onblur="this.style.borderColor='var(--oker-lt)'"/>
          </div>
        </div>

        <div>
          <label for="email" style="font-size:.82rem;font-weight:500;color:var(--bruin);display:block;margin-bottom:.3rem;">E-mailadres *</label>
          <input id="email" type="email" name="email" required placeholder="jouw@email.nl"
            style="width:100%;padding:.75rem 1rem;border:1.5px solid var(--oker-lt);border-radius:10px;font-family:inherit;font-size:.92rem;background:var(--creme);color:var(--text);outline:none;transition:border-color .2s;"
            onfocus="this.style.borderColor='var(--oker)'"
            onblur="this.style.borderColor='var(--oker-lt)'"/>
        </div>

        <div>
          <label for="behandeling" style="font-size:.82rem;font-weight:500;color:var(--bruin);display:block;margin-bottom:.3rem;">Behandeling</label>
          <select id="behandeling" name="behandeling"
            style="width:100%;padding:.75rem 1rem;border:1.5px solid var(--oker-lt);border-radius:10px;font-family:inherit;font-size:.92rem;background:var(--creme);color:var(--text);outline:none;transition:border-color .2s;"
            onfocus="this.style.borderColor='var(--oker)'"
            onblur="this.style.borderColor='var(--oker-lt)'">
            <option value="">Maak een keuze...</option>
            <option>Voetreflexmassage</option>
            <option>Reiki</option>
            <option>Reiki op afstand</option>
            <option>Acces Bars</option>
            <option>Stoelmassage</option>
            <option>Happy Soul Sessie (Coaching)</option>
            <option>Combinatie / weet nog niet</option>
          </select>
        </div>

        <div>
          <label for="bericht" style="font-size:.82rem;font-weight:500;color:var(--bruin);display:block;margin-bottom:.3rem;">Bericht</label>
          <textarea id="bericht" name="bericht" rows="4"
            placeholder="Je vraag, gewenste dag/tijd of andere informatie..."
            style="width:100%;padding:.75rem 1rem;border:1.5px solid var(--oker-lt);border-radius:10px;font-family:inherit;font-size:.92rem;background:var(--creme);color:var(--text);outline:none;resize:vertical;transition:border-color .2s;"
            onfocus="this.style.borderColor='var(--oker)'"
            onblur="this.style.borderColor='var(--oker-lt)'"></textarea>
        </div>

        <input type="text" name="_gotcha" style="display:none"/>

        <button type="submit"
          style="background:var(--oker);color:#fff;border:none;padding:.85rem 2rem;border-radius:100px;font-size:.9rem;font-weight:500;cursor:pointer;font-family:inherit;letter-spacing:.03em;transition:background .2s;"
          onmouseover="this.style.background='var(--bruin)'"
          onmouseout="this.style.background='var(--oker)'">
          Verstuur bericht ✓
        </button>

        <p style="font-size:.78rem;color:var(--bruin-lt);">* verplichte velden</p>
      </form>
    </div>

  </div>
</section>

<!-- Kaart via OpenStreetMap — geen API key nodig -->
<section style="background:var(--creme);padding:4rem 5vw;">
  <div style="max-width:1000px;margin:0 auto;">
    <span class="section-label">Locatie</span>
    <h2 class="section-title" style="margin-bottom:1.5rem;">Vind de praktijk</h2>
    <div style="border-radius:20px;overflow:hidden;box-shadow:0 4px 24px rgba(0,0,0,.08);">
      <iframe
        src="https://www.openstreetmap.org/export/embed.html?bbox=6.8750%2C52.7760%2C6.9050%2C52.7880&layer=mapnik&marker=52.7820%2C6.8900"
        width="100%" height="380" style="border:0;display:block;"
        allowfullscreen="" loading="lazy">
      </iframe>
    </div>
    <div style="display:flex;gap:1rem;margin-top:1.2rem;flex-wrap:wrap;">
      <a href="https://www.google.com/maps/dir/?api=1&destination=Laan+van+de+Marel+55,+7823+BN+Emmen"
         target="_blank" rel="noopener" class="btn-primary">
        📍 Open in Google Maps
      </a>
      <a href="https://maps.apple.com/?address=Laan+van+de+Marel+55,+7823+BN+Emmen,+Nederland"
         target="_blank" rel="noopener" class="btn-secondary">
        🗺 Open in Apple Kaarten
      </a>
    </div>
  </div>
</section>

<!-- Bedankt-melding na verzenden -->
<script>
  if (window.location.search.includes('bedankt=1')) {
    var el = document.createElement('div');
    el.innerHTML = '<div style="position:fixed;top:88px;left:50%;transform:translateX(-50%);background:var(--oker);color:#fff;padding:1rem 2rem;border-radius:100px;font-size:.95rem;font-weight:500;z-index:999;box-shadow:0 4px 20px rgba(0,0,0,.15);">✓ Bedankt! Ik neem zo snel mogelijk contact op.</div>';
    document.body.appendChild(el);
    setTimeout(function(){ el.remove(); }, 5000);
  }
</script>

<section class="contact">
  <h2 class="section-title">Ik kijk ernaar uit<br>je te ont-moeten</h2>
  <p class="section-sub">Tot ziens in mijn praktijk in Emmen.</p>
  <div class="contact-options">
    <a href="https://api.whatsapp.com/send?phone=31659111456"
       class="contact-btn contact-btn-whatsapp"
       target="_blank" rel="noopener">💬 WhatsApp mij</a>
    <a href="tel:+31659111456" class="contact-btn contact-btn-call">📞 Bel mij</a>
  </div>
  <div class="contact-info">
    <span><strong>Locatie</strong>Emmen, Nederland</span>
    <span><strong>Telefoon</strong>06 59 11 14 56</span>
    <span><strong>KVK</strong>97209341</span>
  </div>
</section>

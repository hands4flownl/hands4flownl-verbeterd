---
layout: default
title: "Over mij"
description: "Leer Elsemarie van der Ploeg kennen – Voetreflexmasseur, Reiki Master en coach in Emmen."
permalink: /over-mij/
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{ '/' | absolute_url }}">Home</a>
    <span>Over mij</span>
  </div>
  <span class="section-label">Wie ben ik?</span>
  <h1 class="section-title">Over Elsemarie</h1>
  <p class="section-sub">Voetreflexmasseur, Reiki Master &amp; Coach in Emmen</p>
</section>

<section style="background:var(--white);">
  <div class="about">
    <div class="about-img-wrap">
      <img class="about-img"
           src="{% if site.data['over-mij'].inhoud.foto %}{{ site.data['over-mij'].inhoud.foto }}{% else %}https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/1000019670-high.jpg?enable-io=true&enable=upscale&width=700{% endif %}"
           alt="Elsemarie van der Ploeg – hands4flow Emmen" />
      <span class="about-tag">Reiki Master ✦ Coach</span>
    </div>
    <div>
      <span class="section-label">Mijn verhaal</span>
      <h2 class="section-title">Hallo, ik ben<br>Elsemarie</h2>
      <p class="section-sub">
        Ik ben Elsemarie van der Ploeg en ben blij dat je mijn praktijk voor massage, coaching &amp; Reiki in Emmen gevonden hebt.
        Naast mijn werk in de gezondheidszorg werk ik met veel liefde in mijn praktijk.
      </p>
      <p class="section-sub" style="margin-top:1rem;">
        Ik neem de tijd voor jou — met aandacht, zachtheid en vertrouwen. Ik kijk verder dan alleen de klacht
        en stem intuïtief af op wat jij op dat moment nodig hebt. Soms is een combinatie van behandelingen
        precies wat er nodig is.
      </p>
      <p class="section-sub" style="margin-top:1rem;font-style:italic;">
        Warme groet, Elsemarie
      </p>
      <div class="about-values" style="margin-top:2rem;">
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">Lid van Reiki Vereniging Cirkel —
            <a href="https://www.reikicirkel.nl" target="_blank" rel="noopener">reikicirkel.nl</a></p>
        </div>
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">Gecertificeerd Acces Bars behandelaar</p>
        </div>
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">Opgeleid als coach door José van Eldik in Valthe —
            <a href="http://www.josevaneldik.nl" target="_blank" rel="noopener">josevaneldik.nl</a></p>
        </div>
        <div class="value-item">
          <div class="value-dot"></div>
          <p class="value-text">Werkzaam in de gezondheidszorg naast de praktijk</p>
        </div>
      </div>
      <br/>
      <a href="{{ '/contact/' | absolute_url }}" class="btn-primary">Plan jouw afspraak</a>
      <a href="{{ '/behandelingen/' | absolute_url }}" class="btn-secondary" style="margin-left:.5rem;">Bekijk behandelingen</a>
    </div>
  </div>
</section>

<!-- ── ANDERE INITIATIEVEN (hier thuishorend, niet op homepage) ── -->
<section style="background:var(--creme);">
  <div style="max-width:900px;margin:0 auto;">
    <span class="section-label">Meer van Elsemarie</span>
    <h2 class="section-title" style="font-size:1.6rem;">Andere initiatieven</h2>

    <div style="display:grid;grid-template-columns:1fr 1fr;gap:3rem;margin-top:2rem;align-items:start;">
      <div>
        <a href="https://www.nederland-bewust.nl" target="_blank" rel="noopener">
          <img src="https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/nederland-bewust-logo-transparant-high.png?enable-io=true&enable=upscale&width=300"
               alt="Nederland Bewust" style="max-height:80px;object-fit:contain;margin-bottom:1rem;" />
        </a>
        <p style="font-size:.9rem;color:var(--bruin-lt);line-height:1.7;">
          Elsemarie is mede-initiatiefneemster van <a href="https://www.nederland-bewust.nl" target="_blank" rel="noopener" style="color:var(--oker);">nederland-bewust.nl</a> — de startpagina voor alternatieve zorg, holistische therapie en natuurlijke gezondheid.
        </p>
      </div>
      <div>
        <a href="https://www.jouwcoachlijn.com" target="_blank" rel="noopener">
          <img src="https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/logo_jcl_edited_v2_bg_transparent_-high.png?enable-io=true&enable=upscale&width=300"
               alt="JouwCoachLijn" style="max-height:80px;object-fit:contain;margin-bottom:1rem;" />
        </a>
        <p style="font-size:.9rem;color:var(--bruin-lt);line-height:1.7;">
          Op zoek naar een luisterend oor? Bel <strong>0900-1881</strong> (80 cpm) via <a href="https://www.jouwcoachlijn.com" target="_blank" rel="noopener" style="color:var(--oker);">JouwCoachLijn</a> — Elsemarie luistert zonder oordeel.
        </p>
      </div>
    </div>
  </div>
</section>

<section class="contact">
  <h2 class="section-title">Klaar voor ontspanning?</h2>
  <p class="section-sub">Ik kijk ernaar uit je te ontmoeten in mijn praktijk in Emmen.</p>
  <div class="contact-options">
    <a href="https://api.whatsapp.com/send?phone=31659111456" class="contact-btn contact-btn-whatsapp">💬 WhatsApp mij</a>
    <a href="{{ '/contact/' | absolute_url }}" class="contact-btn contact-btn-mail">✉ Neem contact op</a>
  </div>
</section>

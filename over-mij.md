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
        Ik ben Elsemarie van der Ploeg en ben blij dat je mijn massage, coaching &amp; Reiki praktijk in Emmen gevonden hebt.
      </p>
      <p class="section-sub" style="margin-top:1rem;">
        Naast mijn werk in de gezondheidszorg werk ik met veel liefde in mijn praktijk.
      </p>
      <p class="section-sub" style="margin-top:1rem;">
        In mijn praktijk neem ik de tijd voor jou, met aandacht, zachtheid en vertrouwen. Ik kijk verder dan alleen de klacht en stem intuïtief af op wat jij op dat moment nodig hebt. Het kan ook voorkomen dat je een combinatie van twee of zelfs drie behandelingen nodig hebt.
      </p>
      <p class="section-sub" style="margin-top:1rem;">
        Ik kijk er dan ook naar uit je te ont-moeten.
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
      <a href="{{ '/behandelingen/' | absolute_url }}" class="btn-secondary">Bekijk behandelingen</a>
    </div>
  </div>
</section>

<section style="background:var(--oker-xlt);">
  <div style="max-width:780px;margin:0 auto;text-align:center;">
    <span class="section-label">Mijn werkwijze</span>
    <h2 class="section-title">Persoonlijke aanpak</h2>
    <p class="section-sub" style="margin:0 auto;">
      Ik luister naar jouw verhaal en stem de behandeling af op jouw specifieke wensen.
      Mijn doel is om jou te helpen ontspannen en je energie weer te laten stromen.
      Een combinatie van verschillende behandelingen behoort ook tot de mogelijkheden.
    </p>
    <br/><br/>
    <a href="{{ '/tarieven/' | absolute_url }}" class="btn-primary">Bekijk de tarieven</a>
  </div>
</section>

<section class="contact">
  <span class="section-label">Contact</span>
  <h2 class="section-title">Klaar voor ontspanning?</h2>
  <p class="section-sub">Neem vandaag nog contact op. Ik kijk ernaar uit je te ontmoeten in mijn praktijk in Emmen.</p>
  <div class="contact-options">
    <a href="https://api.whatsapp.com/send?phone=31659111456" class="contact-btn contact-btn-whatsapp">💬 WhatsApp mij</a>
    <a href="{{ '/contact/' | absolute_url }}" class="contact-btn contact-btn-mail">✉ Neem contact op</a>
  </div>
</section>

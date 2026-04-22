---
layout: default
title: "Voetreflexmassage Emmen"
description: "Voetreflexmassage bij hands4flow in Emmen – ontspanning, doorbloeding en zelfherstel."
permalink: /behandelingen/voetreflexmassage/
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{ '/' | absolute_url }}">Home</a>
    <span><a href="{{ '/behandelingen/' | absolute_url }}">Behandelingen</a></span>
    <span>Voetreflexmassage</span>
  </div>
  <span class="section-label">Behandeling</span>
  <h1 class="section-title">Voetreflexmassage</h1>
  <p class="section-sub">Diepe ontspanning via de voeten — heel het lichaam voelt het.</p>
</section>

<section style="background:var(--white);">
  <div class="treatment-detail">
    {% assign data = site.data.voetreflexmassage %}
    {% if data.hero.afbeelding %}
    <img src="{{ data.hero.afbeelding }}" alt="Voetreflexmassage bij hands4flow Emmen" />
    {% else %}
    <img src="https://primary.jwwb.nl/pexels/52/5240642.jpeg?enable-io=true&enable=upscale&crop=1.4286%3A1&width=800" alt="Voetreflexmassage bij hands4flow Emmen" />
    {% endif %}
    <div class="content">

      <p>Bij een voetreflexmassage wordt druk uitgeoefend op specifieke punten op de voet — elk punt correspondeert met een orgaan of lichaamsdeel. Het stimuleert het zelfherstellend vermogen, bevordert de doorbloeding en geeft diepe ontspanning.</p>

      <div class="info-box" style="background:var(--oker-xlt);border-left:3px solid var(--oker);padding:1.2rem 1.4rem;border-radius:8px;margin-bottom:1rem;">
        <strong>Fijn als je last hebt van:</strong><br/>
        Stress · Vermoeidheid · Slaapproblemen · Gespannen spieren · Behoefte aan ontspanning
      </div>

      <div class="info-box">
        <strong>Duur &amp; tarief:</strong><br/>
        30 minuten — € 30,00<br/>
        60 minuten — € 60,00
      </div>

      <details style="margin:1rem 0;cursor:pointer;">
        <summary style="color:var(--oker);font-size:.9rem;font-weight:500;">Meer informatie over voetreflexmassage</summary>
        <div style="margin-top:1rem;font-size:.92rem;line-height:1.8;color:var(--bruin);">
          <p>Elk orgaan en gedeelte van je lichaam heeft een reflectiepunt op de voet. Door hier druk op uit te oefenen worden de desbetreffende delen en organen behandeld. De behandeling verbetert ook de afvoer van afvalstoffen.</p>
          <p>Na de behandeling is het fijn om rust in te plannen en voldoende water te drinken. Draag bij voorkeur kleding waarbij de broekspijpen makkelijk oprollen tot boven de knie.</p>
          <p>Regelmatig komen? Strippenkaarten beschikbaar — 5x of 10x, vraag ernaar via contact.</p>
        </div>
      </details>

      <a href="{{ '/contact/' | absolute_url }}" class="btn-primary">Afspraak maken</a>
      <a href="{{ '/tarieven/' | absolute_url }}" class="btn-secondary" style="margin-left:.5rem;">Alle tarieven</a>
    </div>
  </div>
</section>

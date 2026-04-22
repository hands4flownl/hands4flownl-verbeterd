---
layout: default
title: "Stoelmassage Emmen"
description: "Stoelmassage bij hands4flow Emmen – snel ontspannen, rug, nek en schouders, over de kleding."
permalink: /behandelingen/stoelmassage/
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{ '/' | absolute_url }}">Home</a>
    <span><a href="{{ '/behandelingen/' | absolute_url }}">Behandelingen</a></span>
    <span>Stoelmassage</span>
  </div>
  <span class="section-label">Behandeling</span>
  <h1 class="section-title">Stoelmassage</h1>
  <p class="section-sub">Direct verlichting voor rug, nek en schouders — over de kleding, laagdrempelig.</p>
</section>

<section style="background:var(--white);">
  <div class="treatment-detail">
    {% assign data = site.data.stoelmassage %}
    {% if data.hero.afbeelding %}
    <img src="{{ data.hero.afbeelding }}" alt="Stoelmassage bij hands4flow Emmen" />
    {% else %}
    <img src="https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/file_00000000476061f78aa2a0ee9f74f998-high.png?enable-io=true&enable=upscale&crop=1.4286%3A1&width=800" alt="Stoelmassage bij hands4flow Emmen" />
    {% endif %}
    <div class="content">

      <p>Een stoelmassage is een korte, ontspannende massage van rug, nek, schouders, hoofd, armen en handen — gegeven over de kleding heen in een speciaal ergonomische stoel. Direct effectief, geen voorbereiding nodig.</p>

      <div class="info-box" style="background:var(--oker-xlt);border-left:3px solid var(--oker);padding:1.2rem 1.4rem;border-radius:8px;margin-bottom:1rem;">
        <strong>Fijn als je last hebt van:</strong><br/>
        Nekklachten · Hoofdpijn · Vastzittende schouders · Rugspanning
      </div>

      <div class="info-box">
        <strong>Duur &amp; tarief:</strong><br/>
        30 minuten — € 35,00
      </div>

      <a href="{{ '/contact/' | absolute_url }}" class="btn-primary">Afspraak maken</a>
      <a href="{{ '/tarieven/' | absolute_url }}" class="btn-secondary" style="margin-left:.5rem;">Alle tarieven</a>
    </div>
  </div>
</section>

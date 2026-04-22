---
layout: default
title: "Acces Bars behandeling Emmen"
description: "Acces Bars bij hands4flow Emmen – beperkende patronen loslaten, beter slapen, meer rust."
permalink: /behandelingen/acces-bars/
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{ '/' | absolute_url }}">Home</a>
    <span><a href="{{ '/behandelingen/' | absolute_url }}">Behandelingen</a></span>
    <span>Acces Bars</span>
  </div>
  <span class="section-label">Behandeling</span>
  <h1 class="section-title">Acces Bars</h1>
  <p class="section-sub">Alsof je een knop indrukt en je lichaam reset.</p>
</section>

<section style="background:var(--white);">
  <div class="treatment-detail">
    {% assign data = site.data["acces-bars"] %}
    {% if data.hero.afbeelding %}
    <img src="{{ data.hero.afbeelding }}" alt="Acces Bars behandeling bij hands4flow Emmen" />
    {% else %}
    <img src="https://primary.jwwb.nl/pexels/38/3865496.jpeg?enable-io=true&enable=upscale&crop=1.388%3A1%2Coffset-y40&width=800" alt="Acces Bars behandeling bij hands4flow Emmen" />
    {% endif %}
    <div class="content">

      <p>Bij een Acces Bars behandeling worden 32 energiepunten op het hoofd zacht aangeraakt. Elk punt staat in verband met een thema in je leven — zoals stress, controle, slaap of creativiteit. Door de aanraking laat je beperkende gedachten en patronen los.</p>

      <div class="info-box" style="background:var(--oker-xlt);border-left:3px solid var(--oker);padding:1.2rem 1.4rem;border-radius:8px;margin-bottom:1rem;">
        <strong>Fijn als je last hebt van:</strong><br/>
        Slaapproblemen · Stress · Druk hoofd · Vastgelopen patronen · Behoefte aan meer helderheid
      </div>

      <div class="info-box">
        <strong>Duur &amp; tarief:</strong><br/>
        60 minuten — € 60,00
      </div>

      <details style="margin:1rem 0;cursor:pointer;">
        <summary style="color:var(--oker);font-size:.9rem;font-weight:500;">Wat levert Acces Bars op?</summary>
        <div style="margin-top:1rem;font-size:.92rem;line-height:1.8;color:var(--bruin);">
          <p>Meer rust, helderder denken, beter slapen en meer balans. Lichamelijke klachten kunnen verminderen. Veel mensen beschrijven het als "mijn hoofd is eindelijk eens stil".</p>
          <p>Regelmatig komen? Strippenkaarten beschikbaar — 5x of 10x.</p>
        </div>
      </details>

      <a href="{{ '/contact/' | absolute_url }}" class="btn-primary">Afspraak maken</a>
      <a href="{{ '/tarieven/' | absolute_url }}" class="btn-secondary" style="margin-left:.5rem;">Alle tarieven</a>
    </div>
  </div>
</section>

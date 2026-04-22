---
layout: default
title: "♥️ Blog"
description: "Lees de laatste blogposts van hands4flow over massage, Reiki, coaching en welzijn."
permalink: /blog/
---

<section class="page-hero">
  <div class="breadcrumb">
    <a href="{{ '/' | absolute_url }}">Home</a>
    <span><a href="{{ '/faq/' | absolute_url }}">Info</a></span>
    <span>♥️ Blog</span>
  </div>
  <span class="section-label">Lees & inspireer</span>
  <h1 class="section-title">♥️ Blog</h1>
  <p class="section-sub">
    Welkom op mijn blog! Hier deel ik persoonlijke ervaringen, tips en inzichten over massage, Reiki, coaching en welzijn.
  </p>
</section>

<section style="background:var(--white);">
  <div style="max-width:900px;margin:0 auto;">
    
    {% if site.posts.size > 0 %}
      <div style="display:grid;gap:2rem;">
        {% for post in site.posts %}
          <article style="background:var(--creme-mid);border-radius:20px;padding:2rem;transition:transform .3s,box-shadow .3s;"
                   onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 10px 36px rgba(154,125,0,.12)'"
                   onmouseout="this.style.transform='';this.style.boxShadow=''">
            
            {% if post.afbeelding %}
            <img src="{{ post.afbeelding }}" alt="{{ post.title }}" style="width:100%;border-radius:12px;margin-bottom:1.2rem;object-fit:cover;max-height:240px;" />
            {% endif %}
            
            <div style="font-size:.8rem;color:var(--bruin-mid);margin-bottom:.5rem;">
              {{ post.date | date: "%d %B %Y" }}
            </div>
            
            <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:400;color:var(--bruin);margin-bottom:.8rem;">
              <a href="{{ post.url | relative_url }}" style="text-decoration:none;color:inherit;">
                {{ post.title }}
              </a>
            </h2>
            
            <p style="font-size:.95rem;font-weight:300;color:var(--bruin-lt);line-height:1.75;margin-bottom:1rem;">
              {{ post.excerpt | strip_html | truncatewords: 40 }}
            </p>
            
            <a href="{{ post.url | relative_url }}" class="card-link">Lees meer</a>
          </article>
        {% endfor %}
      </div>
    {% else %}
      <!-- Geen posts gevonden -->
      <div style="text-align:center;padding:4rem 0;">
        <div style="font-size:3rem;margin-bottom:1rem;">📝</div>
        <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;color:var(--bruin);margin-bottom:.8rem;">
          Nog geen blogposts
        </h3>
        <p style="color:var(--bruin-lt);margin-bottom:2rem;">
          De eerste blogpost komt er binnenkort aan. Hou deze pagina in de gaten!
        </p>
        <a href="{{ '/' | absolute_url }}" class="btn-primary">Terug naar home</a>
      </div>
    {% endif %}

  </div>
</section>


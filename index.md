---
layout: default
title: "Hands4Flow"
description: "Massage, Coaching & Reiki in Emmen – hands4flow"
permalink: /
---

<!-- ── HERO ── -->
<section class="hero">
  <div class="hero-text">
    <span class="hero-eyebrow fade-up">Massage · Coaching · Reiki — Emmen</span>
    <h1 class="fade-up delay-1">
      Voel je weer <em>licht</em><br>en ontspannen.
    </h1>
    <p class="hero-desc fade-up delay-2">
      Last van stress, vermoeidheid, nek- en schouderklachten of slaapproblemen? Of gewoon behoefte aan een moment voor jezelf?
      Bij hands4flow in Emmen help ik je om spanning los te laten en je energie te herstellen.
    </p>
    <div class="fade-up delay-3">
      <a href="{{ '/contact/' | absolute_url }}" class="btn-primary">Afspraak maken</a>
      <a href="{{ '/behandelingen/' | absolute_url }}" class="btn-secondary">Behandelingen bekijken</a>
    </div>
  </div>
  <div class="hero-image fade-up delay-2">
    {% if site.data.homepage.hero.afbeelding %}
    <img src="{{ site.data.homepage.hero.afbeelding }}" alt="Voetreflexmassage bij hands4flow" />
    {% else %}
    <img src="https://primary.jwwb.nl/pexels/52/5240642.jpeg?enable-io=true&enable=upscale&crop=1.4286%3A1&width=900" alt="Voetreflexmassage bij hands4flow" />
    {% endif %}
    <div class="hero-badge">
      <div class="hero-badge-icon">🌿</div>
      <div class="hero-badge-text">
        <strong>Persoonlijke aanpak</strong>
        Afgestemd op jouw wensen
      </div>
    </div>
  </div>
</section>

<!-- ── OVER MIJ (kort, vertrouwen wekken) ── -->
<section style="background:var(--creme);">
  <div class="about">
    <div class="about-img-wrap">
      <img class="about-img"
           src="{% if site.data['over-mij'].inhoud.foto %}{{ site.data['over-mij'].inhoud.foto }}{% else %}https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/1000019670-high.jpg?enable-io=true&enable=upscale&width=700{% endif %}"
           alt="Elsemarie van der Ploeg – hands4flow Emmen" />
      <span class="about-tag">Reiki Master ✦ Coach</span>
    </div>
    <div>
      <span class="section-label">Over mij</span>
      <h2 class="section-title">Hallo, ik ben<br>Elsemarie</h2>
      <p class="section-sub">
        Ik ben Elsemarie van der Ploeg en ben blij dat je mijn praktijk voor massage, coaching en Reiki
        in Emmen gevonden hebt. Naast mijn werk in de gezondheidszorg werk ik met veel liefde in mijn
        praktijk. Ik neem de tijd voor jou — met aandacht, zachtheid en vertrouwen.
      </p>
      <a href="{{ '/over-mij/' | absolute_url }}" class="btn-secondary" style="margin-top:1rem;display:inline-block;">Meer over Elsemarie →</a>
    </div>
  </div>
</section>

<!-- ── REVIEWS ── -->
<section style="background:var(--oker-xlt);">
  <div style="max-width:1100px;margin:0 auto;text-align:center;">
    <span class="section-label">Wat klanten zeggen</span>
    <h2 class="section-title" style="margin-bottom:.5rem;">Ervaringen bij hands4flow</h2>
    <p class="section-sub" style="margin-bottom:0;">"Zet jezelf eens op je prioriteitenlijstje."</p>

    <div class="reviews-grid">
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Ongelofelijk hoe ontspannen ik daar iedere keer weer wegkom. Ze heeft veel vastzittende spanning, stress en emoties in beweging gekregen."</p>
        <span class="review-author">— Jeroen, vaste klant voetreflexmassage</span>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Ik kwam met vermoeidheidsklachten. Het drukke leven overweldigt me soms. Elsemarie geeft me precies wat ik nodig heb om weer in contact te komen met mijn lichaam."</p>
        <span class="review-author">— Marije</span>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Zachte geuren, een warme sfeer en een rust die meteen over me heen viel — en toen moest de massage nog beginnen."</p>
        <span class="review-author">— Jamila, Local Guide</span>
      </div>
      <div class="review-card">
        <div class="review-stars">★★★★★</div>
        <p class="review-text">"Wegens hevige nek- en hoofdpijn een afspraak gemaakt. Aan het eind van de dag had ik geen pijn meer en kon ik ontspannen op vakantie."</p>
        <span class="review-author">— Leonora</span>
      </div>
    </div>

    <div style="margin-top:2rem;">
      <a href="https://www.google.com/search?q=Massagepraktijk+hands4flow+Reviews"
         target="_blank" rel="noopener" class="btn-secondary">
        ⭐ Lees alle reviews op Google
      </a>
    </div>
  </div>
</section>

<!-- ── BEHANDELINGEN ── -->
<section class="treatments" id="behandelingen">
  <div class="treatments-header">
    <div>
      <span class="section-label">Wat ik aanbied</span>
      <h2 class="section-title">Behandelingen<br>voor jouw welzijn</h2>
    </div>
    <p class="section-sub">
      Hands4flow biedt een unieke combinatie van behandelingen voor mensen die altijd maar doorgaan
      en weinig tijd nemen voor ontspanning.
    </p>
  </div>

  <div class="klachten-grid" style="max-width:1100px;margin:0 auto 3rem;">
    <div class="klacht-item">😮‍💨 Stress &amp; overprikkeling</div>
    <div class="klacht-item">😴 Vermoeidheid &amp; slaapproblemen</div>
    <div class="klacht-item">🫀 Nek-, schouder- &amp; rugklachten</div>
    <div class="klacht-item">🧠 Vol hoofd, niet kunnen loslaten</div>
    <div class="klacht-item">⚡ Energieverlies &amp; disbalans</div>
    <div class="klacht-item">🌿 Behoefte aan een moment voor jezelf</div>
  </div>

  <div class="treatments-grid">

    <div class="card">
      <img class="card-img"
           src="https://primary.jwwb.nl/pexels/52/5240642.jpeg?enable-io=true&enable=upscale&crop=1.4286%3A1&width=700"
           alt="Voetreflexmassage" />
      <div class="card-body">
        <div class="card-title">Voetreflexmassage</div>
        <p class="card-desc">Bij een voetreflexmassage wordt druk uitgeoefend op de voet, waarop het hele lichaam terug te vinden is. Stimuleert het zelfherstellend vermogen, verbetert de doorbloeding en vermindert stress.</p>
        <a href="{{ '/behandelingen/voetreflexmassage/' | absolute_url }}" class="card-link">Lees meer</a>
      </div>
    </div>

    <div class="card">
      <img class="card-img"
           src="https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/img_20250103_231438-high.jpg?enable-io=true&enable=upscale&crop=1.4286%3A1%2Coffset-y69&width=700"
           alt="Reiki behandeling" />
      <div class="card-body">
        <div class="card-title">Reiki</div>
        <p class="card-desc">Als Reiki Master ben ik een doorgeefluik van de universele levensenergie. Via handoplegging heft de behandeling blokkades op en versterkt het zelfherstellend vermogen.</p>
        <a href="{{ '/behandelingen/reiki/' | absolute_url }}" class="card-link">Lees meer</a>
      </div>
    </div>

    <div class="card card-highlight">
      <img class="card-img"
           src="https://primary.jwwb.nl/pexels/38/3865496.jpeg?enable-io=true&enable=upscale&crop=1.388%3A1%2Coffset-y40&width=700"
           alt="Acces Bars behandeling" />
      <div class="card-body">
        <div class="card-title">Acces Bars</div>
        <p class="card-desc">32 energetische punten op je hoofd worden zacht aangeraakt. Je laat beperkende patronen los, slaapt beter en ervaart meer rust en helderheid — alsof je lichaam een reset krijgt.</p>
        <a href="{{ '/behandelingen/acces-bars/' | absolute_url }}" class="card-link">Ontdek Acces Bars</a>
      </div>
    </div>

    <div class="card">
      <img class="card-img"
           src="https://primary.jwwb.nl/public/z/f/p/temp-umaagwfutijsnqmyiokx/file_00000000476061f78aa2a0ee9f74f998-high.png?enable-io=true&enable=upscale&crop=1.4286%3A1&width=700"
           alt="Stoelmassage" />
      <div class="card-body">
        <div class="card-title">Stoelmassage</div>
        <p class="card-desc">Even snel ontspannen? Een stoelmassage geeft directe verlichting bij spanning in rug, nek en schouders. Over de kleding, laagdrempelig en direct effectief.</p>
        <a href="{{ '/behandelingen/stoelmassage/' | absolute_url }}" class="card-link">Lees meer</a>
      </div>
    </div>

    <div class="card">
      <img class="card-img"
           src="https://primary.jwwb.nl/pexels/16/1645226.jpeg?enable-io=true&enable=upscale&crop=1.4286%3A1&width=700"
           alt="Coaching" />
      <div class="card-body">
        <div class="card-title">Coaching</div>
        <p class="card-desc">Via gesprekken, ademsessies en body drum release worden blokkades opgeruimd. Kom dichter bij jezelf en leer weer vertrouwen en rust te ervaren.</p>
        <a href="{{ '/coaching/happy-soul-sessies/' | absolute_url }}" class="card-link">Lees meer</a>
      </div>
    </div>

  </div>
</section>

<!-- ── TARIEVEN CTA ── -->
<section style="background:var(--creme-mid);text-align:center;">
  <div style="max-width:600px;margin:0 auto;">
    <span class="section-label">Tarieven</span>
    <h2 class="section-title">Wat kost een behandeling?</h2>
    <p class="section-sub">Behandelingen vanaf € 30,00. Combinaties en strippenkaarten zijn mogelijk.</p>
    <a href="{{ '/tarieven/' | absolute_url }}" class="btn-primary">Bekijk alle tarieven</a>
  </div>
</section>

<!-- ── BLOG ── -->
{% if site.posts.size > 0 %}
<section style="background:var(--white);">
  <div style="max-width:1100px;margin:0 auto;">
    <div style="display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:2.5rem;flex-wrap:wrap;gap:1rem;">
      <div>
        <span class="section-label">Inspiratie & inzicht</span>
        <h2 class="section-title">Van mijn hart<br>naar jou</h2>
      </div>
      <a href="{{ '/blog/' | absolute_url }}" class="btn-secondary">Alle blogposts →</a>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:2rem;">
      {% for post in site.posts limit:3 %}
      <article style="background:var(--creme-mid);border-radius:20px;overflow:hidden;transition:transform .3s,box-shadow .3s;"
               onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 10px 36px rgba(154,125,0,.12)'"
               onmouseout="this.style.transform='';this.style.boxShadow=''">
        {% if post.afbeelding %}
        <img src="{{ post.afbeelding }}" alt="{{ post.title }}"
             style="width:100%;height:200px;object-fit:cover;" />
        {% endif %}
        <div style="padding:1.5rem;">
          <div style="font-size:.8rem;color:var(--bruin-mid);margin-bottom:.5rem;">
            {{ post.date | date: "%d %B %Y" }}
          </div>
          <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;font-weight:400;color:var(--bruin);margin-bottom:.6rem;">
            <a href="{{ post.url | relative_url }}" style="text-decoration:none;color:inherit;">
              {{ post.title }}
            </a>
          </h3>
          <p style="font-size:.9rem;font-weight:300;color:var(--bruin-lt);line-height:1.7;margin-bottom:1rem;">
            {{ post.excerpt | strip_html | truncatewords: 20 }}
          </p>
          <a href="{{ post.url | relative_url }}" class="card-link">Lees meer</a>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}

<!-- ── CONTACT ── -->
<section class="contact" id="contact">
  <span class="section-label">Contact</span>
  <h2 class="section-title">Klaar voor ontspanning?</h2>
  <p class="section-sub">Bel, app of mail — ik help je graag verder.</p>
  <div class="contact-options">
    <a href="https://api.whatsapp.com/send?phone=31659111456"
       class="contact-btn contact-btn-whatsapp">💬 WhatsApp mij</a>
    <a href="{{ '/contact/' | absolute_url }}"
       class="contact-btn contact-btn-mail">✉ Neem contact op</a>
  </div>
  <div class="contact-info">
    <span><strong>Locatie</strong>Emmen, Nederland</span>
    <span><strong>Telefoon</strong>06 59 11 14 56</span>
    <span><strong>KVK</strong>97209341</span>
  </div>
</section>

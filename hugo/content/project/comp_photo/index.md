---
title: Computational Photography Final Project
summary: Non-Photorealistic Rendering of Impressionist Paintings.
tags:
- class
date: '2018-12-08T00:00:00Z'
external_link: ''
links: null
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
slides: example
author_card_html: '<div class="media author-card" itemscope="" itemtype="http://schema.org/Person">

  <img alt="Avatar" class="portrait mr-3" itemprop="image" src="/authors/admin/avatar_hu4388b2781ee3b68acf12416bb9cd4a76_57148_250x250_fill_q90_lanczos_center.jpg"/>

  <div class="media-body">

  <h5 class="card-title" itemprop="name"><a href="https://connorzl.github.io/">Connor
  Lin</a></h5>

  <h6 class="card-subtitle">PhD Candidate</h6>

  <p class="card-text" itemprop="description">My interests primarily lie at the intersection
  between computer graphics, geometry processing, and machine learning!</p>

  <ul aria-hidden="true" class="network-icon">

  <li>

  <a href="https://github.com/connorzl" itemprop="sameAs" rel="noopener" target="_blank">

  <i class="fab fa-github"></i>

  </a>

  </li>

  <li>

  <a href="https://twitter.com/connorzl" itemprop="sameAs" rel="noopener" target="_blank">

  <i class="fab fa-twitter"></i>

  </a>

  </li>

  <li>

  <a href="https://linkedin.com/in/connorzl" itemprop="sameAs" rel="noopener" target="_blank">

  <i class="fab fa-linkedin"></i>

  </a>

  </li>

  <li>

  <a href="/files/cv.pdf" itemprop="sameAs">

  <i class="ai ai-cv"></i>

  </a>

  </li>

  </ul>

  </div>

  </div>'
---


Most of the pipeline here is inspired by Image and Video Based Painterly Animation [HE 04]. We also experimented with tools from GradientShop [BZCC 10], such as the long-edge detector to compute better paint stroke orientations.

Each painting is composed of multiple layers, increasing in level of detail:
![](/img/compphoto1.png)
![](/img/compphoto2.png)

A couple more fun examples:
![](/img/compphoto3.png)
![](/img/compphoto4.png)
![](/img/compphoto5.png)

---
title: Quad Meshing Pipeline
summary: Master's Thesis, advised by Keenan Crane.
tags:
- research
date: '2019-07-19T00:00:00Z'
external_link: ''
image:
  caption: Wax figure of Taylor Swift from Madame Tussaud
  focal_point: Smart
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


This pipeline  describes a method for computing near-conformal integer grid maps with very low area distortion; such maps can be used to directly extract a high-quality quad mesh. Unlike previous methods, this formulation involves no mixed integer problems or other forms of combinatorial optimization. Instead, it entails two easy problems (a convex program and a linear system with Dirichlet boundary conditions) that can be solved efficiently and optimally. The basic idea is to replace the difficult texture rectification step from discrete conformal mapping, which is formulated in the parameter domain, with a purely intrinsic variational procedure inspired by methods for periodic global parameterization. We apply this algorithm to generate quad meshes for all models in a representative database, achieving high quality results at significantly lower computational cost. We also show how this formulation provides a unified perspective on a long history of problems in field-guided parameterization and global conformal parameterization.

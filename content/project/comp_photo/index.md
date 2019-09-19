---
title: Computational Photography Final Project
summary: Non-Photorealistic Rendering of Impressionist Paintings.
tags:
- class
date: "2018-12-08T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

links:
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example
---

Most of the pipeline here is inspired by Image and Video Based Painterly Animation [HE 04]. We also experimented with tools from GradientShop [BZCC 10], such as the long-edge detector to compute better paint stroke orientations.

Each painting is composed of multiple layers, increasing in level of detail:
![](/img/compphoto1.png)
![](/img/compphoto2.png)

A couple more fun examples:
![](/img/compphoto3.png)
![](/img/compphoto4.png)
![](/img/compphoto5.png)


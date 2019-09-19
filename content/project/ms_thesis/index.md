---
title: Quad Meshing Pipeline
summary: Master's Thesis, advised by Keenan Crane.
tags:
- research
date: "2019-07-19T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Wax figure of Taylor Swift from Madame Tussaud
  focal_point: Smart

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

**[TODO] make this understandable for a general audience**

This paper describes a method for computing near-conformal integer grid maps with very low area distortion; such maps can be used to directly extract a high-quality quad mesh. Unlike previous methods, this formulation involves no mixed integer problems or other forms of combinatorial optimization. Instead, it entails two easy problems (a convex program and a linear system with Dirichlet boundary conditions) that can be solved efficiently and optimally. The basic idea is to replace the difficult texture rectification step from discrete conformal mapping, which is formulated in the parameter domain, with a purely intrinsic variational procedure inspired by methods for periodic global parameterization. We apply this algorithm to generate quad meshes for all models in a representative database, achieving high quality results at significantly lower computational cost. We also show how this formulation provides a unified perspective on a long history of problems in field-guided parameterization and global conformal parameterization.

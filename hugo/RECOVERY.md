# Recovery provenance

This is reconstructed source, not a claim to have recovered the exact lost
original files. The published site at commit `f37b754` is the content reference,
with the subsequently supplied `F26_Resume.pdf` as the current CV.

The older `connorzl/academic-kickstart` source at commit `e1a15b0` supplied the
configuration structure, project Markdown, and Academic theme. Academic is
vendored from commit `5b4d11825e7c5ff3eb3125d049a34107e512d2ed`.
Only site content, configuration, theme code, and assets were imported.

Recovered material:

- The current homepage biography, role, affiliations, interests, education,
  social links, and experience cards came from the published `index.html`.
- All six publications' titles, authors, dates, summaries, and paper links came
  from the published `index.json`, with display conventions checked against
  the HTML. Publication author rendering preserves equal-contribution stars.
- The missing thesis post's body, embedded video, title, summary, and featured
  image came from `post/ms/index.html` and its published media.
- Historical project/post author cards retain the profiles originally shown on
  those pages through per-page `author_card_html` overrides. Updating the current
  profile therefore does not rewrite those archived cards.
- Published media, including historical resized images, remain available at
  their original URLs. The custom domain is preserved through `static/CNAME`.

The source generates the page markup, publication lists, taxonomy pages,
search index, sitemap, feeds, and pagination redirects. Local template overrides
restore the published compact paper list, unlinked paper headings/authors,
empty footer, search scope, and profile/404 listing behavior.

To preserve the frontend exactly, `layouts/_default/baseof.html` selects the
published `academic.min.dece3379ebc8d86dbd68264c588243d3.css` and
`academic.min.b2cc8bd29fb9c81d4b9e12ae64e0496f.js` bundles from `static/`.
The original theme's editable SCSS and JavaScript remain vendored. To make a
future design change through them, remove the two bundle-path substitutions
in that override and verify the generated styles/scripts before deployment.

The source uses Hugo 0.55.6 extended and BlackFriday. Upgrading to current Hugo
requires a separate theme/Markdown migration. Historical pages now share the
current navigation and frontend assets; their primary visible content is
preserved. Generated whitespace, metadata formatting, and asset fingerprints
can differ from the original outputs.

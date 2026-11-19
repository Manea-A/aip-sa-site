# aip-sa.com – AIP company website

> **Keep this repository public.** It serves https://aip-sa.com through GitHub Pages. On a free
> GitHub plan, Pages works only for public repositories: making this one private takes the
> website offline. That happened from 2026-11-14 to 2026-11-16 ("There isn't a GitHub Pages site
> here"). Every push to `main` republishes `public/` (workflow `.github/workflows/pages.yml`).

Plain HTML and CSS, no framework, no tracker. The company is called only **AIP**, in both languages.

```
public/          <- the website (deploy this folder only)
  index.html       Home in Arabic (the 2026-11-19 design)        built by tools/build_home.py
  en/index.html    Home in English                               built by tools/build_home.py
  pricing.html     Pricing (older page): Nawa, Fath, Nedaa, bundles, terms
  404.html
  assets/css/home.css   the home page's styles; style.css is the pricing and 404 pages'
  assets/img/           aip-wordmark.svg, nedaa-mark.svg, logo-mark.svg (favicon)
tools/build_home.py   <- the home page's Arabic and English text; edit it, run it, commit both pages
design/               <- the owner's design file of 2026-11-19 (packed design-tool export, not deployed)
recovered/            <- what was recovered from web.archive.org (reference only, not deployed)
```

Arabic (RTL) is at `/`, English at `/en/`; the language button links between them, and the old `?lang=en`
address opens `/en/`.

**The home page (2026-11-19).** Built from the owner's design, as static HTML. Left out on purpose, because
they looked generated or claimed what nobody can check: a "live status" panel ("Data centers: online", "AI:
learning"), a server-rack readout ("ALL SYSTEMS NOMINAL"), a row of results percentages with no source
("40–70% lower costs" and so on), "up to 99% accuracy" for Waseel, a scrolling word ticker, glow effects
and map coordinates in the footer. Arabic body text is formal Arabic. Contact details follow the new
design (WhatsApp +966 55 633 0039, Al Sitteen Tower); the pricing page still shows +966 58 196 2775.

## Preview locally

```
cd public
python -m http.server 8000      # then open http://localhost:8000
```

## Deploy

Upload **the contents of `public/`** to any static host, for example GitHub Pages (Pages workflow publishing `public/`), Cloudflare Pages (output dir `public`), Hostinger `public_html`, or a static server on Railway.
Making aip-sa.com serve this site requires **replacing** the apex `A 2.57.91.91` record, which is Hostinger's parking page. Do not touch the MX, SPF, DKIM, DMARC, autoconfig or autodiscover records, or any `nedaa.*`, `*.nidaa`, `app` or `send/rsend` records.

## For the owner to review (items 2 to 11 are about the pricing page and the old home page)

1. **Logo:** the home page and the pricing and 404 pages use the AIP wordmark from the 2026-11-19 design (`assets/img/aip-wordmark.svg`); the older "Artificial Intelligence Place" image was removed (the company is only "AIP").
2. **Look:** the original CSS and JS were not archived either. The layout, colours (#57a1c1) and behaviour were recreated from the page structure.
3. **Product logos** for Nawa, Fath and Nedaa on the pricing page were not archived, so icons stand in for them.
4. **"Download Profile" buttons:** the profile PDFs were never linked or archived (`href="#"`). The buttons now go to the contact form. Send the PDFs and they can be linked.
5. **"Learn more" buttons on Services:** these had no target in the original. They now go to the contact form.
6. **Client and partner logos:** 7 partner logos were recovered from the older 2024 site. The other partners (Sebl, Facilities Security Forces, OPAL) and all six clients appear as names, which is what the original showed whenever a logo failed to load. Please confirm that these organisations are still OK to list.
7. **Contact forms** open the visitor's email app, addressed to **info@aip-sa.com**, because a static site has no form backend. Make sure that mailbox exists, or add a form service.
8. **Pricing "Call us" button:** the original pointed to the placeholder `+966500000000`. It now uses the site's own number, +966 58 196 2775.
9. **Inconsistent or outdated content, left as it was:**
   - Fath is "90+ agents" on the home page and "105 agents" on the pricing page.
   - The product is spelled "Nidaa" (home, English) and "Nedaa" (pricing).
   - The news dates say January 2025, but the linked LinkedIn posts are from October 2025.
   - The footer says © 2025.
   - Many pricing-page items had no English text in the original, so they stay Arabic in English mode.
   - Prices, discounts, payment terms and the "3-month warranty" are from Feb 2026.
   - The Twitter link uses twitter.com.
10. **Nedaa link:** "Visit Nedaa", pointing to https://nedaa.aip-sa.com, was added to the Nedaa product card (home) and the Nedaa pricing section.
11. The older 2024–25 WordPress pages (Go Digital, Industrial, SAP solutions, "Graf for Real-Estate", about, contact) were replaced by the 2026 site. Their text is kept in `recovered/` in case anything should come back.

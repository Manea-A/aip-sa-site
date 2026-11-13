# aip-sa.com – AIP (AI Place) company website

Static rebuild of the old **saudiaip.com** site. It is based on the Wayback Machine capture from 12 Feb 2026 and now uses the domain **aip-sa.com**.
It is plain HTML, CSS and a small amount of JavaScript. There is no build step, no tracker and no third-party request. Font Awesome is stored inside the site.

```
public/        <- the website (deploy this folder only)
  index.html     Home: hero, about, products, services, solutions, clients/partners, news, contact
  pricing.html   Pricing: Nawa, Fath (105 agents), Nedaa, bundles, terms
  404.html
  assets/        css, js, img (logos recovered from the archive), vendor/fontawesome (6.5.1 Free)
recovered/     <- what was recovered from web.archive.org (reference only, not deployed)
```

Arabic (RTL) is the default. The EN/عربي button switches the page to English (LTR) and remembers the choice. `?lang=en` also opens it in English.

## Preview locally

```
cd public
python -m http.server 8000      # then open http://localhost:8000
```

## Deploy

Upload **the contents of `public/`** to any static host, for example GitHub Pages (Pages workflow publishing `public/`), Cloudflare Pages (output dir `public`), Hostinger `public_html`, or a static server on Railway.
Making aip-sa.com serve this site requires **replacing** the apex `A 2.57.91.91` record, which is Hostinger's parking page. Do not touch the MX, SPF, DKIM, DMARC, autoconfig or autodiscover records, or any `nedaa.*`, `*.nidaa`, `app` or `send/rsend` records.

## For the owner to review

1. **Logo:** the 2026 logo file (`AIP_LOGO.png`) was never archived. The site uses the older AIP mark and the white "Artificial Intelligence Place" wordmark from the 2024 site. Replace `assets/img/logo-mark.svg` and `logo-white.png` if they are out of date.
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

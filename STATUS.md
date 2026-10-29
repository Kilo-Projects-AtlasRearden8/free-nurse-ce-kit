# STATUS — Free Nurse CE Kit

## What was built

A free, fillable, printable, large-print friendly continuing-education kit for registered nurses, published by Asdale Dynamics, LLC (education only — not medical advice). No account, no login, no internet needed after download.

Files:
- `README.md` — kit overview, contents, how to use, large-print notes, education-only disclaimer, MIT license, credit to Asdale Dynamics, LLC, link to dylanasdale.github.io
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `assets/style.css` — canonical shared print styles: 16 pt+ body, high contrast, generous ruled writing space, `@media print` clean output
- `ce-tracker.html` / `ce-tracker.md` — CE tracker: nurse/license details, progress summary with auto totals, 20-row fillable course log table, sign-off friendly
- `license-renewal-calendar.html` / `license-renewal-calendar.md` — 12-month renewal planner with per-month checklists, renewal submission checklist, fillable license-details card
- `course-log.html` / `course-log.md` — per-course detail log (provider, instructor, date, hours, category, cost, certificate #, URL, application notes) with auto cost/hour totals, 15 rows
- `reflection-templates.html` / `reflection-templates.md` — three templates: per-course reflection, quarterly CE reflection, annual/renewal-cycle reflection; print one per course
- `tests/validate.py` — validation script (HTML structure, fillable controls, LICENSE/README text, secret scan, no `.github/workflows`)

Every HTML page embeds its CSS, so each is a standalone printable file. Large-print friendly: 16 pt+ body text, wide ruled rows, big checkboxes, high contrast.

## How to run

1. Open this folder.
2. Open any `.html` file in a browser (Chrome, Edge, Safari, Firefox).
3. Fill in fields on screen, or print blank and write by hand.
4. Use the browser print dialog; print styles hide controls and output clean black-and-white worksheets.
5. Markdown files are the editable source copies of each worksheet.

Validation: `python3 tests/validate.py`

## Verification results

- `python3 tests/validate.py` — PASSED: all four HTML files parse cleanly (doctype, no unclosed tags, all form controls fillable with `class="fill"`, print styles present); `LICENSE` contains the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`; `README.md` credits Asdale Dynamics, LLC and includes the MIT license reference; no `.github/workflows` directory; no secrets, API keys, passwords, or private keys found in any file.
- HTML pages are self-contained (embedded CSS) and open without a build step or server.

## Known gaps

- No automated browser/print rendering test (no headless browser available); print output verified by CSS inspection only, not by actual print rendering.
- Auto-total JavaScript in `ce-tracker.html` and `course-log.html` works on screen but totals are blank on printout until filled in (intended).
- Calendar months are generic (not tied to a specific year); user writes in the year.
- Not a compliance tool: CE categories, renewal deadlines, and fees vary by state board; users must confirm with their board of nursing.

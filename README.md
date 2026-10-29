# Free Nurse CE Kit

> **Free, fillable, printable continuing-education helpers for registered nurses.**  
> No account, no login, no internet required after download. Education only — not medical advice.

Published by **Asdale Dynamics, LLC** (Indiana, formed October 2026). Dylan Asdale is a registered nurse turned AI author and founder of Asdale Dynamics, LLC. His book *The Massive AI Manual* and hub site [dylanasdale.github.io](https://dylanasdale.github.io) explain AI "like a friend would": plain English, step by step, never condescending.

---

## What's Inside

| File | Purpose | Key Features |
|------|---------|--------------|
| [`ce-tracker.html`](ce-tracker.html) / [`ce-tracker.md`](ce-tracker.md) | Track CE hours by category toward renewal | 20-row fillable log, auto-totaling progress summary (Category A / B / Other), nurse & license details card |
| [`license-renewal-calendar.html`](license-renewal-calendar.html) / [`license-renewal-calendar.md`](license-renewal-calendar.md) | 12-month renewal planner | Per-month checklists, renewal submission checklist, fillable license-details card (expiry, grace period, fees) |
| [`course-log.html`](course-log.html) / [`course-log.md`](course-log.md) | Per-course detail log | 15-row log with provider, instructor, date, hours, category, cost, certificate #, URL, application notes; auto cost/hour totals |
| [`reflection-templates.html`](reflection-templates.html) / [`reflection-templates.md`](reflection-templates.md) | Guided reflection prompts | 3 templates: per-course, quarterly, annual/renewal-cycle; print one per course |

Every page is a **single self-contained HTML file** with embedded CSS. Open in any browser, fill on screen, and print. No build step, no server, no dependencies.

---

## Quick Start

1. **Download** this folder (clone or download ZIP).
2. **Open** any `.html` file in your browser (Chrome, Edge, Safari, Firefox).
3. **Fill** in the fields on screen, or print blank and write by hand.
4. **Print** using your browser's print dialog — print styles strip headers/controls for clean black-and-white worksheets.
5. **File** the completed sheets with your licensure records.

> ⚠️ **Verify all CE requirements with your state board of nursing.** Requirements vary by state; these templates are not a compliance guarantee.

---

## Large-Print Friendly Design

All pages are designed for readability and handwriting:

- **Base font 16 px+** (18 px for writing areas)
- **High contrast** black-on-white with strong borders
- **Generous line height** (1.6) and wide ruled rows (64–70 px height)
- **Large checkboxes** (26 × 26 px) and form controls (17 px text)
- **Print styles** (`@media print`) remove backgrounds, hide on-screen controls, force black borders/text, prevent table rows from splitting across pages

---

## How Each Template Works

### CE Tracker (`ce-tracker.html`)
- **Header card:** Name, license #, state, expiry, reporting period, required hours
- **Progress summary:** Auto-calculates total hours + Category A / B / Other subtotals as you type
- **20-row log:** Date, Course/Activity, Provider, Category, Hours, Cost, Certificate filed (Y/N), Notes
- **Tip:** Category values "A" or "B" (case-insensitive) feed the summary boxes

### License Renewal Calendar (`license-renewal-calendar.html`)
- **Header card:** License expiry, renewal due date, grace period end, CE hours due, renewal fee
- **12 monthly cards:** Each has a focus field + 4 standard checklist items (CE progress, certificates, applications, etc.)
- **Renewal submission checklist:** 7-step final verification before submitting to your board

### Course Log (`course-log.html`)
- **Header card:** Name, license #, state, reporting period, total hours needed, page numbering
- **15-row detail log:** Title, Provider, Instructor, Date, Hours, Category, Cost, Certificate #, URL/Access, Application notes
- **Cost summary:** Auto-totals hours and dollars as you type

### Reflection Templates (`reflection-templates.html`)
- **Template 1 — Per-course:** What did I learn? What will I change? Remaining questions? Recommendation?
- **Template 2 — Quarterly:** Most useful course, applied learning, to-learn list, on-track check, next quarter plan
- **Template 3 — Annual/Renewal:** Most valuable learning, practice impact, best providers/formats, changes for next cycle, notes for next renewal

---

## Accessibility & Usability

- **Labels on all inputs** (header cards use `<label>`; table rows use descriptive column headers)
- **Keyboard navigable** — tab through all fields, `Enter`/`Space` for checkboxes
- **Focus indicators** — 3 px blue outline on focused fields
- **Print-only cleanup** — `.no-print` class hides instructional text and controls when printing
- **Semantic HTML** — proper heading hierarchy, `<table>` with `<thead>`/`<tbody>`, `<ul>` for checklists

---

## Education Only Disclaimer

> **These templates are for continuing-education recordkeeping only.**  
> They do not constitute medical advice, nursing advice, or licensure guidance.  
> CE hour categories, renewal deadlines, grace periods, and documentation rules vary by state.  
> **Always confirm requirements with your state board of nursing and employer.**

---

## License

**MIT License** — see [`LICENSE`](LICENSE).

```
Copyright (c) 2026 Asdale Dynamics, LLC
```

---

## About Asdale Dynamics, LLC

Asdale Dynamics, LLC is an Indiana LLC founded by Dylan Asdale, registered nurse and AI author. The LLC publishes:

- Beginner-friendly AI education, books & guides (*The Massive AI Manual*)
- Practical open-source tools (prompt tools, local-LLM utilities, MCP servers, agent skills)
- Small-business & author tools (KDP/book publishing, marketing, reselling, bookkeeping)
- Accessible life-admin helpers (paperwork organizers, budgeting, low-energy/ADHD-friendly productivity)
- Healthcare-worker AI aids (education only, never medical advice)
- Fun extras: FFXIV and chess tools

🔗 **Learn more:** https://dylanasdale.github.io

---

## File Structure

```
free-nurse-ce-kit/
├── LICENSE
├── README.md
├── STATUS.md
├── assets/
│   └── style.css          # Canonical shared print styles
├── ce-tracker.html
├── ce-tracker.md
├── license-renewal-calendar.html
├── license-renewal-calendar.md
├── course-log.html
├── course-log.md
├── reflection-templates.html
├── reflection-templates.md
└── tests/
    └── validate.py        # Validation script (HTML structure, fillable controls, secrets scan)
```

---

## Validation

Run the included test suite:

```bash
python3 tests/validate.py
```

Checks performed:
- ✅ All HTML files parse cleanly (doctype, no unclosed tags)
- ✅ All form controls are fillable (`class="fill"`)
- ✅ Print styles (`@media print`) present in each HTML file
- ✅ Required markers present ("Asdale Dynamics, LLC", "Education only", etc.)
- ✅ `LICENSE` contains exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`
- ✅ `README.md` credits Asdale Dynamics, LLC and references MIT License
- ✅ No `.github/workflows` directory
- ✅ No secrets, API keys, passwords, or private keys in any file

---

## Contributing

This is a free, open educational resource. Feel free to fork, adapt, and share — attribution appreciated.

---

*Made with care by Asdale Dynamics, LLC • Education only • Not medical advice*
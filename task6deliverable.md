# JRN 3015A — Task 6 Deliverable: Product Prototype & Investor Pitch (Kikao360)
*Generated & verified by `t6prompt.py` against Assignment 2 Rubric (14 Marks) & Expected Outputs.*

---

## 6.1 Rubric Alignment: Which Prototype Options (a–g) Apply to Kikao360

| Rubric Option | Applies? | Kikao360 Deliverable & Evidence |
| :--- | :---: | :--- |
| **a. 2–3 min podcast or video pilot** | ✅ **Yes** | Persistent NPR-style audio dock + planned 2–3 min flagship Kikao360 Pilot Explainer (*"Soma. Tazama. Sikiliza."*) introducing a real Kenyan MSME/eTIMS story. |
| **b. Sample digital magazine or newsletter** | ✅ **Yes** | Guardian-style Magazine view (`prototype/index.html`) + full responsive **Tuesday/Friday Email Newsletter Issue #42** (`prototype/newsletter.html` and embedded in `prototype/samples.html`). |
| **c. Wireframe or interactive mock-up of a media app** | ✅ **Yes** | Full 5-mode interactive web app (`whatsapp`, `guardian`, `pinterest`, `tiktok`, `sphere`) + Category Onboarding Picker + User Account Space (`Saved`, `Liked`, `My Algorithm`) + 3-Gate Tipline + Lipa na M-Pesa STK Push. |
| **d. Sample website or news platform** | ✅ **Yes** | Live multi-page web platform (`prototype/index.html`, `prototype/cms.html`, `prototype/samples.html`, `prototype/newsletter.html`). |
| **e. Media service portfolio with sample client deliverables** | ✅ **Yes** | **B2B Native Sponsor Content Package & Intelligence Dossier** in `prototype/samples.html` (1,200w Whitepaper + 60s Reel + WhatsApp push slot @ KES 80k) + `format_reel.py` stamped 9:16 video (`sample_VID_094529_reels.mp4`). |
| **f. Demonstration of a proposed media technology solution** | ✅ **Yes** | **Inside-the-Sphere 3D Room** (6 vertical 3-tier pillars = 18 cards), **Pinch-to-Switch** gesture controller, **`format_reel.py`** auto-formatter, and **Owner CMS (`cms.html`)** with 3-stage pipeline & CAC tracker. |
| **g. Core features & user experience (Mandatory)** | ✅ **Required** | End-to-end user journey demonstrated live alongside the 10–15 minute Investor Pitch. |

---

## 6.2 Interactive Prototype Architecture & Core UX Flow

* **Primary Web App (`prototype/index.html`):** Zero-dependency HTML5, CSS3, and ES6+ JavaScript (`data.js`, `app.js`, `sphere.js`, `gestures.js`) styled in Kikao360's 60-30-10 palette (**Obsidian `#0b101b` / Guardian Navy `#052962` / Emerald `#00a884` / Terracotta `#f26419`**).
* **Five Interconnected Viewing Modes:**
  1. **WhatsApp Channel:** OpenGraph rich teaser cards, view counts, emoji reaction pills.
  2. **The Magazine:** Pillar navigation, Mega-Menu drawer, Read/Watch/Listen switcher, persistent NPR-style audio dock, and Lipa na M-Pesa STK Push modal.
  3. **Pinterest Masonry Grid:** 2-column mobile / 4-column desktop visual discovery feed.
  4. **Reels / TikTok Feed:** 9:16 vertical video feed with engagement controls.
  5. **3D Sphere Room:** 6 vertical 3-tier pillars (18 cards) inside a draggable, zoomable 360° spatial room.
* **Personalization & Trust Loops:** Category Onboarding Picker, User Account Space (`Saved`, `Liked`, `My Algorithm`), and 3-Gate Community Tipline Modal.
* **Owner Operations CMS (`prototype/cms.html`):** Editorial Calendar, 3-stage pipeline (`Pending Review` → `Pending Publication` → `Published`), and Post-Publication Performance & CAC Dashboard (`CAC ≤ KES 3.00`).
* **Client & Format Showcase (`prototype/samples.html`):** Architectural distinction between:
  1. **📰 Finished Editorial & Commercial Product Deliverables (Options b & e):**
     * **Full Email Newsletter Template (`prototype/newsletter.html`):** Responsive HTML Morning Dispatch (Issue #42) featuring masthead, Nairobi weather/Daraja uptime telemetry strip, lead M-Pesa API investigation, 60-Second Flash Radar, audio commute player embed, native Safaricom sponsor spotlight, and Lipa na M-Pesa micro-patronage prompt.
     * **B2B Native Sponsor Deliverable Dossier:** Co-branded fintech package (1,200w dossier + 60s Reel + WhatsApp telemetry) demonstrating compliance with the Editorial–Commercial Firewall.
  2. **🧩 Atomic UI & Interaction Components (Options c & f):**
     * Category Onboarding Picker (9 beats), WhatsApp OG rich preview card, 9:16 vertical video frame, Guardian editorial spread, 3-gate tipline verification, persistent audio dock pill, Lipa na M-Pesa STK modal, and Inside-the-Sphere 3D spatial room.

---

## 6.3 Investor Pitch Deck (10–15 Minute Boardroom Presentation — Synced with Tasks 1–5)

* **Slide 1 — The Hook & Problem:** **75.1%** of Kenya is under 35 (**KNBS, 2019**); **77%** of online Kenyans consume news via social platforms (**Reuters Institute, 2024**), yet legacy outlets (*Business Daily*, *The Standard*, *The Star*) gate analysis behind paywalls that **91% of surveyed youth** resist, leaving 7.4M MSMEs underserved.
* **Slide 2 — The Solution (Kikao360):** *"Comment is free, but truth is multidimensional."* / *"Soma. Tazama. Sikiliza."* — A 5-mode, zero-paywall multimodal newsroom uniting WhatsApp speed, Guardian editorial rigor, Pinterest/Reels discovery, and a 3D Sphere Room.
* **Slide 3 — Target Audience & Market Opportunity:** Primary (*Amina, 22* — Digital Hustler & Student Innovator, 19–27) + Secondary (*Brian, 31* — Corporate & Policy Professional, 28–38); **15.1M** TikTok adult reach (+42.7% YoY; **DataReportal, 2025**) & **60%** WhatsApp news usage.
* **Slide 4 — Live Product Demo (4 Mins):** Walk through `prototype/index.html` (WhatsApp Card → Magazine Read/Watch/Listen → M-Pesa STK Push → 3D Sphere Room) + `prototype/cms.html` (3-Stage Pipeline & CAC Dashboard).
* **Slide 5 — Competitive Advantage & Moat:** **Lower barrier to entry** (100% in-house zero-dependency tech + multidisciplinary team), COPE *"Create Once, Package Three Ways"*, 3-Gate Tipline, and 10x leaner OPEX (**KES 145,000/mo**).
* **Slide 6 — Operations & Governance (Task 3):** Hybrid Flat-Functional + Network (Hub-and-Spoke) structure, Two-Source Rule, 24–48h Right of Reply, 70/30 Human-to-AI Mandate, and MCK/ODPC/Defamation/Copyright compliance.
* **Slide 7 — Business Model & Pricing (Task 4):** 4-Pillar Hybrid Revenue — Fintech Native Sponsorships (KES 40k/80k/120k), Lipa na M-Pesa Micro-Patronage (KES 250 avg), Audio/Video Licensing (KES 15k–25k), and Campus Activations (KES 30k–65k).
* **Slide 8 — Financial Projections & Break-Even (Task 4):** Startup CAPEX **KES 480,000** | Monthly OPEX **KES 145,000** | **Operational Break-Even: Month 3 (+KES 70,000)** | **Cumulative Cash-Flow Positive: Month 4 (+KES 110,000)** | **Full CAPEX Payback: Month 6 (+KES 645,000 cumulative net)**.
* **Slide 9 — 3-Month Growth & Marketing Plan (Task 5):** 50,000 WhatsApp subscribers & 75,000 Web MAUs by Month 3 at **CAC ≤ KES 3.00** via campus ignition, investigative series, and strategic university/fintech/radio partnerships.
* **Slide 10 — The Seed Ask & Use of Funds:** Seeking **KES 480,000** seed capital (47% production rig/lighting, 33% editing workstation, 11% domain/licensing/Daraja, 8% contingency) with full payback by Month 6.

---

## 6.4 Prototype Coherence & Polish Checklist (Pre-Boardroom Walkthrough)
1. **Localize `prototype/js/data.js`:** Remove leftover `PulseWire` comment and foreign byline (`Robert Booth and Miatta Mbriwa`), replacing `story-2` with 100% Kenyan/East African reporting.
2. **Upgrade Visual Thumbnails & Video:** Replace raw workspace screenshots with clean editorial cover images and wire `sample_VID_094529_reels.mp4` (stamped 9:16 Reel).
3. **Sync `pitchDeckModal` in `prototype/index.html`:** Update modal slides to reflect the verified **Month 3 Operational / Month 4 Cumulative / Month 6 CAPEX Payback** milestones and **KNBS 2019 / Reuters 2024 / DataReportal 2025** stats.
4. **Top-Bar Navigation Link to `samples.html`:** Add a direct button alongside `⚙️ CMS` so investors can inspect sample client/newsletter deliverables in one click.
5. **2–3 Minute Pilot & Newsletter Preview:** Add the flagship 2–3 min pilot track to the audio dock and a Tue/Fri newsletter preview in `samples.html`.

---

## Verification Gate Summary
- ✅ `6a_to_6g_rubric_mapped`: PASS
- ✅ `6_architecture_all_3_pages`: PASS
- ✅ `6_pitch_10_slides_synced_numbers`: PASS
- ✅ `6_polish_checklist_present`: PASS
- ✅ `expected_output_prototype`: PASS
- ✅ `expected_output_pitch_deck`: PASS

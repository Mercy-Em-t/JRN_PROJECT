# Kikao360 — Editorial Calendar, Writer/Converter Roles & 3-Stage Content Pipelines

This SOP operationalizes the complete newsroom lifecycle from writing and multimodal conversion to editorial meetings, approval gates, and post-publication **Reach, Impressions, and CAC** monitoring.

---

## 1. Content Creation & Conversion Roles (The Newsroom Desk)

| Role | Primary Output | Handoff Target |
| :--- | :--- | :--- |
| **Magazine & Print Writers** *(Core Editor + Campus Correspondents)* | 800–1,200 word investigative articles, news bulletins, and print-ready longform layouts. | **Pending Review Pipeline** |
| **Title, Hook & Caption Specialist** | A/B-tested headlines, 0–3s TikTok/Reels hooks, WhatsApp 2-line teasers, and SEO descriptions. | **Audio/Video Converters & WhatsApp Desk** |
| **Audio Converter / Producer** | Converts approved written bulletins into **3–5 min daily audio dispatches** and **13-min weekly flagship bulletins** (MP3 + transcript). | **Pending Publication Pipeline** |
| **Video Converter / Editor** | Converts written scripts + field footage into **60s 9:16 TikTok & IG Reels** using `format_reel.py` (with safe-zone `KIKAO360` logo stamp). | **Pending Publication Pipeline** |

---

## 2. Group Organization & Editorial Review Meetings

| Meeting | Day & Time (EAT) | Attendees | Agenda & Definition of Done |
| :--- | :--- | :--- | :--- |
| **Pitch & Calendar Sync** | **Monday 08:30 EAT** (30 min) | All 4 Core Founders + Lead Correspondents | Lock the week's 9-beat story slots, assign writers, and flag sponsor conflicts. |
| **Editorial Review & QA Gate** | **Wednesday 14:00 EAT** (30 min) | Managing Editor, Fact-Checkers, Audio/Video Converters | Review items in **Pending Review**; verify Two-Source Rule & Right of Reply; move approved pieces to **Pending Publication**. |
| **Post-Publication & CAC Sync** | **Friday 16:00 EAT** (30 min) | CEO, Commercial Director, CTO, Managing Editor | Audit Reach, Impressions, M-Pesa conversions, and **CAC**; adjust next week's hooks and promo spend. |

---

## 3. The Three Content State Pipelines (Tracked in `prototype/cms.html`)

### Pipeline A: Pending Review (`draft` → `pending_review`)
* **Entry Criteria:** Writer submits article draft, 2+ verified sources, headline/hook options, and beat tag.
* **Action:** Held here until Fact-Check Desk & Managing Editor sign off on accuracy, libel safety, and 70/30 human verification.

### Pipeline B: Pending Publication (`approved` → `pending_publish`)
* **Entry Criteria:** Approved at Editorial Review.
* **Action:** Audio & Video Converters attach the **MP3 bulletin**, **9:16 Reels/TikTok MP4**, and **WhatsApp OpenGraph card**. Story sits in the **Content Planning Calendar** awaiting its scheduled EAT slot (07:30 or 13:00 EAT).

### Pipeline C: Post-Publication Performance & CAC (`published` → `analytics`)
Every published piece is tracked at **24h, 72h, and 7d** intervals across:
* **Reach** *(Unique accounts/readers reached)*
* **Impressions** *(Total views across WhatsApp, Web, TikTok, IG Reels)*
* **Engagement & Conversion** *(Likes, Saves, Shares, M-Pesa STK clicks)*
* **Customer Acquisition Cost (CAC):**
  $$\text{CAC (KES)} = \frac{\text{Channel Marketing \& Promo Spend (KES)}}{\text{New Active Subscribers / Readers Acquired}}$$
  *Baseline Target (Task 4 OPEX):* With **KES 15,000/mo** social promo targeting **5,000+ new monthly readers/subscribers**, target blended **CAC ≤ KES 3.00 per subscriber** (and **≤ KES 300 per M-Pesa micro-donor**).

# Kikao360 Deep Explainer & Study Book
**Grounded in the 31-Step Media Venture Design & Validation Protocol (`media-venture-design-protocol`)**

This guide explains **what** we built for Kikao360, **why** each architectural and management choice was made, and **how** to defend every decision in the **Week 11 Media Investors' Boardroom Simulation**.

---

## Chapter 1: The 31-Step Methodology — Why Every Gate Matters
Your handwritten 31-step protocol ensures you never fall into the #1 student-project trap: *building a pretty prototype without a viable business behind it.*

1. **Industry Transformation (Steps 1–6):** Legacy Kenyan outlets (*Business Daily*, *Nation*) rely on print/paywalls while 84% of 18–35s get news on social/messaging apps. Attention is fragmented, and AI lowers content-creation cost—meaning **trust and verification** become the scarce, valuable asset.
2. **Benchmark & Negative Tests (Step 10):** A feature is only "done" if it passes both positive goals *and* negative tests (e.g., *fail if mobile load > 2s; fail if fixed OPEX exceeds KES 145k before Month 3*).
3. **MoSCoW Narrowing (Step 21c):** Prevents feature bloat. We locked **WhatsApp Cards, Magazine, 60s Reels/TikTok, Category Onboarding, and Tipline QA** as *Must Haves*, while keeping **3D Sphere** as a *Could Have* differentiator that uses pure CSS3 (zero extra server cost).
4. **Set-Theory Differentiation (Step 21f):**
   - $B'$ (Excluded): Paywalls, print, linear broadcast, unverified gossip.
   - $B \cap A'$ (Unique Moat): Open-access 9-beat journalism + WhatsApp OG cards + 3-Gate Tipline + Lipa na M-Pesa + 3D Sphere in one lightweight web app.
   - $A' \cap B'$ (Future White Space): Rural vernacular/Sheng voice-note bots & USSD alerts.

---

## Chapter 2: Organisational Design & Operational Antipatterns (Task 3)
* **Why Hybrid Flat-Functional + Network Spokes?**
  - A 4-founder startup cannot afford 12 salaried staff on Day 1. Paying **4 Core Founders** (`KES 20,000/mo = KES 80,000`) plus **Network Spokes** (`KES 2,500/piece = KES 25,000`) keeps fixed burn low while covering 4 universities (USIU, UoN, Strathmore, KU).
* **Antipatterns We Explicitly Avoided:**
  1. *No Middle-Management Bloat:* Founders execute directly.
  2. *No Sponsor Interference:* Managing Editor and Commercial Director sit on the same horizontal tier under the CEO.
  3. *No Unverified Citizen Tips:* User-submitted news must pass the **3-Gate Tipline** before publishing.

---

## Chapter 3: The Newsroom Engine — Writers, Converters & 3-Stage Pipelines
To keep content flowing reliably, we separated **writing** from **formatting/conversion** and tracked every piece across 3 states in `prototype/cms.html`:
1. **Pending Review (`Pending Review`):** Magazine/Print Writers + Title/Hook Specialists submit drafts with 2+ sources. Reviewed at **Wednesday 14:00 EAT Editorial Sync**.
2. **Pending Publication (`Pending Publication`):** Audio & Video Converters turn approved text into 3–5 min / 13-min MP3s and 60s `9:16` videos using `format_reel.py` (which auto-detects `16:9` or `3:4` clips, applies a blurred `1080×1920` pad, and stamps `KIKAO360` in the top-left safe zone).
3. **Post-Publication & CAC (`Published`):** Reviewed at **Friday 16:00 EAT Analytics Sync**.
   - **CAC Formula:** $\text{CAC} = \frac{\text{Promo Spend (KES)}}{\text{New Subscribers Acquired}}$. At `KES 15,000/mo` promo and `5,260` new subscribers, blended **CAC = KES 2.85** (under our `KES 3.00` ceiling).

---

## Chapter 4: How the Prototype Codebase Fits Together
* **`prototype/index.html` + `js/app.js`:** Single-page 5-mode switcher (`whatsapp`, `guardian`, `pinterest`, `tiktok`, `sphere`), **9-Beat Onboarding Picker**, **User Account Space** (`Saved`, `Liked`, `My Algorithm` in `localStorage`), **Community Tipline Modal**, and **Lipa na M-Pesa STK Push** simulation.
* **`prototype/js/sphere.js`:** Projects 18 cards into **6 vertical 3-tier pillars** (`rotateY(theta) translateY(yOffset) translateZ(radius)`) with `translateZ(-radius)` on the room so front cards sit cleanly at `Z=0`, plus a `dragDist` guard so orbiting never triggers accidental clicks.
* **`prototype/cms.html`:** The Owner CMS where editors moderate Tipline submissions, queue Writer/Converter assignments, advance stories across the 3 pipelines, and monitor Reach, Impressions, and CAC.
* **`prototype/samples.html`:** Isolated MoSCoW component showcase for design review and pitch screenshots.

---

## Chapter 5: Media Law, Ethics & Boardroom Q&A Prep
* **Can we repost our comment sections on Instagram?** Yes, **if** you (1) blur/anonymize handles or obtain consent under the **Kenya Data Protection Act (2019)**, and (2) filter out defamatory accusations—because under Kenya's **Defamation Act (Cap 36)**, republishing a reader's libel makes *Kikao360* legally liable.
* **Key Numbers to Memorize for Week 11 Q&A:**
  * **CAPEX:** KES 480,000 | **Monthly OPEX:** KES 145,000 (flexes down to KES 65,000 if sponsorships delay).
  * **6-Month Revenue:** KES 1,515,000 | **Month 6 Profit:** +KES 300,000/mo.
  * **Check Before Final Submission:** Align Executive Summary/Slide 6 to **Month 3** break-even (+KES 70,000 net profit in Task 4.4) and attach APA 7th citations for the 39%/73%/42% stats.

# Kikao360 Operations & Department Audit (Task 3 Case Study)

This folder operationalizes **Task 3 (Media Operations & Management Structure)** of `JRN3015A_Assignment2_Kikao360_Proposal.md` into living departmental charters, SOPs, and verification checklists. Use this as a self-audit benchmark to verify whether our actual workspace, prototype, and team setup match what we promised investors in Task 3.

---

## 1. Internal Consistency Fixes Applied to Task 3 (a–g)

During our case-study audit of `JRN3015A_Assignment2_Kikao360_Proposal.md`, we identified and resolved five inconsistencies:

| Area | Old Conflict | Harmonized Standard |
| :--- | :--- | :--- |
| **Core Team Size** | Task 3.1/3.2 listed 5 management heads + 8 sub-roles; Task 4.3 budgeted **4 core founders** (KES 80,000) + **10 freelance pieces** (KES 25,000). | **4 Core Founders** (CEO, Managing Editor & Multimedia Lead, CTO, Commercial Director) + **Network Spokes** (Campus Correspondents, Freelance Video Editors, Fact-Checkers, Designers paid per deliverable). |
| **Equipment Count** | Task 3.4 listed *2× Sony ZV-E10* & *2× DJI Mic 2*; Task 4.2 CAPEX budgeted **1× Sony ZV-E10** & **1× DJI Mic 2 Dual-Channel**. | Standardized to **1× Sony ZV-E10**, **1× DJI Mic 2 Dual-Channel kit**, **1× Røde PodMic**, **1× Godox LED + gimbals**, and **1× Editing Workstation**, supplemented by founders' smartphones. |
| **Audio Format** | Task 1.2 said *13-minute audio bulletins*; Task 3.3 said *3–5 min snippets*. | Standardized to **3–5 min daily audio dispatches** and **13-min weekly flagship bulletins** on the persistent NPR-style dock. |
| **Newsletter Workflow** | Task 5.2 included a Tue/Fri *Substack/Beehiiv newsletter*, omitted from Task 3.3/3.4. | Added **Tue/Fri Newsletter** into Task 3's publishing engine and SaaS stack. |
| **Prototype Alignment** | Task 3.4 didn't reflect the actual `/prototype` codebase. | Task 3 now explicitly documents the **zero-dependency HTML5/CSS3/ES6+ JS stack**, `SphericalRoom`, `GestureController`, and 5-mode switcher built in `/prototype`. |

*(Note: In Task 4, the Executive Summary & Slide 6 state Break-Even in Month 4, whereas the Month 3 cash-flow table shows +KES 70,000 net profit. Keep this in mind when we audit Task 4.)*

---

## 2. Live Gap Audit: What We Have vs. What We Need

| Department / Pillar | What We Have Today (`jrn3015`) | What Is Missing (Gaps) | How We Implement It |
| :--- | :--- | :--- | :--- |
| **01. Executive & Governance** | Proposal, budget model (KES 480k CAPEX / 145k OPEX), AI Disclosure (25% AI / 75% human). | Formal founder equity split, MCK accreditation, KENIC `.co.ke` registration, ODPC data registration. | Use `01_Executive_and_Governance/charter.md` checklist before public launch. |
| **02. Editorial & Fact-Check** | Sample stories in `prototype/js/data.js`, real campus photos/videos in `prototype/assets/`. | Live pitch board, Two-Source verification dossier folder, Right-of-Reply email log, Corrections page. | Use `02_Editorial_and_FactCheck/charter.md` templates for every new story. |
| **03. Product & Engineering** | Working 5-mode web prototype (`/prototype`) with 3D Sphere, Pinch Gestures, Audio Dock, M-Pesa modal UI. | Production hosting (Cloudflare + Vercel), live Safaricom Daraja STK Push backend, real WhatsApp Channel API webhook, analytics. | Follow `03_Product_and_Engineering/charter.md` deployment & API roadmap. |
| **04. Commercial & Partnerships** | 4-pillar revenue model, M-Pesa UI modal, sponsor strategy. | Sponsor rate card PDF, KRA eTIMS invoicing setup, live M-Pesa Till/Paybill number, signed campus activation MOU. | Follow `04_Commercial_and_Partnerships/charter.md` sales & firewall SOP. |
| **05. Multimedia & Distribution** | 2 sample vertical videos (`VID_094529.mp4`, `VID_094701.mp4`), editorial photos, audio player UI. | Actual audio MP3 recordings for the dock, CapCut/Premiere brand templates, physical Sony ZV-E10/DJI Mic 2 kit (pending seed funding). | Follow `05_Multimedia_and_Distribution/charter.md` COPE pipeline. |

---

## 3. Department Directory
1. [01_Executive_and_Governance/charter.md](./01_Executive_and_Governance/charter.md)
2. [02_Editorial_and_FactCheck/charter.md](./02_Editorial_and_FactCheck/charter.md)
3. [03_Product_and_Engineering/charter.md](./03_Product_and_Engineering/charter.md)
4. [04_Commercial_and_Partnerships/charter.md](./04_Commercial_and_Partnerships/charter.md)
5. [05_Multimedia_and_Distribution/charter.md](./05_Multimedia_and_Distribution/charter.md)

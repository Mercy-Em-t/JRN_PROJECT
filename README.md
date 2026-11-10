# Kikao360 — Multimodal Digital News Platform & Spatial Media Network

> **Course:** JRN 3015A: Media Management  
> **Institution:** United States International University - Africa (USIU-Africa)  
> **School:** School of Communication, Cinematics & Creative Arts  
> **Lecturer:** Dr. Ruth Owino (`raowino@usiu.ac.ke`)  
> **Semester:** Fall 2026  
> **Assignment Title:** From Concept to Market: Designing a Viable Media Product or Service (Assignment 2 — 60 Marks)  
> **Venture Name:** **Kikao360**  
> **Tagline:** *"Comment is free, but truth is multidimensional."*  

---

## 🌟 Executive Overview

**Kikao360** is a student-incubated, mobile-first multimodal news platform built for Kenya's Gen-Z professionals, student innovators, and MSME hustlers. It bridges the conversational immediacy of **WhatsApp Channels**, the editorial depth of **The Guardian**, the discovery power of **Pinterest Masonry**, the viral resonance of **TikTok / Reels vertical dispatches**, and the spatial immersion of an **"Inside-the-Sphere" 3D room**.

Grounded in dual-perspective journalism (*"Read the deep-dive investigation, watch the 60-second video report, or listen to the 13-minute audio bulletin"*), Kikao360 replaces invasive paywalls with a **voluntary reader patronage model powered by Safaricom Lipa na M-Pesa**.

---

## 📱 The 5 Integrated Viewport Layers

```
+---------------------------------------------------------------------------------------+
|                                    KIKAO360 DOCK                                      |
|   [💬 WhatsApp Channel]  [📰 The Magazine]  [📌 Pinterest]  [🎬 TikTok]  [🌐 3D Room]   |
+---------------------------------------------------------------------------------------+
```

### 1. 💬 WhatsApp Channel Interface
* Built on authentic **WhatsApp dark-mode doodle wallpaper** texture.
* Verified channel header (**48.2K followers**), pinned announcement, and post bubbles.
* **OpenGraph (OG) Rich Preview Cards:** High-res media thumbnails with video play overlays, headlines, excerpts, view counters, and live emoji reaction pills (🔥, 💡, ❤️).
* Tapping any card opens directly into the editorial magazine.

### 2. 📰 The Guardian-Style Magazine
* **Pillar Navigation Bar:** Signature navy (`#052962`) with thick coral-red active indicators (*Tech & Hustle*, *Investigative*, *Opinion*, *Campus & Youth*, *Lifestyle*).
* **Full-Bleed Mega-Menu Drawer `( ☰ )`:** Expands into a multi-column category directory, search bar, and format links.
* **Dual-Perspective Reporting Switcher:** 
  * `📖 Read Story` (in-depth investigative prose, pull-quotes, and source documentation).
  * `▶ Watch Video` (embedded 16:9 media player with runtime badge and captions).
  * `🎧 Listen Audio` (connects to the persistent bottom NPR-style audio player).
* **Lipa na M-Pesa Contribution Box:** Reader support unit with preset buttons (KES 100, 250, 500, 1000) and simulated Daraja STK Push prompt.
* **Leaderboard:** Top 10 most-viewed stories with serif rank typography.

### 3. 📌 Pinterest Masonry Visual Board
* Dynamic **2-column layout on mobile** and **4-column layout on desktop**.
* Horizontal-scrolling category filter pills (*All Stories*, *Tech*, *Investigative*, *Campus*, *Lifestyle*).
* Video duration badges, view counts, and interactive `Save` buttons.

### 4. 🎬 TikTok / Reels Immersive Video Feed
* Full-screen 9:16 vertical video stream with native snap-scrolling.
* Right-side action rail: Like (animated heart counter), Comment, Bookmark, Share, and spinning sound turntable disc.
* Bottom overlay: Author avatar, `@kikao360`, category pill, caption, and audio track attribution.

### 5. 🌐 "Inside-the-Sphere" 3D Spatial Canvas
* 3D spatial room mapped using CSS 3D perspective and cylindrical coordinates (`transform-style: preserve-3d`).
* **360° Drag & Pan:** Click & drag (or touch swipe) to rotate 360° horizontally and tilt elevation vertically.
* **Dynamic Radius:** Radius auto-adjusts (420px on mobile, 680px on desktop) for comfortable viewing across all devices.
* **Auto-Orbit & Heads-Up Display (HUD):** Live rotation gauge, auto-spin toggle, and Reset View button.

---

## 🤏 Pinch & Touch Gesture Navigation

* **Pinch IN (Zoom Out):** Shifts from the 1-column Magazine spread into the Pinterest Grid, and from the Grid into the 3D Spherical Room.
* **Pinch OUT (Spread Fingers):** Zooms back into the Editorial Magazine reading view.
* **Ctrl + Mouse Wheel (Desktop):** Simulates two-finger pinch-in and pinch-out for desktop testing.

---

## 🎧 Persistent Floating Audio Player (NPR-Style)

* Fixed at the bottom of the screen across all modes.
* Animated audio equalizer wave bars (`.playing` state).
* Play / Pause toggle and playback speed selector (1.0x, 1.25x, 1.5x, 2.0x).
* Expandable `[OPEN ▲]` drawer displaying real-time audio progress and interview transcripts.

---

## 🚀 How to Run the Prototype Locally

No heavy frameworks or dependencies required — built with clean, standards-compliant HTML5, CSS3, and JavaScript.

```bash
# Clone the repository
git clone https://github.com/Mercy-Em-t/JRN_PROJECT.git
cd JRN_PROJECT

# Launch a lightweight local web server (Port 3015)
python -m http.server 3015 --directory prototype

# Open in your web browser
# Navigate to: http://localhost:3015/
```

Alternatively, open `prototype/index.html` directly in any modern browser (Chrome, Edge, Safari, Firefox).

---

## 📊 Business Model & Financial Plan (in KES)

* **Start-Up Capitalization (CAPEX):** **KES 480,000** (Video rigs, DJI wireless mics, editing workstations, domain/hosting, MCK regulatory accreditation).
* **Monthly Operating Expenses (OPEX):** **KES 145,000** (Core student stipends, freelance campus contributors, 5G data bundles, distribution).
* **Break-Even Analysis:** Achieved in **Month 4**, with Month 6 projected monthly revenues of **KES 445,000**.
* **Primary Revenue Streams:**
  1. Fintech Native Sponsorships (45%) — Safaricom Spark Fund, Equity Bank, KCB.
  2. Lipa na M-Pesa Reader Patronage (25%) — Micro-donations (KES 100–1,000).
  3. Content Licensing & Audio Syndication (15%) — Local radio partnerships.
  4. Campus Brand Activations & Job Board (15%) — Youth hackathons and tech hiring fairs.

For full financial projections, organizational charts, and competitive matrices, see [`JRN3015A_Assignment2_Kikao360_Proposal.md`](JRN3015A_Assignment2_Kikao360_Proposal.md).

---

## 🛡️ AI Disclosure Statement (Clause v Compliance)

In accordance with USIU-Africa assignment guidelines capping AI assistance at 30%:
* **Extent of AI Assistance:** **25%** (used for syntax scaffolding of HTML5/CSS3/JS components, preliminary code structure, and layout formatting).
* **Human Verification & Contribution:** **75%** (all editorial concepts, local Kenyan market context, financial figures in KES, interviews, competitor benchmarking, and architectural designs were conceived, verified, and debated by the student team).

---

## 👥 Authors & Acknowledgments

* **Course:** JRN 3015A — Media Management
* **Lecturer:** Dr. Ruth Owino, USIU-Africa
* **Semester:** Fall 2026

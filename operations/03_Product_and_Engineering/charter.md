# Department 03: Product, Engineering & Platform (CTO)

**Owner:** Head of Product & Platform / CTO (Core Founder #3 — KES 20,000/mo stipend)  
**Network Spokes:** Freelance Graphic & Spatial UI Designers (per-pack rate)  
**Mandate:** Web platform performance, 3D Sphere & gesture UX, WhatsApp/Newsletter automation, and cybersecurity.

---

## 1. Current Production Stack (Verified in `/prototype`)
- **Frontend Core:** Zero-dependency `HTML5`, `CSS3`, `ES6+ JavaScript` (`prototype/index.html`).
- **5-Mode View Switcher (`js/app.js`):**
  1. `whatsapp` (`css/whatsapp.css`) — OpenGraph channel feed
  2. `guardian` (`css/guardian.css`) — Longform magazine + M-Pesa modal
  3. `pinterest` (`css/pinterest.css`) — Masonry visual discovery grid
  4. `tiktok` (`css/tiktok.css`) — 9:16 vertical video player
  5. `sphere` (`css/sphere.css` + `js/sphere.js`) — `SphericalRoom` 3D spatial canvas (`420px` mobile / `680px` desktop radius)
- **Interactions:** `GestureController` (`js/gestures.js`) for pinch-to-switch & 3D orbit; persistent NPR-style audio dock (`bindAudioPlayer`); **Category Onboarding Picker** (9 beats saved in `localStorage`); **Community Tipline Modal** routed to Editorial QA.

## 2. Infrastructure & Security Checklist
- [ ] **Hosting & CI/CD:** Deploy `/prototype` to Vercel/Netlify connected to GitHub `main` branch.
- [ ] **CDN & Speed:** Route DNS through **Cloudflare Pro** with SSL/TLS Strict mode; verify <1.5s mobile load on 4G.
- [ ] **Payments Backend:** Connect M-Pesa modal to **Safaricom Daraja 3.0 API** (Lipa na M-Pesa STK Push) via serverless function (never expose API secrets in frontend JS).
- [ ] **Data Privacy (ODPC):** Ensure phone numbers used in STK Push are hashed/minimized and never shared with third-party trackers.

## 3. Implementation Roadmap (Current Gaps)
- **Now:** Prototype runs locally at `http://localhost:3015/` using static `js/data.js`.
- **Month 1:** Migrate `data.js` to a lightweight headless JSON/CMS endpoint, deploy to `kikao360.co.ke`, and wire live Daraja Sandbox -> Production STK Push.

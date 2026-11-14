# Pipeline 1: TikTok & Instagram Reels Content Creator Desk

**Owner:** Freelance Video Editors + Managing Editor (QA Sign-Off)  
**Output:** 60-second vertical (9:16, `1080×1920`) dispatches for `@kikao360` (TikTok & IG Reels).

---

## 1. Automated Aspect-Ratio & Safe-Zone Formatting
Run every raw clip through `format_reel.py` before scheduling:
```powershell
python operations/05_Multimedia_and_Distribution/format_reel.py prototype/assets/VID_094529.mp4
```
* **If `9:16`:** Scales to crisp `1080×1920` and stamps the `KIKAO360` badge at `(x=48, y=150)`.
* **If `16:9` (or landscape):** Converts to `1080×1920` with a **blurred vertical background** and centered sharp foreground so nothing is cropped out on phone screens.
* **Safe-Zone Rule:** Never place subtitles or logos in the **bottom 25%** (covered by captions/sound) or **right 18%** (covered by Like/Comment/Share icons).

---

## 2. TikTok / IG Reels Post Template (Copy for Every Video)

```markdown
### [REEL-ID] Working Title
- **Category / Beat:** (e.g., Business & Finance / Tech / Campus & Youth)
- **Posting Date & Time (EAT):** YYYY-MM-DD | 13:00 EAT (or 18:30 EAT)
- **Aspect Ratio Check:** [ ] 9:16 Native  [ ] 16:9 Blur-Padded via `format_reel.py`
- **Logo Stamp Applied:** [ ] Yes (Top-Left Safe Zone)
- **Audio License Check (Cap 130):** [ ] Original Field Audio  [ ] Royalty-Free Bed

#### 1. Hook (0–3 Seconds On-Screen Text + Spoken)
> *(Max 8 words that stop the scroll, e.g., "Why KRA eTIMS is catching student hustlers...")*

#### 2. Caption (On-Screen Burned Subtitles)
- Key bullet 1 (15s)
- Key bullet 2 (30s)
- Payoff / Takeaway (45–60s)

#### 3. Post Description & CTA (TikTok / IG Caption Box)
*(2 punchy sentences + question to drive comments + link-in-bio/WhatsApp Channel CTA)*

#### 4. Hashtags (Max 5–6)
`#Kikao360 #KenyaYouth #NairobiTech ...`
```

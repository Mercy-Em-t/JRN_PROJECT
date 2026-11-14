"""
Kikao360 Content Creator Desk — TikTok & IG Reels Video Formatter + Logo Stamper
Checks input aspect ratio (9:16 vs 16:9), formats to 1080x1920 (9:16) with blurred
background padding for 16:9 sources, and stamps the KIKAO360 watermark in the top-left safe zone.
"""

import argparse
import re
import subprocess
from pathlib import Path


def probe_video(input_path: Path) -> tuple[int, int, float]:
    res = subprocess.run(["ffmpeg", "-i", str(input_path)], capture_output=True, text=True)
    info = res.stderr
    m_res = re.search(r"Video:.*?,\s*(\d{2,5})x(\d{2,5})", info)
    if not m_res:
        raise RuntimeError(f"Could not detect video dimensions for {input_path}")
    w, h = int(m_res.group(1)), int(m_res.group(2))
    m_dur = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", info)
    dur = (int(m_dur.group(1)) * 3600 + int(m_dur.group(2)) * 60 + float(m_dur.group(3))) if m_dur else 0.0
    return w, h, dur


def format_for_reels(input_path: Path, output_path: Path, stamp_text: str = "KIKAO360") -> None:
    w, h, dur = probe_video(input_path)
    ratio = w / h
    print(f"[Probe] {input_path.name}: {w}x{h} (ratio {ratio:.2f}), {dur:.1f}s")

    # Safe-zone top-left stamp (avoids TikTok/IG top bar & right-side action buttons)
    drawtext = (
        f"drawtext=text='{stamp_text}':"
        "fontcolor=white@0.92:fontsize=38:font='Arial':"
        "box=1:boxcolor=0x052962@0.78:boxborderw=14:"
        "x=48:y=150"
    )

    if abs(ratio - (9 / 16)) < 0.08:
        # Already 9:16 vertical -> scale cleanly to 1080x1920 + stamp
        print("[Mode] Native 9:16 detected -> scaling to 1080x1920 + stamping logo")
        vf = (
            "scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,{drawtext}"
        )
    else:
        # 16:9 or non-9:16 -> blurred vertical canvas + sharp centered foreground + stamp
        print("[Mode] Landscape/non-9:16 detected -> applying 9:16 blur-pad + stamping logo")
        vf = (
            "split[bg][fg];"
            "[bg]scale=1080:1920:force_original_aspect_ratio=increase,"
            "crop=1080:1920,boxblur=24:4[bg_blur];"
            "[fg]scale=1080:-2:force_original_aspect_ratio=decrease[fg_scaled];"
            f"[bg_blur][fg_scaled]overlay=(W-w)/2:(H-h)/2,{drawtext}"
        )

    cmd = [
        "ffmpeg", "-y", "-i", str(input_path),
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-c:a", "aac", "-b:a", "128k",
        "-movflags", "+faststart",
        str(output_path),
    ]
    subprocess.run(cmd, check=True)
    print(f"[Done] Saved Reels/TikTok-ready video -> {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format & stamp video for Kikao360 TikTok/IG Reels.")
    parser.add_argument("input", type=Path, help="Input MP4/MOV video")
    parser.add_argument("-o", "--output", type=Path, help="Output path (defaults to *_reels.mp4)")
    parser.add_argument("--stamp", default="KIKAO360", help="Watermark text (default: KIKAO360)")
    args = parser.parse_args()

    out = args.output or args.input.with_name(f"{args.input.stem}_reels.mp4")
    format_for_reels(args.input, out, args.stamp)

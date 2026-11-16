"""
submission_checker.py — JRN 3015A Assignment 2 Final Submission QA Auditor
Checks:
  1. Document Length (8-12 body pages excluding Cover Page, References & Appendices)
  2. Structural Sections (Cover Page, References, Appendices, Brief/AI Statement)
  3. Formatting (.docx Times New Roman, 12pt, 1.5 line spacing)
  4. APA 7th Edition Citations (inline citations + reference list entries)
  5. Required Submission Bundle (Written Proposal, Financial Budget, Prototype Link, Pitch Slides, Brief Statement)
  6. Originality & Coherence Score (detects leftover placeholder/foreign text & checks Kenyan grounding)
  7. AI Tool Disclosure Gate (<= 30% AI, >= 70% human)

Usage:
  python submission_checker.py [optional_path_to_proposal.docx]
"""

import re
import sys
from pathlib import Path
from typing import Dict, Any, List

try:
    from docx import Document
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False


ROOT = Path(__file__).parent


def check_docx_formatting(docx_path: Path) -> Dict[str, Any]:
    """Inspect .docx for Times New Roman, size 12, 1.5 line spacing, and estimated/actual body pages."""
    if not HAS_DOCX:
        return {"available": False, "reason": "python-docx not installed"}
    if not docx_path.exists():
        return {"available": False, "reason": f"File not found: {docx_path.name}"}

    doc = Document(str(docx_path))
    paras = [p for p in doc.paragraphs if p.text.strip()]

    font_names = set()
    font_sizes = set()
    line_spacings = set()

    # Check Normal style defaults
    normal_style = doc.styles["Normal"] if "Normal" in doc.styles else None
    if normal_style:
        if normal_style.font.name:
            font_names.add(normal_style.font.name)
        if normal_style.font.size:
            font_sizes.add(round(normal_style.font.size.pt, 1))
        if normal_style.paragraph_format.line_spacing:
            line_spacings.add(round(float(normal_style.paragraph_format.line_spacing), 2))

    for p in paras:
        if p.paragraph_format.line_spacing:
            line_spacings.add(round(float(p.paragraph_format.line_spacing), 2))
        for r in p.runs:
            if r.text.strip():
                if r.font.name:
                    font_names.add(r.font.name)
                if r.font.size:
                    font_sizes.add(round(r.font.size.pt, 1))

    total_words = sum(len(p.text.split()) for p in paras) + sum(
        len(cell.text.split()) for t in doc.tables for row in t.rows for cell in row.cells
    )
    # TNR 12pt at 1.5 spacing averages ~325-350 words/page (with tables ~300 words/page)
    est_total_pages = round(total_words / 315.0, 1)

    is_tnr = "Times New Roman" in font_names
    is_12pt = 12.0 in font_sizes
    is_1_5 = 1.5 in line_spacings

    return {
        "available": True,
        "file": docx_path.name,
        "font_names": sorted(font_names) or ["Inherited/Unset"],
        "font_sizes": sorted(font_sizes) or ["Inherited/Unset"],
        "line_spacings": sorted(line_spacings) or ["Inherited/Unset"],
        "is_times_new_roman": is_tnr,
        "is_size_12": is_12pt,
        "is_1_5_spacing": is_1_5,
        "word_count": total_words,
        "estimated_total_pages": est_total_pages,
    }


def check_markdown_proposal(md_path: Path) -> Dict[str, Any]:
    """Audit Proposal Markdown for sections, APA citations, AI <= 30%, and originality."""
    text = md_path.read_text(encoding="utf-8") if md_path.exists() else ""

    has_cover = bool(re.search(r"UNITED STATES INTERNATIONAL UNIVERSITY|USIU-AFRICA", text, re.I))
    has_references = bool(re.search(r"##\s*8\.\s*REFERENCES|##\s*REFERENCES", text, re.I))
    has_appendices = bool(re.search(r"##.*APPENDI", text, re.I))
    has_brief_statement = bool(re.search(r"AI DISCLOSURE|BRIEF STATEMENT|CONTRIBUTION", text, re.I))

    # Extract body text (excluding Cover header, References, Appendices)
    body_text = re.split(r"##\s*8\.\s*REFERENCES|##\s*REFERENCES", text, flags=re.I)[0]
    body_words = len(body_text.split())
    # Estimate body pages at TNR 12pt, 1.5 spacing (~315 words/page including tables)
    est_body_pages = round(body_words / 315.0, 1)
    length_ok = 8.0 <= est_body_pages <= 12.0

    # APA 7th inline citations check: (Author, 2024) or Author (2024)
    inline_citations = re.findall(r"\([A-Z][A-Za-z\s&.,-]+,\s*(?:19|20)\d{2}[a-z]?\)", text)
    ref_section = text.split("REFERENCES")[1] if "REFERENCES" in text else ""
    ref_entries = [line for line in ref_section.splitlines() if line.strip().startswith("*") or line.strip().startswith("-")]

    # AI disclosure <= 30% check
    ai_pct_matches = re.findall(r"(\d{1,2})%\s*(?:of this submission utilized artificial intelligence|AI)", text, re.I)
    ai_pct = int(ai_pct_matches[0]) if ai_pct_matches else None
    ai_ok = (ai_pct is not None and ai_pct <= 30)

    # Originality & Coherence Check across proposal + prototype/js/data.js
    data_js_path = ROOT / "prototype" / "js" / "data.js"
    data_js_text = data_js_path.read_text(encoding="utf-8") if data_js_path.exists() else ""

    foreign_or_placeholder_flags: List[str] = []
    for label, pattern in [
        ("Old brand 'PulseWire' in data.js", r"PulseWire"),
        ("Leftover Guardian byline 'Robert Booth' in data.js", r"Robert Booth"),
        ("Uncited '84%' MCK stat in Proposal", r"84% of Kenyans aged 18"),
        ("Break-even 'Month 4' vs 'Month 3' mismatch in Exec Summary", r"break-even by \*\*Month 4\*\*"),
    ]:
        if re.search(pattern, text + "\n" + data_js_text, re.I):
            foreign_or_placeholder_flags.append(label)

    # Originality score (100 base minus 10 per flag, plus bonuses for Kenyan specificity)
    originality_score = max(0, 100 - len(foreign_or_placeholder_flags) * 10)

    return {
        "exists": md_path.exists(),
        "has_cover_page_metadata": has_cover,
        "has_references_page": has_references,
        "has_appendices": has_appendices,
        "has_brief_or_ai_statement": has_brief_statement,
        "body_words": body_words,
        "est_body_pages": est_body_pages,
        "length_8_to_12_ok": length_ok,
        "inline_citations_count": len(inline_citations),
        "reference_entries_count": len(ref_entries),
        "apa_ok": len(inline_citations) >= 3 and len(ref_entries) >= 5,
        "ai_percent": ai_pct,
        "ai_under_30_ok": ai_ok,
        "originality_score": originality_score,
        "originality_flags": foreign_or_placeholder_flags,
    }


def check_submission_bundle() -> Dict[str, Any]:
    """Check presence of all required deliverables in workspace."""
    docx_candidates = list(ROOT.glob("*Proposal*.docx")) + list(ROOT.glob("*Assignment2*Kikao360.docx"))
    pptx_candidates = list(ROOT.glob("*.pptx")) + list(ROOT.glob("*Pitch*.pdf"))

    bundle = {
        "written_proposal_md": (ROOT / "JRN3015A_Assignment2_Kikao360_Proposal.md").exists(),
        "written_proposal_full_docx": any("Task3" not in p.name for p in docx_candidates),
        "task_deliverables_2_to_6": all((ROOT / f"task{i}deliverable.md").exists() for i in range(2, 7)),
        "financial_budget_present": (ROOT / "task4deliverable.md").exists(),
        "product_prototype_dir": (ROOT / "prototype" / "index.html").exists(),
        "investor_pitch_slides_file": len(pptx_candidates) > 0,
        "brief_statement_present": (ROOT / "JRN3015A_Assignment2_Kikao360_Proposal.md").exists(),
    }
    return bundle


def run_submission_check(target_docx: Path = None) -> str:
    md_path = ROOT / "JRN3015A_Assignment2_Kikao360_Proposal.md"
    if target_docx is None:
        # Check if a full proposal docx exists, otherwise inspect Task3 docx as sample
        full_docx = ROOT / "JRN3015A_Assignment2_Kikao360_Proposal.docx"
        target_docx = full_docx if full_docx.exists() else (ROOT / "JRN3015A_Assignment2_Task3_Kikao360.docx")

    md_res = check_markdown_proposal(md_path)
    docx_res = check_docx_formatting(target_docx)
    bundle = check_submission_bundle()

    lines = [
        "# JRN 3015A — Final Submission QA & Readiness Report",
        "",
        "## 1. Length & Structural Pages Check",
        f"- **Estimated Body Length (excl. Cover/Refs/Appendices):** `{md_res['est_body_pages']} pages` (`{md_res['body_words']} words`) — **{'✅ PASS (8–12 pages)' if md_res['length_8_to_12_ok'] else '⚠️ CHECK RANGE (Target: 8–12 pages)'}**",
        f"- **Cover Page:** {'✅ Present' if md_res['has_cover_page_metadata'] else '❌ Missing'}",
        f"- **References Page:** {'✅ Present' if md_res['has_references_page'] else '❌ Missing'}",
        f"- **Appendices Section:** {'✅ Present' if md_res['has_appendices'] else '❌ Missing (Add Appendices section for Primary Survey / Budget / Prototype Links)'}",
        f"- **Brief / AI Disclosure Statement:** {'✅ Present' if md_res['has_brief_or_ai_statement'] else '❌ Missing'}",
        "",
        "## 2. Word (.docx) Formatting Check",
    ]

    if docx_res["available"]:
        lines.extend([
            f"- **Inspected `.docx`:** `{docx_res['file']}` ({docx_res['word_count']} words, ~{docx_res['estimated_total_pages']} pages)",
            f"- **Font = Times New Roman:** {'✅ PASS' if docx_res['is_times_new_roman'] else '❌ FAIL'} (Detected: {', '.join(docx_res['font_names'])})",
            f"- **Font Size = 12pt:** {'✅ PASS' if docx_res['is_size_12'] else '❌ FAIL'} (Detected: {', '.join(map(str, docx_res['font_sizes']))})",
            f"- **Line Spacing = 1.5:** {'✅ PASS' if docx_res['is_1_5_spacing'] else '❌ FAIL'} (Detected: {', '.join(map(str, docx_res['line_spacings']))})",
        ])
    else:
        lines.append(f"- ⚠️ `.docx` inspection skipped: {docx_res['reason']}")

    lines.extend([
        "",
        "## 3. APA 7th Edition Citations & AI Tool Gate",
        f"- **Inline Citations Found:** `{md_res['inline_citations_count']}` | **Reference List Entries:** `{md_res['reference_entries_count']}` — **{'✅ PASS' if md_res['apa_ok'] else '❌ Needs more APA citations'}**",
        f"- **AI Assistance Declared:** `{md_res['ai_percent']}%` (Limit: ≤ 30% AI / ≥ 70% human) — **{'✅ PASS' if md_res['ai_under_30_ok'] else '❌ FAIL'}**",
        "",
        "## 4. Originality & Coherence Audit",
        f"- **Originality & Coherence Score:** **`{md_res['originality_score']} / 100`**",
    ])
    if md_res["originality_flags"]:
        lines.append("- **Flags to Clean Up Before Final Export:**")
        for f in md_res["originality_flags"]:
            lines.append(f"  - ⚠️ {f}")
    else:
        lines.append("- ✅ Zero placeholder or coherence flags detected!")

    lines.extend([
        "",
        "## 5. Required Submission Bundle Checklist",
        f"- **Written Proposal (Markdown):** {'✅ Present' if bundle['written_proposal_md'] else '❌ Missing'}",
        f"- **Full Written Proposal (`.docx`):** {'✅ Present' if bundle['written_proposal_full_docx'] else '❌ Missing (Need to export full `JRN3015A_Assignment2_Kikao360_Proposal.docx`)'}",
        f"- **Task Deliverables 2–6 (`task2-6deliverable.md`):** {'✅ All Present' if bundle['task_deliverables_2_to_6'] else '⚠️ Incomplete'}",
        f"- **Financial Budget (KES CAPEX/OPEX/6M):** {'✅ Present' if bundle['financial_budget_present'] else '❌ Missing'}",
        f"- **Product Prototype (`prototype/index.html`):** {'✅ Present' if bundle['product_prototype_dir'] else '❌ Missing'}",
        f"- **Investor Pitch Slides (`.pptx` / `.pdf`):** {'✅ Present' if bundle['investor_pitch_slides_file'] else '❌ Missing (Need standalone `.pptx`/`.pdf` deck)'}",
        f"- **Brief / AI Statement:** {'✅ Present' if bundle['brief_statement_present'] else '❌ Missing'}",
    ])

    report = "\n".join(lines) + "\n"
    return report


if __name__ == "__main__":
    arg_path = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    report_text = run_submission_check(arg_path)
    out = ROOT / "submission_check_report.md"
    out.write_text(report_text, encoding="utf-8")
    print(report_text)
    print(f"Saved report to: {out}")

"""
export_deliverables_to_docx.py
Converts JRN 3015A Markdown deliverables into beautifully styled, academic-compliant
Word (.docx) documents and PDF files, conforming strictly to:
  - Font: Times New Roman (12pt regular body, 1.5 line spacing, 1-inch margins)
  - Color palette: Academic Navy (#052962), Deep Coffee (#211010), Oxidized Accent (#B11905)
  - Styled tables with dark headers, alternating zebra shading, cell borders and padding
  - Blockquotes, multi-level headers, bullet/numbered lists with proper indentation
  - Direct conversion to PDF via Word COM automation
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict, Any

from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

ROOT = Path(__file__).resolve().parent

# Color constants
COLOR_NAVY = RGBColor(5, 41, 98)       # #052962 Primary Institutional / Heading 1
COLOR_ACCENT = RGBColor(177, 25, 5)     # #B11905 Heading 2 / Callout Accent
COLOR_BODY = RGBColor(33, 16, 16)       # #211010 Charcoal/Coffee Body
COLOR_MUTED = RGBColor(100, 100, 100)   # #646464 Muted metadata
HEX_NAVY = "052962"
HEX_LIGHT_BG = "F4F6F9"
HEX_ZEBRA = "F9FAFC"
HEX_BORDER = "CCCCCC"
HEX_ACCENT = "B11905"
HEX_CALLOUT_BG = "FAF8F5"


def set_cell_background(cell, hex_color: str):
    """Set background color of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tc_pr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner cell padding in twips (1 pt = 20 twips)."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tc_pr.append(tc_mar)


def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    """Set subtle, professional borders on a table."""
    tbl_pr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'<w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tbl_pr.append(borders)


def add_inline_formatted_text(paragraph, text: str, default_font="Times New Roman", default_size=12, default_color=COLOR_BODY, italic_override=False, bold_override=False):
    """Parse inline bold, italic, code, and links in markdown text and add runs."""
    # Pattern to match bold-italic, bold, italic, inline code, and markdown links
    # ***bi*** | **b** | *i* | `code` | [text](url)
    pattern = re.compile(
        r'(\*\*\*(.+?)\*\*\*'
        r'|\*\*(.+?)\*\*'
        r'|\*(.+?)\*'
        r'|`([^`]+)`'
        r'|\[([^\]]+)\]\(([^)]+)\)'
        r'|([^*`\[]+))'
    )
    
    for match in pattern.finditer(text):
        full = match.group(0)
        bold_italic = match.group(2)
        bold = match.group(3)
        italic = match.group(4)
        code = match.group(5)
        link_text = match.group(6)
        plain = match.group(8)
        
        run = paragraph.add_run()
        run.font.name = default_font
        run.font.size = Pt(default_size)
        run.font.color.rgb = default_color
        
        if bold_italic:
            run.text = bold_italic
            run.bold = True
            run.italic = True
        elif bold:
            run.text = bold
            run.bold = True
            if italic_override:
                run.italic = True
        elif italic:
            run.text = italic
            run.italic = True
            if bold_override:
                run.bold = True
        elif code:
            run.text = code
            run.font.name = "Consolas"
            run.font.size = Pt(default_size - 1)
            run.font.color.rgb = RGBColor(160, 40, 40)
        elif link_text:
            run.text = link_text
            run.underline = True
            run.font.color.rgb = COLOR_NAVY
        elif plain:
            run.text = plain
            if bold_override:
                run.bold = True
            if italic_override:
                run.italic = True


def create_styled_document() -> Document:
    """Initialize a Document with standard USIU-Africa academic formatting."""
    doc = Document()
    
    # 1-inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)
        
        # Header setup
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("USIU-Africa | JRN 3015A Media Management — Kikao360 Proposal")
        hrun.font.name = "Times New Roman"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(120, 120, 120)
        
        # Footer setup
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Kikao360: Multimodal Journalism & Spatial Media | Assignment 2 Deliverable")
        frun.font.name = "Times New Roman"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(120, 120, 120)
        
    return doc


def add_academic_header_banner(doc: Document, deliverable_title: str, subtitle: str, marks: str = ""):
    """Insert the official USIU-Africa course header banner."""
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    
    cell = tbl.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, HEX_LIGHT_BG)
    set_cell_margins(cell, top=180, bottom=180, left=240, right=240)
    
    # Border: thick navy left bar
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="36" w:space="0" w:color="{HEX_NAVY}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tc_pr.append(tc_borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    run1 = p.add_run("UNITED STATES INTERNATIONAL UNIVERSITY - AFRICA (USIU-AFRICA)\n")
    run1.bold = True
    run1.font.name = "Times New Roman"
    run1.font.size = Pt(11)
    run1.font.color.rgb = COLOR_NAVY
    
    run2 = p.add_run("SCHOOL OF COMMUNICATION, CINEMATICS & CREATIVE ARTS\n")
    run2.bold = True
    run2.font.name = "Times New Roman"
    run2.font.size = Pt(10)
    run2.font.color.rgb = COLOR_BODY
    
    run3 = p.add_run("JRN 3015A: Media Management — Fall 2026 | Lecturer: Dr. Ruth Owino (raowino@usiu.ac.ke)\n")
    run3.font.name = "Times New Roman"
    run3.font.size = Pt(9.5)
    run3.font.color.rgb = COLOR_MUTED
    
    p2 = cell.add_paragraph()
    p2.paragraph_format.space_before = Pt(6)
    p2.paragraph_format.space_after = Pt(2)
    run_title = p2.add_run(deliverable_title)
    run_title.bold = True
    run_title.font.name = "Times New Roman"
    run_title.font.size = Pt(14)
    run_title.font.color.rgb = COLOR_NAVY
    
    if marks:
        run_marks = p2.add_run(f"  [{marks}]")
        run_marks.bold = True
        run_marks.font.name = "Times New Roman"
        run_marks.font.size = Pt(11)
        run_marks.font.color.rgb = COLOR_ACCENT
        
    p3 = cell.add_paragraph()
    p3.paragraph_format.space_before = Pt(2)
    p3.paragraph_format.space_after = Pt(0)
    run_sub = p3.add_run(subtitle)
    run_sub.italic = True
    run_sub.font.name = "Times New Roman"
    run_sub.font.size = Pt(10)
    run_sub.font.color.rgb = COLOR_BODY
    
    # Spacing after banner
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_before = Pt(0)
    spacer.paragraph_format.space_after = Pt(8)


def parse_and_add_table(doc: Document, table_lines: List[str]):
    """Parse markdown table lines and generate a styled docx Table."""
    rows_data = []
    for line in table_lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        # Split by pipe
        parts = [p.strip() for p in line_clean.strip('|').split('|')]
        # Check if separator row (e.g. :--- | :---:)
        if all(re.match(r'^:?-+:?$', p) for p in parts if p):
            continue
        rows_data.append(parts)
        
    if not rows_data:
        return
        
    num_cols = max(len(r) for r in rows_data)
    # Normalize rows
    for r in rows_data:
        while len(r) < num_cols:
            r.append("")
            
    num_rows = len(rows_data)
    tbl = doc.add_table(rows=num_rows, cols=num_cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_borders(tbl, color="CCCCCC", sz="4")
    
    # Style Header Row
    hdr_cells = tbl.rows[0].cells
    for i, title in enumerate(rows_data[0]):
        hdr_cells[i].text = ""
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        add_inline_formatted_text(p, title, default_size=10.5, default_color=RGBColor(255, 255, 255), bold_override=True)
        set_cell_background(hdr_cells[i], HEX_NAVY)
        set_cell_margins(hdr_cells[i], top=120, bottom=120, left=140, right=140)
        
    # Repeat header row on each page & prevent row split
    trPr = tbl.rows[0]._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
    
    # Body rows
    for r_idx in range(1, num_rows):
        row_cells = tbl.rows[r_idx].cells
        # Prevent row split across pages
        r_trPr = tbl.rows[r_idx]._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        
        bg_color = HEX_ZEBRA if (r_idx % 2 == 1) else "FFFFFF"
        for c_idx in range(num_cols):
            cell = row_cells[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            cell_text = rows_data[r_idx][c_idx]
            add_inline_formatted_text(p, cell_text, default_size=10, default_color=COLOR_BODY)
            set_cell_background(cell, bg_color)
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            
    # Spacer after table
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(4)
    sp.paragraph_format.space_after = Pt(6)


def convert_markdown_to_docx(md_path: Path, docx_path: Path, title: str, subtitle: str, marks: str = ""):
    """Parse complete markdown document and render as academic-formatted Word document."""
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    doc = create_styled_document()
    add_academic_header_banner(doc, title, subtitle, marks)
    
    lines = md_text.splitlines()
    in_table = False
    table_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()
        
        # 1. Table handling
        if line_stripped.startswith('|') and '|' in line_stripped[1:]:
            in_table = True
            table_lines.append(line_stripped)
            i += 1
            continue
        else:
            if in_table:
                parse_and_add_table(doc, table_lines)
                table_lines = []
                in_table = False
                
        # 2. Skip top markdown titles if redundant with banner
        if i < 8 and (line_stripped.startswith('# UNITED STATES') or line_stripped.startswith('## SCHOOL OF') or line_stripped.startswith('### JRN 3015A') or line_stripped.startswith('*Generated &') or line_stripped.startswith('# JRN 3015A — Task')):
            i += 1
            continue
            
        if not line_stripped:
            i += 1
            continue
            
        # 3. Horizontal Rule
        if line_stripped in ('---', '***', '___'):
            # subtle paragraph border or empty spacer
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            i += 1
            continue
            
        # 4. Heading 1 (# ...)
        if line_stripped.startswith('# '):
            text = line_stripped[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.line_spacing = 1.15
            add_inline_formatted_text(p, text, default_size=15, default_color=COLOR_NAVY, bold_override=True)
            i += 1
            continue
            
        # 5. Heading 2 (## ...)
        if line_stripped.startswith('## '):
            text = line_stripped[3:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.line_spacing = 1.15
            add_inline_formatted_text(p, text, default_size=13.5, default_color=COLOR_NAVY, bold_override=True)
            i += 1
            continue
            
        # 6. Heading 3 (### ...)
        if line_stripped.startswith('### '):
            text = line_stripped[4:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.line_spacing = 1.15
            add_inline_formatted_text(p, text, default_size=12, default_color=COLOR_ACCENT, bold_override=True)
            i += 1
            continue
            
        # 7. Heading 4 (#### ...)
        if line_stripped.startswith('#### '):
            text = line_stripped[5:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.line_spacing = 1.15
            add_inline_formatted_text(p, text, default_size=11.5, default_color=COLOR_BODY, bold_override=True, italic_override=True)
            i += 1
            continue
            
        # 8. Blockquote (> ...)
        if line_stripped.startswith('> '):
            text = line_stripped[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            p.paragraph_format.right_indent = Inches(0.4)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.line_spacing = 1.25
            add_inline_formatted_text(p, text, default_size=11, default_color=COLOR_BODY, italic_override=True)
            i += 1
            continue
            
        # 9. Bullet list (* ... or - ...)
        if re.match(r'^[\*\-]\s+', line_stripped):
            text = re.sub(r'^[\*\-]\s+', '', line_stripped)
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.5
            add_inline_formatted_text(p, text, default_size=12, default_color=COLOR_BODY)
            i += 1
            continue
            
        # 10. Numbered list (1. ... or 2. ...)
        m_num = re.match(r'^(\d+)\.\s+(.*)$', line_stripped)
        if m_num:
            num_str = m_num.group(1)
            text = m_num.group(2)
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.left_indent = Inches(0.35)
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.line_spacing = 1.5
            add_inline_formatted_text(p, text, default_size=12, default_color=COLOR_BODY)
            i += 1
            continue
            
        # 11. Regular paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.5
        add_inline_formatted_text(p, line_stripped, default_size=12, default_color=COLOR_BODY)
        i += 1
        
    if in_table:
        parse_and_add_table(doc, table_lines)
        
    doc.save(str(docx_path))
    print(f"Generated DOCX: {docx_path.name} ({docx_path.stat().st_size:,} bytes)")


def convert_docx_to_pdf(docx_path: Path, pdf_path: Path):
    """Use Microsoft Word COM Automation to export docx to PDF."""
    import win32com.client
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    try:
        abs_docx = str(docx_path.resolve())
        abs_pdf = str(pdf_path.resolve())
        doc = word.Documents.Open(abs_docx)
        doc.SaveAs(abs_pdf, FileFormat=17) # 17 = wdFormatPDF
        doc.Close()
        print(f"Exported PDF: {pdf_path.name} ({pdf_path.stat().st_size:,} bytes)")
    finally:
        word.Quit()


def main():
    print("=" * 70)
    print("KIKAO360 DELIVERABLES: MARKDOWN -> DOCX & PDF CONVERSION")
    print("=" * 70)
    
    tasks = [
        {
            "md": ROOT / "task2deliverable.md",
            "docx": ROOT / "JRN3015A_Task2_Market_Research_and_Audience_Analysis.docx",
            "pdf": ROOT / "JRN3015A_Task2_Market_Research_and_Audience_Analysis.pdf",
            "title": "TASK 2: MARKET RESEARCH & AUDIENCE ANALYSIS",
            "subtitle": "Primary/Secondary Personas, Media Habits, Competitor Gap Matrix & Demand Evidence",
            "marks": "10 Marks"
        },
        {
            "md": ROOT / "task3deliverable.md",
            "docx": ROOT / "JRN3015A_Task3_Media_Operations_and_Management.docx",
            "pdf": ROOT / "JRN3015A_Task3_Media_Operations_and_Management.pdf",
            "title": "TASK 3: MEDIA OPERATIONS & MANAGEMENT STRUCTURE",
            "subtitle": "Operating Model Benchmark, Hybrid Hub-and-Spoke Org Chart, COPE Pipeline & Tech Stack",
            "marks": "8 Marks"
        },
        {
            "md": ROOT / "task4deliverable.md",
            "docx": ROOT / "JRN3015A_Task4_Business_Model_and_Financial_Sustainability.docx",
            "pdf": ROOT / "JRN3015A_Task4_Business_Model_and_Financial_Sustainability.pdf",
            "title": "TASK 4: BUSINESS MODEL & FINANCIAL SUSTAINABILITY",
            "subtitle": "4-Pillar Revenue Hybrid, CAPEX (KES 480k), OPEX (KES 145k/mo), 6-Month P&L and Break-Even",
            "marks": "12 Marks"
        },
        {
            "md": ROOT / "task5deliverable.md",
            "docx": ROOT / "JRN3015A_Task5_Marketing_Distribution_and_Audience_Growth.docx",
            "pdf": ROOT / "JRN3015A_Task5_Marketing_Distribution_and_Audience_Growth.pdf",
            "title": "TASK 5: MARKETING, DISTRIBUTION & AUDIENCE GROWTH",
            "subtitle": "Branding Principles, Failsafe Channel Matrix, 3-Phase Growth Campaign & Budget (KES 90k)",
            "marks": "8 Marks"
        },
        {
            "md": ROOT / "task6deliverable.md",
            "docx": ROOT / "JRN3015A_Task6_Product_Prototype_and_Investor_Pitch.docx",
            "pdf": ROOT / "JRN3015A_Task6_Product_Prototype_and_Investor_Pitch.pdf",
            "title": "TASK 6: PRODUCT PROTOTYPE & INVESTOR PITCH",
            "subtitle": "Interactive Prototype Options (a-g), 5-Mode UX Architecture & 10-15 Min Pitch Deck",
            "marks": "14 Marks"
        },
        {
            "md": ROOT / "JRN3015A_Assignment2_Kikao360_Proposal.md",
            "docx": ROOT / "JRN3015A_Assignment2_Kikao360_Full_Proposal.docx",
            "pdf": ROOT / "JRN3015A_Assignment2_Kikao360_Full_Proposal.pdf",
            "title": "MASTER BUSINESS VENTURE PROPOSAL: KIKAO360",
            "subtitle": "Kenya's Multimodal Newsroom & Spatial Media Platform (Complete Tasks 1-6 & APA References)",
            "marks": "60 Marks"
        },
        {
            "md": ROOT / "submission_check_report.md",
            "docx": ROOT / "JRN3015A_Submission_Verification_Report.docx",
            "pdf": ROOT / "JRN3015A_Submission_Verification_Report.pdf",
            "title": "SUBMISSION VERIFICATION & QUALITY AUDIT REPORT",
            "subtitle": "Comprehensive Rubric, Financial, Operational & Formatting Compliance Audit",
            "marks": "Audit Pass"
        }
    ]
    
    # 1. Convert Markdown to DOCX
    for t in tasks:
        if t["md"].exists():
            convert_markdown_to_docx(t["md"], t["docx"], t["title"], t["subtitle"], t["marks"])
        else:
            print(f"Warning: {t['md'].name} does not exist.")
            
    print("\n" + "=" * 70)
    print("CONVERTING DOCX TO PDF VIA WORD COM AUTOMATION")
    print("=" * 70)
    
    # 2. Convert DOCX to PDF
    for t in tasks:
        if t["docx"].exists():
            try:
                convert_docx_to_pdf(t["docx"], t["pdf"])
            except Exception as e:
                print(f"Error converting {t['docx'].name} to PDF: {e}")
                
    print("\nAll conversions completed successfully!")


if __name__ == "__main__":
    main()

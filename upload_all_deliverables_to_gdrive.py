"""
upload_all_deliverables_to_gdrive.py
Uploads all formatted .docx and .pdf deliverables to the JRN 3015 Google Drive folder:
Folder ID: 1AhIh9y5I-vEsaD8qNDJADSIXEgUrZ2tI
Account: memurugat@gmail.com
"""

import os
import subprocess
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARENT_FOLDER_ID = "1AhIh9y5I-vEsaD8qNDJADSIXEgUrZ2tI"

FILES_TO_UPLOAD = [
    # Task 2
    "JRN3015A_Task2_Market_Research_and_Audience_Analysis.docx",
    "JRN3015A_Task2_Market_Research_and_Audience_Analysis.pdf",
    # Task 3
    "JRN3015A_Task3_Media_Operations_and_Management.docx",
    "JRN3015A_Task3_Media_Operations_and_Management.pdf",
    # Task 4
    "JRN3015A_Task4_Business_Model_and_Financial_Sustainability.docx",
    "JRN3015A_Task4_Business_Model_and_Financial_Sustainability.pdf",
    # Task 5
    "JRN3015A_Task5_Marketing_Distribution_and_Audience_Growth.docx",
    "JRN3015A_Task5_Marketing_Distribution_and_Audience_Growth.pdf",
    # Task 6
    "JRN3015A_Task6_Product_Prototype_and_Investor_Pitch.docx",
    "JRN3015A_Task6_Product_Prototype_and_Investor_Pitch.pdf",
    # Master Proposal (Tasks 1-6 Full)
    "JRN3015A_Assignment2_Kikao360_Full_Proposal.docx",
    "JRN3015A_Assignment2_Kikao360_Full_Proposal.pdf",
    # Submission Verification Report
    "JRN3015A_Submission_Verification_Report.docx",
    "JRN3015A_Submission_Verification_Report.pdf",
]


def upload_file(filename: str):
    filepath = ROOT / filename
    if not filepath.exists():
        print(f"Missing file: {filename}")
        return None
        
    cmd = [
        "gdrive", "mutate", "upload",
        str(filepath),
        "--parent", PARENT_FOLDER_ID
    ]
    env = os.environ.copy()
    env["AGY_ACCOUNT"] = "memurugat@gmail.com"
    
    result = subprocess.run(cmd, env=env, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"FAILED to upload {filename}: {result.stderr.strip()}")
        return None
    else:
        out = result.stdout.strip()
        print(out)
        # Extract ID from output: "Uploaded: filename (ID: 12345)"
        import re
        m = re.search(r'ID:\s*([a-zA-Z0-9_\-]+)', out)
        file_id = m.group(1) if m else "Unknown"
        return {
            "filename": filename,
            "id": file_id,
            "size": filepath.stat().st_size,
            "url": f"https://drive.google.com/file/d/{file_id}/view"
        }


def main():
    print("=" * 70)
    print("UPLOADING FORMATTED DELIVERABLES (.DOCX & .PDF) TO GOOGLE DRIVE")
    print(f"Parent Folder ID: {PARENT_FOLDER_ID}")
    print("=" * 70)
    
    results = []
    # Note: JRN3015A_Task2_Market_Research_and_Audience_Analysis.docx was already uploaded in test, but let's re-record or upload the rest
    for fn in FILES_TO_UPLOAD:
        if fn == "JRN3015A_Task2_Market_Research_and_Audience_Analysis.docx":
            # Already uploaded: ID 13qPF5VtIi8lWVmMnVDrbb2VV2EZwXeWL
            print(f"Already uploaded: {fn} (ID: 13qPF5VtIi8lWVmMnVDrbb2VV2EZwXeWL)")
            results.append({
                "filename": fn,
                "id": "13qPF5VtIi8lWVmMnVDrbb2VV2EZwXeWL",
                "size": (ROOT / fn).stat().st_size,
                "url": "https://drive.google.com/file/d/13qPF5VtIi8lWVmMnVDrbb2VV2EZwXeWL/view"
            })
            continue
            
        res = upload_file(fn)
        if res:
            results.append(res)
            
    # Save upload summary JSON
    with open(ROOT / "drive_upload_summary.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
        
    print("\n" + "=" * 70)
    print("ALL UPLOADS COMPLETED")
    print(f"Total uploaded: {len(results)}/{len(FILES_TO_UPLOAD)}")
    print("=" * 70)


if __name__ == "__main__":
    main()

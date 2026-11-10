import subprocess
import os

GDRIVE_CMD = r"C:\Users\user\.gemini\config\plugins\gdrive\skills\gdrive\scripts\gdrive.cmd"

def check_drive():
    try:
        cmd = [GDRIVE_CMD, "readonly", "recent", "--max", "15"]
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            print("STDERR:", result.stderr)
            print("STDOUT:", result.stdout)
        else:
            print("=== RECENT GOOGLE DRIVE FILES ===")
            print(result.stdout)
    except Exception as e:
        print(f"Error querying gdrive: {e}")

if __name__ == "__main__":
    check_drive()


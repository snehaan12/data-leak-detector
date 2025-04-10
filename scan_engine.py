import os
from utils.extract_text import extract_text
from utils.presidio_scanner import scan_with_presidio
from utils.drive_uploader import upload_to_drive

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def handle_file(file_bytes, filename):
    """
    Save file, extract text, scan for PII, upload if safe.
    """
    file_path = os.path.join(UPLOAD_FOLDER, filename)

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    content = extract_text(file_path)
    findings = scan_with_presidio(content)

    if findings:
        os.remove(file_path)
        return {
            "status": "unsafe",
            "findings": findings
        }

    drive_url = upload_to_drive(file_path, filename)
    os.remove(file_path)

    return {
        "status": "safe",
        "url": drive_url
    }

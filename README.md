# 🔐 Data Leak Detector

A Streamlit-based web app that uploads documents to Google Drive and scans them for sensitive data using NLP tools.

## 🚀 Features

- Upload `.txt`, `.pdf`, etc.
- Auto-upload to Google Drive
- Scan files using [Presidio](https://github.com/microsoft/presidio)
- Extract detected entities like names, emails, phone numbers

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Drive API
- Microsoft Presidio

## 📦 Setup Locally

```bash
git clone https://github.com/snehaan12/data-leak-detector.git
cd data-leak-detector
pip install -r requirements.txt

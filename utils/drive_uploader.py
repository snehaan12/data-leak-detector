import os
import json
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Load from Streamlit secrets
GOOGLE_DRIVE_FOLDER_ID = st.secrets["GOOGLE_DRIVE_FOLDER_ID"]
CREDENTIALS_DICT = json.loads(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"])

def upload_to_drive(local_path: str, filename: str) -> str:
    credentials = service_account.Credentials.from_service_account_info(
        CREDENTIALS_DICT,
        scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': filename,
        'parents': [GOOGLE_DRIVE_FOLDER_ID]
    }
    media = MediaFileUpload(local_path, resumable=True)
    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    return f"https://drive.google.com/file/d/{file.get('id')}/view"

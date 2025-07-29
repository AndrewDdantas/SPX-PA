from dotenv import load_dotenv
import os

load_dotenv()

json_key = {
    "type": os.getenv("GOOGLE_SHEET_TYPE"),
    "project_id": os.getenv("GOOGLE_SHEET_PROJECT_ID"),
    "private_key_id": os.getenv("GOOGLE_SHEET_PRIVATE_KEY_ID"),
    "private_key": os.getenv("GOOGLE_SHEET_PRIVATE_KEY"),
    "client_email": os.getenv("GOOGLE_SHEET_CLIENT_EMAIL"),
    "client_id": os.getenv("GOOGLE_SHEET_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/conex-o-google-sheets%40teste-motoristas.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

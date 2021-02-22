import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import hashlib

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
'https://www.googleapis.com/auth/classroom.coursework.me',
'https://www.googleapis.com/auth/classroom.coursework.students',
#'https://www.googleapis.com/auth/classroom.rosters',
'https://www.googleapis.com/auth/classroom.courses.readonly',
'https://www.googleapis.com/auth/classroom.announcements',
]

class GoogleLogin:
    def login(self, user_id):
        user_bytes = user_id.encode('utf-8')
        user = hashlib.sha256(user_bytes).hexdigest()
        creds = None
        if os.path.exists(f'credentials/tokens/{user}.pickle'):
            with open(f'credentials/tokens/{user}.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'credentials/tokens/{user}.pickle', 'wb') as token:
                pickle.dump(creds, token)
        
        return creds
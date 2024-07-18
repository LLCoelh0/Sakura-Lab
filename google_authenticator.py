import os
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
#Load environment variables from the .env file
load_dotenv()

class GoogleAuthenticator:
    SCOPES = ['https://www.googleapis.com/auth/drive.file']

    def __init__(self, credentials_path_env_var='GOOGLE_CREDENTIALS_PATH', token_file='token.json'):
        self.credentials_path = os.getenv(credentials_path_env_var)
        if not self.credentials_path:
            raise EnvironmentError(f"The environment variable '{credentials_path_env_var}' is not set.")
        self.token_file = token_file
        self.creds = None

    def load_credentials(self):
        #Loads the credentials from the token.json file if it exists
        if os.path.exists(self.token_file):
            self.creds = Credentials.from_authorized_user_file(self.token_file, self.SCOPES)

    def refresh_credentials(self):
        #Attempts to refresh the expired credentials if possible
        if self.creds and self.creds.expired and self.creds.refresh_token:
            self.creds.refresh(Request())

    def authenticate_user(self):
        #Authenticates the user using OAuth 2.0 and saves the credentials
        if not self.creds or not self.creds.valid:
            self.refresh_credentials()
            if not self.creds or not self.creds.valid:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, self.SCOPES)
                self.creds = flow.run_local_server(port=0)
                self.save_credentials()

    def save_credentials(self):
        #Saves the credentials to the token.json file
        with open(self.token_file, 'w') as token:
            token.write(self.creds.to_json())

    def get_credentials(self):
        #Gets the credentials, performing authentication if necessary
        self.load_credentials()
        self.authenticate_user()
        return self.creds
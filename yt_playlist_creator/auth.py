import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# --- CONSTANTS ---
# This is the file that will store the user's credentials after they log in.
TOKEN_PICKLE_FILE = "token.pickle"
# This is the name of the file the user must download from Google Cloud Console.
CLIENT_SECRETS_FILE = "client_secret.json" 
# This defines the permissions our app is requesting.
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    """
    Authenticates the user and returns a YouTube API service object.
    Handles the OAuth 2.0 flow and token storage.
    """
    credentials = None

    # Check if the user has already logged in and we have a token.
    if os.path.exists(TOKEN_PICKLE_FILE):
        print("Loading credentials from file...")
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            credentials = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print("Refreshing access token...")
            credentials.refresh(Request())
        else:
            # Check if the client_secret.json file exists.
            if not os.path.exists(CLIENT_SECRETS_FILE):
                print("\n--- IMPORTANT ---")
                print(f"Error: The credentials file '{CLIENT_SECRETS_FILE}' was not found.")
                print("Please follow the setup instructions in the README.md to download it.")
                print("Place it in the same directory where you are running this command.")
                print("-----------------\n")
                return None
            
            print("Starting new user authentication flow...")
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
            # This will open a browser window for the user to log in.
            credentials = flow.run_local_server(port=0)
            
            # Save the credentials for the next run so they don't have to log in again.
            with open(TOKEN_PICKLE_FILE, 'wb') as token:
                pickle.dump(credentials, token)
                print(f"Credentials saved to '{TOKEN_PICKLE_FILE}' for future use.")

    # Build and return the service object that we can use to make API calls.
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

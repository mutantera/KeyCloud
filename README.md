# Keylogger with Google Drive Upload

## Project Description

This project is a Python-based **keylogger** that logs all keystrokes and uploads the log file to **Google Drive** every hour using the **Google Drive API**. The purpose of this project is educational; it's designed to demonstrate how to combine Python keylogging with cloud services for log management. **Do not use this on any system without explicit permission** from the owner, as it can be illegal and unethical.

---

## Features

- **Keylogging**: Logs every keystroke made by the user and stores it in a text file.
- **Automated Log Uploads**: Uploads the `key_log.txt` file to Google Drive at regular intervals (every hour).
- **OAuth 2.0 Authentication**: Uses Google’s OAuth 2.0 protocol for secure authentication and authorization.
- **Log Management**: Automatically clears the log file after each upload to Google Drive.
- **Cross-platform**: Works on Windows, macOS, and Linux.

---

## Prerequisites

To use this tool, you need:
- Python 3.x installed.
- A Google account with **Google Drive API** enabled.
- A working internet connection.

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/keylogger-with-google-drive.git
cd keylogger-with-google-drive
```

### Step 2: Install Dependencies

You will need to install the required Python libraries using the `requirements.txt` file provided in the repository.

```bash
pip install -r requirements.txt
```

The following dependencies will be installed:
- `pynput` (to capture keyboard input)
- `google-auth` (for handling OAuth 2.0 credentials)
- `google-auth-oauthlib`
- `google-api-python-client`

### Step 3: Set Up Google Drive API

Follow these steps to enable the **Google Drive API** and set up your project credentials.

1. **Go to the Google Cloud Console**:
    - Visit the [Google Cloud Console](https://console.developers.google.com/).
    - Create a new project if you don’t already have one.

2. **Enable the Google Drive API**:
    - In the left-hand sidebar, navigate to **APIs & Services** > **Library**.
    - Search for **Google Drive API** and enable it for your project.

3. **Create OAuth 2.0 Credentials**:
    - Go to **APIs & Services** > **Credentials**.
    - Click **Create Credentials** and select **OAuth 2.0 Client ID**.
    - Choose **Desktop App** as the application type.
    - Download the `credentials.json` file once the credentials are created.

4. **Place `credentials.json` in the Project Directory**:
    - Save the `credentials.json` file in the root of your project directory.

---

## Usage

Once the dependencies are installed and the **Google Drive API** is set up, you can run the keylogger.

### Step 1: Run the Keylogger

Use the following command to run the keylogger:

```bash
python keylogger_drive.py
```

### Step 2: Authenticate with Google

The first time you run the script:
- A browser window will open, asking you to sign in to your Google account.
- Once authenticated, a `token.pickle` file will be created. This file stores your session so you don’t need to re-authenticate each time.

### Step 3: Log Uploading to Google Drive

- The script logs every keystroke to a file called `key_log.txt`.
- Every hour (or the interval you configure), the script uploads the log file to Google Drive.
- After uploading, the log file is cleared to prevent duplicate entries in future uploads.

### Viewing Logs in Google Drive

- Open [Google Drive](https://drive.google.com/) in your browser.
- The uploaded logs will appear as `key_log.txt` in the root directory or the folder you specify in the script.

---

## Google Drive API Setup (Detailed)

### Step 1: Go to Google Cloud Console

1. **Sign in** to the [Google Cloud Console](https://console.developers.google.com/).
2. Create a new project by clicking the **Select Project** dropdown and then **New Project**.
3. Name your project and click **Create**.

### Step 2: Enable Google Drive API

1. In the left-hand menu, click **APIs & Services** > **Library**.
2. In the search bar, type **Google Drive API** and click on it.
3. Click **Enable**.

### Step 3: Create OAuth 2.0 Credentials

1. Navigate to **APIs & Services** > **Credentials**.
2. Click on **Create Credentials** and choose **OAuth 2.0 Client ID**.
3. Under the **Application Type** dropdown, select **Desktop App**.
4. Enter a name for the credentials and click **Create**.
5. Download the `credentials.json` file and place it in your project folder.

### Step 4: Authentication

When you first run the Python script:
- A browser window will open asking you to log in to your Google account.
- This allows the script to gain permission to upload files to your Google Drive.
- After successful login, a file called `token.pickle` will be created. This stores your session, so you won’t need to log in again for future runs.

---

## Configuration

### Modify the Upload Interval

By default, the script uploads the log file to Google Drive every hour (`3600` seconds). To change this interval:
1. Open `keylogger_drive.py`.
2. Locate the line `time.sleep(3600)` and change `3600` to the number of seconds you want.

For example:
- To upload every 30 minutes: `time.sleep(1800)`
- To upload every 10 minutes: `time.sleep(600)`

### Changing the Upload Location in Google Drive

If you want to upload the logs to a specific folder in your Google Drive, you can modify the `upload_to_drive()` function in the script.

---

## Contributing

We welcome contributions! If you'd like to contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they are well-tested.
4. Submit a pull request with a clear explanation of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

## Disclaimer

This tool is for **educational purposes only**. Unauthorized use of this tool may be illegal under your local laws. Always obtain **explicit permission** before using it on any system.

### **Explanation of Each Section**:

1. **Project Description**: Explains what the project does and emphasizes that it’s for educational use only.
2. **Features**: Lists key features such as keylogging, Google Drive uploads, and OAuth 2.0 integration.
3. **Prerequisites**: Lists the required tools and environment.
4. **Installation**: Walks through cloning the repository, installing dependencies, and setting up the Google Drive API.
5. **Usage**: Instructions on how to run the script, authenticate with Google, and how the logs are handled.
6. **Google Drive API Setup**: Step-by-step instructions on how to set up the Google Drive API, create OAuth credentials, and place the `credentials.json` file in the right directory.
7. **Configuration**: Explains how to modify the upload interval and change the log upload location in Google Drive.
8. **Contributing**: Guidelines for how others can contribute to the project.
9. **License**: Specifies that the project is under the MIT License.
10. **Disclaimer**: A reminder that this tool is for educational purposes only.

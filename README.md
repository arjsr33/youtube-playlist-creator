# **YouTube Playlist Creator CLI**

A simple and powerful command-line tool to create a YouTube playlist directly from a text file of songs.

This tool securely authenticates with your own Google Account using OAuth 2.0, searches for each song from your list, and adds the top result automatically to a new playlist.

## **Features**

* **Create** Playlists from a **File**: Instantly turn a simple text file of songs into a YouTube playlist.  
* **YouTube & YouTube Music**: Choose whether to create a standard video playlist or a playlist specifically for YouTube Music.  
* **Secure Authentication**: Uses the official Google OAuth 2.0 flow. Your credentials are stored locally and are never shared.  
* **Customizable**: Set the title, description, and privacy status (public, private, or unlisted) for your new playlist.  
* **Cross-Platform**: Works on Windows, macOS, and Linux.

## **Installation**

This tool is built with Python and can be installed using pip.

1. **Prerequisite**: Ensure you have Python 3.6 or newer installed. You can check by running python \--version.  
2. **Clone the Repository**: First, get the source code from GitHub.  
   git clone https://github.com/arjsr33/youtube-playlist-creator.git
   cd yt-playlist-creator

3. **Install the Tool**: Use pip to install the tool in "editable" mode. This allows you to make changes to the code without needing to reinstall.  
   pip install \-e .

## **Configuration: One-Time Setup (Required)**

Before you can use this tool, you must authorize it to access your YouTube account. This is a **one-time setup** that allows the tool to securely act on your behalf.

#### **Step 1: Set up your Google Cloud Project**

1. Go to the [**Google Cloud Console**](https://console.cloud.google.com/).  
2. Click the project dropdown in the top bar and select **NEW PROJECT**.  
3. Give it a name (e.g., "My YouTube Tools") and click **CREATE**.

#### **Step 2: Enable the YouTube Data API v3**

1. With your new project selected, navigate to the navigation menu (☰) and go to **APIs & Services \> Library**.  
2. Search for YouTube Data API v3 and click on it.  
3. Click the **ENABLE** button.

#### **Step 3: Create Your Credentials**

1. In the navigation menu, go to **APIs & Services \> Credentials**.  
2. Click **\+ CREATE CREDENTIALS** at the top and select **OAuth client ID**.  
3. If this is your first time, you may be prompted to configure the "OAuth consent screen".  
   * Choose **External** for the User Type and click **CREATE**.  
   * Fill in the required fields:  
     * **App name**: YouTube Playlist Creator  
     * **User support email**: Your email address.  
     * **Developer contact information**: Your email address.  
   * Click **SAVE AND CONTINUE** through the rest of the steps. You can leave the "Scopes" and "Test users" sections blank.  
4. Now, back on the "Create OAuth client ID" screen:  
   * For the **Application type**, select **Desktop app**.  
   * Give it a name (e.g., "Playlist Creator CLI").  
5. Click **CREATE**.

#### **Step 4: Download and Place the Credentials File**

1. A window will pop up showing your Client ID. Click the **DOWNLOAD JSON** button.  
2. **VERY IMPORTANT**: Rename the downloaded file to exactly client\_secret.json.  
3. Place this client\_secret.json file in the root of the project directory (the same folder where you ran the pip install command).

You are now fully configured\!

## **Usage**

Once installed and configured, you can run the tool from your terminal. The first time you run it, a browser window will open asking you to log in to your Google Account and grant permission.

**Create a songs.txt file with your song list:**

Eminem \- Till I Collapse  
Kanye West \- Through the Wire  
Linkin Park \- Breaking the Habit  
Imagine Dragons \- Warriors

### **Basic Command (Standard YouTube Playlist)**

This is the simplest way to run the tool. It will create a standard video playlist.

create-playlist \--file songs.txt \--title "My Awesome Playlist"

### **Create a YouTube Music Playlist**

Use the \--type music flag to create a playlist specifically for YouTube Music.

create-playlist \--file songs.txt \--title "My Workout Mix" \--type music

### **Command with All Options**

Here is an example using all available arguments to create a public YouTube Music playlist.

create-playlist \--file "rock\_songs.txt" \--title "My Rock Anthems" \--description "Classic rock hits for the gym." \--privacy public \--type music

### **Arguments**

| Argument | Short Form | Required? | Description |
| :---- | :---- | :---- | :---- |
| \--file | \-f | **Yes** | The path to your text file containing song names, one per line. |
| \--title | \-t | **Yes** | The title for your new playlist. |
| \--description | \-d | No | The description for the playlist. |
| \--privacy | \-p | No | The privacy status: private, public, or unlisted. Defaults to private. |
| \--type |  | No | The platform: youtube or music. Specifies where the playlist is intended for. Defaults to youtube. |

## **License**

This project is licensed under the MIT License. See the [LICENSE](https://github.com/arjsr33/youtube-playlist-creator/blob/main/README.md) file for details.

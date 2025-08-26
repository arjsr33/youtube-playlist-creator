from googleapiclient.errors import HttpError

def create_playlist(youtube, title, description, privacy_status):
    """Creates a new private playlist and returns its ID."""
    try:
        playlist_response = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "title": title,
                    "description": description,
                    "defaultLanguage": "en"
                },
                "status": {
                    "privacyStatus": privacy_status
                }
            }
        ).execute()

        playlist_id = playlist_response["id"]
        print(f"✅ Successfully created playlist: '{title}' (ID: {playlist_id})")
        return playlist_id

    except HttpError as e:
        print(f"❌ An HTTP error {e.resp.status} occurred during playlist creation: {e.content}")
        return None

def search_for_video(youtube, query, platform='youtube'):
    """
    Searches for a video on YouTube and returns the top result's ID.
    If platform is 'music', it prioritizes the music category.
    """
    try:
        # --- UPDATED SEARCH LOGIC ---
        # Base parameters for the search
        search_params = {
            'q': query,
            'part': "snippet",
            'maxResults': 1,
            'type': "video"
        }
        
        # If the user wants a YouTube Music playlist, we add the categoryId for Music.
        if platform == 'music':
            search_params['videoCategoryId'] = '10' # Music category ID
            print("  -> Searching for official music track...")
        else:
            print("  -> Searching for video...")

        # Execute the search with the appropriate parameters
        search_response = youtube.search().list(**search_params).execute()

        videos = search_response.get("items", [])
        if not videos:
            print(f"  -> ⚠️ No video found for query: {query}")
            return None
        
        video_id = videos[0]["id"]["videoId"]
        video_title = videos[0]["snippet"]["title"]
        print(f"  -> Found: '{video_title}'")
        return video_id

    except HttpError as e:
        print(f"  -> ❌ An HTTP error {e.resp.status} occurred during search: {e.content}")
        return None

def add_video_to_playlist(youtube, playlist_id, video_id):
    """Adds a video to a specified playlist."""
    try:
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()
        print(f"  -> ✅ Successfully added video to playlist.")
    except HttpError as e:
        print(f"  -> ❌ An HTTP error {e.resp.status} occurred while adding video: {e.content}")

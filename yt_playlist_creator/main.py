import argparse
import time
from . import auth
from . import playlist

def main():
    """The main function and entry point for the CLI tool."""
    parser = argparse.ArgumentParser(
        description="A CLI tool to create a YouTube playlist from a text file of songs."
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        required=True,
        help="Path to the text file containing the list of songs (one per line)."
    )
    parser.add_argument(
        "-t", "--title",
        type=str,
        required=True,
        help="The title of the new YouTube playlist."
    )
    parser.add_argument(
        "-d", "--description",
        type=str,
        default="Playlist created with yt-playlist-creator CLI.",
        help="The description for the new playlist."
    )
    parser.add_argument(
        "-p", "--privacy",
        type=str,
        choices=['private', 'public', 'unlisted'],
        default='private',
        help="Set the playlist privacy status (private, public, or unlisted)."
    )
    # --- NEW ARGUMENT ---
    parser.add_argument(
        "--type",
        type=str,
        choices=['youtube', 'music'],
        default='youtube',
        help="The platform to create the playlist on. 'youtube' for standard video playlists, 'music' for YouTube Music. Defaults to 'youtube'."
    )

    args = parser.parse_args()

    # --- Start the process ---
    
    # 1. Authenticate
    print("Authenticating with your Google Account...")
    youtube = auth.get_authenticated_service()
    if not youtube:
        print("Authentication failed. Exiting.")
        return

    print("Authentication successful!\n")

    # 2. Create the playlist
    playlist_id = playlist.create_playlist(youtube, args.title, args.description, args.privacy)
    if not playlist_id:
        print("Failed to create playlist. Exiting.")
        return

    # 3. Read songs from the file
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            songs = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Error: The file '{args.file}' was not found.")
        return

    print(f"\nFound {len(songs)} songs in '{args.file}'. Adding them to the playlist...")

    # 4. Search for each song and add it to the playlist
    for i, song_query in enumerate(songs, 1):
        print(f"\n[{i}/{len(songs)}] Processing: {song_query}")
        # Pass the new 'type' argument to the search function
        video_id = playlist.search_for_video(youtube, song_query, args.type)
        if video_id:
            playlist.add_video_to_playlist(youtube, playlist_id, video_id)
            # A small delay to be respectful to the API and avoid rate limiting.
            time.sleep(1) 
    
    # --- UPDATED URL LOGIC ---
    if args.type == 'music':
        playlist_url = f"https://music.youtube.com/playlist?list={playlist_id}"
    else:
        playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
        
    print(f"\n🎉 All done! Your new playlist is ready at:\n{playlist_url}")

if __name__ == '__main__':
    main()

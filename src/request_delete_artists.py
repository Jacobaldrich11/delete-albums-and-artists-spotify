import requests
import time
import os
from dotenv import load_dotenv


# Your OAuth token
load_dotenv()
oauth_token = os.getenv("OAUTH_TOKEN")

# API endpoints
BASE_URL = "https://api.spotify.com/v1"
url_get_followed_artists = f"{BASE_URL}/me/following?type=artist"
url_unfollow_artists = f"{BASE_URL}/me/following?type=artist"

# Headers for the requests
headers = {
    "Authorization": f"Bearer {oauth_token}",
    "Content-Type": "application/json"
}

def get_all_followed_artists():
    artists = []
    after = None
    limit = 50  # Maximum allowed by Spotify API

    while True:
        url = f"{url_get_followed_artists}&limit={limit}"
        if after:
            url += f"&after={after}"
        
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching artists: {response.status_code}")
            print(f"Response: {response.json()}")
            return artists

        data = response.json()
        new_artists = [item['id'] for item in data['artists']['items']]
        artists.extend(new_artists)

        if data['artists']['next'] is None:
            break

        after = data['artists']['cursors']['after']

    return artists

def unfollow_artists(artist_ids):
    for i in range(0, len(artist_ids), 50):  # Spotify API allows unfollowing up to 50 artists at once
        ids = artist_ids[i:i+50]
        response = requests.delete(url_unfollow_artists, headers=headers, json={"ids": ids})
        if response.status_code == 204:
            print(f"Unfollowed artists: {ids}")
        else:
            print(f"Failed to unfollow artists: {ids}, Status code: {response.status_code}")
            print(f"Response: {response.text}")
        
        # Sleep for a short time to avoid rate limiting
        time.sleep(1)

def main():
    followed_artists = get_all_followed_artists()
    print(f"Found {len(followed_artists)} followed artists")

    if followed_artists:
        confirm = input("Are you sure you want to unfollow all these artists? (yes/no): ")
        if confirm.lower() == 'yes':
            unfollow_artists(followed_artists)
            print("Artist unfollowing process completed.")
        else:
            print("Artist unfollowing cancelled.")
    else:
        print("No followed artists found.")

if __name__ == "__main__":
    main()
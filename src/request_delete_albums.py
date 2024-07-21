import requests
import os
from dotenv import load_dotenv

# Your OAuth token
load_dotenv()
oauth_token = os.getenv("OAUTH_TOKEN")

# API endpoints
BASE_URL = "https://api.spotify.com/v1"
url_get_albums = f"{BASE_URL}/me/albums"
url_delete_albums = f"{BASE_URL}/me/albums"

# Headers for the requests
headers = {
    "Authorization": f"Bearer {oauth_token}",
    "Content-Type": "application/json"
}

def get_all_albums():
    albums = []
    offset = 0
    limit = 50  # Maximum allowed by Spotify API

    while True:
        response = requests.get(f"{url_get_albums}?limit={limit}&offset={offset}", headers=headers)
        if response.status_code != 200:
            print(f"Error fetching albums: {response.status_code}")
            return albums

        data = response.json()
        new_albums = [item['album']['id'] for item in data['items']]
        albums.extend(new_albums)

        if len(new_albums) < limit:
            break

        offset += limit

    return albums

def delete_albums(album_ids):
    for i in range(0, len(album_ids), 20):  # Spotify API allows deleting up to 20 albums at once
        ids = album_ids[i:i+20]
        response = requests.delete(url_delete_albums, headers=headers, json={"ids": ids})
        if response.status_code == 200:
            print(f"Deleted albums: {ids}")
        else:
            print(f"Failed to delete albums: {ids}, Status code: {response.status_code}")

def main():
    saved_albums = get_all_albums()
    print(f"Found {len(saved_albums)} saved albums")

    if saved_albums:
        confirm = input("Are you sure you want to delete all these albums? (yes/no): ")
        if confirm.lower() == 'yes':
            delete_albums(saved_albums)
            print("Album deletion process completed.")
        else:
            print("Album deletion cancelled.")
    else:
        print("No albums found to delete.")

if __name__ == "__main__":
    main()
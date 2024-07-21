import base64
import requests
import os
from dotenv import load_dotenv

def main():
    # Your app's credentials
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    # The authorization URL
    auth_url = 'https://accounts.spotify.com/authorize'
    token_url = 'https://accounts.spotify.com/api/token'

    # The redirect URI and desired scope
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'user-library-modify'

    # Step 1: Authorization
    auth_headers = {
        'client_id': client_id,
        'response_type': 'code',
        'redirect_uri': redirect_uri,
        'scope': scope
    }

    print(f"Please visit this URL to authorize your application: {auth_url}?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}")

    # After visiting the URL, you'll be redirected. Copy the 'code' parameter from the redirected URL
    auth_code = input("Enter the code from the redirected URL: ")

    # Step 2: Getting the access token
    encoded_credentials = base64.b64encode(f"{client_id}:{client_secret}".encode('utf-8')).decode("utf-8")
    token_headers = {
        "Authorization": f"Basic {encoded_credentials}",
    }
    token_data = {
        "grant_type": "authorization_code",
        "code": auth_code,
        "redirect_uri": redirect_uri,
    }

    r = requests.post(token_url, headers=token_headers, data=token_data)
    token_response = r.json()

    print(f"Your access token is: {token_response['access_token']}")
    print(f"It will expire in {token_response['expires_in']} seconds")
    
if __name__ == "__main__":
    main()
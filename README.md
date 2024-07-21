# Delete All Albums/Artists Spotify Script

Scripts for deleting all artists and all albums from your Spotify account.

## Steps

1. Install **requests** and (optionally) **dotenv** using `pip install requests dotenv`. Alternatively create a virtual environment.
    - Type and run `python -m venv venv` in your terminal.
    - Activate your virtual environment. On Mac, you type `source venv/bin/activate`. On Windows, you type `./venv/Scripts/activate`.
    - Finally, type `pip install -r requirements.txt` to automatically install the required libraries.
2. Get your access token following the steps [here](https://developer.spotify.com/documentation/web-api).
3. If you cannot get your access token, first create a Spotify app [here](https://developer.spotify.com/dashboard). Then go to the settings of that app, and copy and paste the app's ClientID and ClientSecret in the script `src/access_token.py`. The script will walk you through how to get an access token.
4. Using your access token, run either `src/request_delete_albums.py` or `src/request_delete_artists.py` (or both). Use your token by setting the `oauth_token` variable equal to your respective token. 
5. The script will automatically delete all your albums or all of your artists respectively. Enjoy!

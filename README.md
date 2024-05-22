# Explorify
This program generates personalized Spotify playlists based on songs the user has not listened to from a chosen artist. Explorify enhances the user's music discovery experience by recommending new tracks from their favorite artists that they may have missed

## Files and Scripts

### core.py

Under the hood functions for playlist creation, artist lookup, etc.

### explorify.py

A Spotify API Developer Key is needed for the use of this program. For help in locating this entity please refer to [Obtaining a Spotify API Developer key](#obtaining-a-spotify-api-developer-key).

### template.env

An example `.env` file with the required hidden or sensitive environment variables. The following block is a recreation of the file. When running the programs, please rename the file to `.env`.

```
SPOTIPY_CLIENT_ID = 'yourclientID'
SPOTIPY_CLIENT_SECRET= 'yourclientsecret'
SPOTIPY_CLIENT_REDIRECT_URI = 'https://example.org/callback'
```

### requirements.txt

A standard list of dependencies which can be installed using the following command on terminals:

```
pip install -r requirements.txt
```

## Obtaining a Spotify API Developer key

1. Go to https://developer.spotify.com/ and log into your Spotify account. Navigate to the `Dashboard`.
2. Create an app and fill out the requisite information. While here, add `http://127.0.0.1:5000/redirect` to `Redirect URIs`.
3. Click `Save`, then click your newly created app and navigate to `Settings`.
4. Copy-and-paste your `Client ID` and `Client secret` into your `.env` file (into `CLIENT_ID` and `CLIENT_SECRET` respectively).

For more information, please refer to the [Spotify for Developers Documentation](https://developer.spotify.com/).

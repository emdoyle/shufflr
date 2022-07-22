import spotipy
from spotipy.oauth2 import SpotifyOAuth

from settings import settings

SPOTIFY_SCOPES = " ".join(
    [
        "user-read-private",
        "user-read-currently-playing",
        "user-top-read",
        "user-read-playback-state",
        "user-modify-playback-state",
    ]
)

Spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=settings.SPOTIFY_CLIENT_ID,
        client_secret=settings.SPOTIFY_CLIENT_SECRET,
        redirect_uri=settings.SPOTIFY_REDIRECT_URI,
        scope=SPOTIFY_SCOPES,
    )
)

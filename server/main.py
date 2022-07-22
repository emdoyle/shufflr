from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from spotify import Spotify

app = FastAPI()


@app.get("/auth")
async def auth():
    auth_manager = Spotify.auth_manager
    return RedirectResponse(auth_manager.get_authorize_url())


@app.get("/oauth-callback/")
async def oauth_callback(code: str):
    auth_manager = Spotify.auth_manager
    auth_manager.get_access_token(code)
    return RedirectResponse("http://127.0.0.1:3000/success")


@app.get("/top-songs/")
async def top_songs():
    return Spotify.current_user_top_tracks(time_range="long_term")

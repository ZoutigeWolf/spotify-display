import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from zouti_utils.json import load_json

SCOPES = [
    "user-read-playback-state"
]

config = load_json("config.json")

sp_auth = SpotifyOAuth(
    client_id=config["spotify_client_id"],
    client_secret=config["spotify_client_secret"],
    redirect_uri=config["spotify_redirect_uri"],
    scope=",".join(SCOPES),
    open_browser=config["open_browser"]
)


def fetch_data(client: spotipy.Spotify) -> dict:
    data = client.current_playback()

    progress = data["progress_ms"]
    length = data["item"]["duration_ms"]

    p_min, p_sec = divmod(progress // 1000, 60)
    l_min, l_sec = divmod(length // 1000, 60)

    return {
        "album": data["item"]["album"]["name"],
        "album_img_url": data["item"]["album"]["images"][-1]["url"],
        "track": data["item"]["name"],
        "artists": [a["name"] for a in data["item"]["artists"]],
        "offset": progress % 1000,
        "progress": progress // 1000,
        "progress_formatted": f"{p_min:02}:{p_sec:02}",
        "length": length // 1000,
        "length_formatted": f"{l_min:02}:{l_sec :02}"
    }


def main():
    sp = spotipy.Spotify(auth_manager=sp_auth)
    print("a")

    while True:
        data = fetch_data(sp)
        print(data)
        time.sleep(1 - (data["offset"] / 1000))


if __name__ == "__main__":
    main()
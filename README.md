# spotify-display [WIP]

A Python program to display your current Spotify playing status on an LED matrix.


## Configuration
The program communicates with the Spotify API through a Spotify app.
The credentials for this app are stored in the `config.json` file in the working directory of the program.


#### config.json
```json
{
    "spotify_client_id": "YOUR SPOTIFY APP CLIENT ID",
    "spotify_client_secret": "YOUR SPOTIFY APP CLIENT SECRET",
    "spotify_redirect_uri": "YOUR SPOTIFY APP REDIRECT URI"
}
```
It is recommended to use `http://127.0.0.1:8080` as the redirect uri.

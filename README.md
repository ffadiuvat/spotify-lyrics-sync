
This is a python script to sync lirik with your spotify playback in terminal. This is build by using spotify api to get the playback state and [syair.info](https://syair.info) as the lyric provider

Thanks to this project [https://github.com/TimoLin/SpotifyLyrics](https://github.com/TimoLin/SpotifyLyrics) as the reference for the algorithm to sync the lyrics.

## Features

- Sync Lyrics in Your Terminal

## Tech
- [Python] - Main programming language
- [Spotify API] - To get the playback state

## Installation

You will need to install the dependency in requirements.txt

```
pip install -f requirements.txt
```

Create config.ini file and fill the configuration

```
[spotify]
username = $your-spotify-username
client_id=$client-id-from-spotify-api
client_secret=$client-secret-from-spotify-api

[oauth]
scope=user-read-playback-state
redirect_uri=https://ffadiuvat.github.io/
```

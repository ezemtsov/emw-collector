import sys
import os

import spotipy
import spotipy.util as util

def login(user):
    token = util.prompt_for_user_token(
        username = user,
        scope = 'playlist-read-private',
        client_id = os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret = os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri = 'https://example.com/callback/')
    sp = spotipy.Spotify(token)
    return sp

def read_playlist(sp, user, playlist_id):
    results = sp.user_playlist_tracks(user, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def is_duplicate(sp, user, playlist_id, track_id):
    playlist_tracks = read_playlist(sp, user, playlist_id)
    tracks_ids = list(map(
        lambda x: x["track"]["id"],
        playlist_tracks))
    
    if track_id in tracks_ids:
        return True
    else:
        return False

def add_track(sp, user, playlist_id, track_id):
    if is_duplicate(sp, user, playlist_id, track_id):
        return False
    else:
        results = sp.user_playlist_add_tracks(user, playlist_id, [track_id])
        return True

def search_track(sp,track_request):
    results = sp.track(track_request)
    return results["id"]

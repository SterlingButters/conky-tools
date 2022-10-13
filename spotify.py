import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import json
# https://developer.spotify.com/dashboard/applications/b1ba800ad7064644843e21b675069a6c/users

CLIENT_ID = 'b1ba800ad7064644843e21b675069a6c'
CLIENT_SECRET = 'f9d1f2e2cd694852a0cb81b0dd806906'
SCOPE= 'user-library-read user-read-playback-state user-read-currently-playing user-read-recently-played user-read-playback-position' # https://developer.spotify.com/documentation/general/guides/authorization/scopes/


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback", username='sterlingbutters', scope=SCOPE))

urn = 'spotify:track:0Svkvt5I79wficMFgaqEQJ'

# track = sp.track(urn)
# pprint.pprint(track)

current_track = sp.current_user_playing_track()
print(json.dumps(current_track, indent=4))

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
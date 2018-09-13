import sys
import spotipy
import spotipy.util as util
from pprint import pprint

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print "   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name'])

scope = 'user-library-read'
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    # for item in results['items']:
    #     track = item['track']
    #     print track['name'] + ' - ' + track['artists'][0]['name']

    playlists = sp.current_user_playlists()
    for pl in playlists["items"]:
        if pl["name"] == 'Pop Rising':
            pprint( pl)
            idn = pl["id"]# ["href"]
            results =  sp.user_playlist(username, pl["id"], fields="tracks,next")
            tracks = results['tracks']
            pprint(tracks.keys())
            show_tracks(tracks)
            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)

            for item in tracks["items"]:
                if item["track"]['available_markets'] and "JP" not in item["track"]['available_markets']:
                    pprint(item)
    # tprt = playlists['Top pop rising tracks']
    # print tprt
else:
    print "Can't get token for", username



"""
{u'collaborative': False,
 u'external_urls': {u'spotify': u'https://open.spotify.com/playlist/37i9dQZF1DWUa8ZRTfalHk'},
 u'href': u'https://api.spotify.com/v1/playlists/37i9dQZF1DWUa8ZRTfalHk',
 u'id': u'37i9dQZF1DWUa8ZRTfalHk',
 u'images': [{u'height': 300,
              u'url': u'https://i.scdn.co/image/101383db0cb35237ff23fa531f56f010c62ab230',
              u'width': 300}],
 u'name': u'Pop Rising',
 u'owner': {u'display_name': u'Spotify',
            u'external_urls': {u'spotify': u'https://open.spotify.com/user/spotify'},
            u'href': u'https://api.spotify.com/v1/users/spotify',
            u'id': u'spotify',
            u'type': u'user',
            u'uri': u'spotify:user:spotify'},
 u'primary_color': None,
 u'public': True,
 u'snapshot_id': u'MTUzNTczMTIyNiwwMDAwMDIwZDAwMDAwMTY1OTBiNmQ5NjcwMDAwMDE2NThlZTRiOTU0',
 u'tracks': {u'href': u'https://api.spotify.com/v1/playlists/37i9dQZF1DWUa8ZRTfalHk/tracks',
             u'total': 78},
 u'type': u'playlist',
 u'uri': u'spotify:user:spotify:playlist:37i9dQZF1DWUa8ZRTfalHk'}

"""
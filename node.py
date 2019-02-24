import spotipy
import spotify_ops
from spotify_ops import sp


class Node:
    def __init__(self, artist):
        self.artist = artist
        self.id = artist['id']
        self.radius = self.artist['popularity']
        self.pics = self.artist['images']
        self.url = self.artist['external_urls']['spotify']
        self.collaborators = set()


    def find_collab(self):
        album_ids = spotify_ops.artist_albums_set(self.id)
        for album_id in album_ids:
            track_ids = spotify_ops.album_tracks_set(album_id)
            for track_id in track_ids:
                artist_ids = spotify_ops.track_artists_set(track_id)
                for artist_id in artist_ids:
                    if artist_id != self.id:     # doesn't allow the node artist to be in collaborator set
                        self.collaborators.add(artist_id)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyAuthenticator:
    @staticmethod
    def request_authorization(client_id, client_secret, redirect_uri, scope):
        try:
            return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                             client_secret=client_secret,
                                                             redirect_uri=redirect_uri,
                                                             scope=scope))
        except Exception as e:
            print("Erreur lors de l'initialisation de l'objet Spotify:", e)
            return None

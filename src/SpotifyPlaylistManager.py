


import os
import sys

import pandas as pd 


import json

class SpotifyPlaylistManager:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope

    def main(self, playlist_name, playlist_description, is_public):

        self.sp = SpotifyAuthenticator().request_authorization(self.client_id, self.client_secret, self.redirect_uri,
                                                           self.scope)
        print("Etape 2 : Genrate Tocke Access")
        user_info = self.sp.current_user()
    


if __name__ == "__main__":
    # Charger les variables d'environnement à partir du fichier .env
    load_dotenv()
    client_id = ""
    client_secret = ""
    redirect_uri = ""
    scope = 'user-read-private, playlist-modify-private'

    if client_id == "" or client_secret == "":
        print("Veuillez remplir le fichier .env")
    else:
        if len(sys.argv) < 3:
            print("Il manque des arguments pour l'exécution.")
            print("Exemple d'exécution : python3 file.py <votre_playliste_name> <votre_description_playlist>")
            sys.exit(1)

        # Maintenant, vous pouvez accéder aux arguments comme suit :
        playlist_name = sys.argv[1]
        playlist_description = sys.argv[2]
            
        manager = SpotifyPlaylistManager(client_id, client_secret, redirect_uri, scope)
        manager.main(playlist_name, playlist_description, is_public=False)

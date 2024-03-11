from src.SpotifyPlaylistManager import SpotifyPlaylistManager
from dotenv import load_dotenv
import os
import sys

if __name__ == "__main__":
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    redirect_uri = os.getenv("REDIRECT_URI")
    scope = 'user-read-private, playlist-modify-private'

    if client_id == "" or client_secret == "":
        print("Veuillez remplir le fichier .env")
    else:
        if len(sys.argv) < 3:
            print("Il manque des arguments pour l'exécution.")
            print("Exemple d'exécution : python3 main.py <votre_playliste_name> <votre_description_playlist>")
            sys.exit(1)

        playlist_name = sys.argv[1]
        playlist_description = sys.argv[2]
            
        manager = SpotifyPlaylistManager(client_id, client_secret, redirect_uri, scope)
        manager.main(playlist_name, playlist_description, is_public=False)

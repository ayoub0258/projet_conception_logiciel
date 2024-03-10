from src.SpotifyAuthenticator import SpotifyAuthenticator
from src.SearchTracks import SearchTracks
from src.PDFGenerator import PDFGenerator
import os
import sys
from dotenv import load_dotenv
import pandas as pd
from src.SpotifyPlaylist import SpotifyPlaylist
import json

class SpotifyPlaylistManager:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        load_dotenv()
    def main(self, playlist_name, playlist_description, is_public):

        self.sp = SpotifyAuthenticator().request_authorization(self.client_id, self.client_secret, self.redirect_uri,
                                                           self.scope)
        print("Etape 2 : Genrate Tocke Access")
        user_info = self.sp.current_user()
        token_access = self.lire_token_from_file()


        self.playlist = SpotifyPlaylist(token_access)
        playlist_info = self.playlist.create_playlist(user_info['id'], playlist_name=playlist_name,
                                              playlist_description=playlist_description, is_public=is_public)


        nom_fichier = 'chansons.csv'
        chansons_df = self.lire_csv_chansons(nom_fichier)

        if chansons_df is not None:
            track_uris = []
            for index, chanson in chansons_df.iterrows():
                chanson_info = SearchTracks.get_song_info(chanson['Titre'], token_access)
                if chanson_info:
                    track_uris.append(chanson_info['uri'])

            if track_uris:

                self.playlist.add_items_to_playlist(playlist_info['id'], track_uris)
                items_info = self.playlist.get_playlist_items(playlist_info['id'])
                PDFGenerator.generate_pdf(items_info)
            else:
                print("Aucun URI de piste trouvé.")

    @staticmethod
    def lire_token_from_file(filename='.cache'):
        try:
            with open(filename, 'r') as file:
                token_data = json.load(file)
                return token_data.get('access_token')
        except FileNotFoundError:
            return None

    @staticmethod
    def lire_csv_chansons(nom_fichier):
        print("Etape 4 : Get trucks title from csv file")
        try:
            return pd.read_csv(nom_fichier)
        except FileNotFoundError:
            print("Le fichier spécifié n'a pas été trouvé.")
            return None


if __name__ == "__main__":
    # Charger les variables d'environnement à partir du fichier .env
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
            print("Exemple d'exécution : python3 file.py <votre_playliste_name> <votre_description_playlist>")
            sys.exit(1)

        # Maintenant, vous pouvez accéder aux arguments comme suit :
        playlist_name = sys.argv[1]
        playlist_description = sys.argv[2]
            
        manager = SpotifyPlaylistManager(client_id, client_secret, redirect_uri, scope)
        manager.main(playlist_name, playlist_description, is_public=False)


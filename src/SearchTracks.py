import requests

class SearchTracks:
    @staticmethod
    def get_song_info(song_title, token_access):
        print("Etape 5 : Look for truck in spotify by title")
        url_search_spotify = f"https://api.spotify.com/v1/search?q={song_title}&type=track&limit=1"
        headers = {"Authorization": f"Bearer {token_access}"}
        response = requests.get(url_search_spotify, headers=headers)

        if response.status_code == 200:
            song_info = response.json()
            uri = song_info["tracks"]["items"][0]["uri"]
            song_name = song_info["tracks"]["items"][0]["name"]
            spotify_url = song_info["tracks"]["items"][0]["external_urls"]["spotify"]

            return {
                "name": song_name,
                "uri": uri,
                "spotify_url": spotify_url
            }
        else:
            print("Erreur lors de la récupération des informations sur la chanson.")
            return None

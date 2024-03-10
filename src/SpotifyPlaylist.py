import requests

class SpotifyPlaylist:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    def create_playlist(self, playlist_owner_id, playlist_name, playlist_description="", is_public=False):
        print("Etape 3 : Create PlayList")
        url = f'https://api.spotify.com/v1/users/{playlist_owner_id}/playlists'
        data = {
            "name": playlist_name,
            "description": playlist_description,
            "public": is_public
        }
        headers = {
            'Authorization': 'Bearer ' + self.bearer_token,
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            print("La playlist a été créée avec succès!")
            return response.json()
        else:
            print("Erreur lors de la création de la playlist:", response.status_code)
            print(response.text)
            return None

    def add_items_to_playlist(self, playlist_id, uris, position=None):
        print("Etape 6 : Add tracks to playlist by uris")
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        data = {
            "uris": uris
        }
        if position is not None:
            data["position"] = position

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 201:
            print("Items added to playlist successfully!")
            return response.json()
        else:
            print(f"Error adding items to playlist: {response.status_code}")
            print(response.json())
            return None

    def get_playlist_items(self, playlist_id):
        print("Etape 7 : Look for trucks in playlist")
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {
            "Authorization": f"Bearer {self.bearer_token}"
        }
        params = {
            "limit": 50
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            tracks_info = []

            items = data.get('items', [])
            for item in items:
                track_info = item.get('track', {})
                track_name = track_info.get('name')
                release_date = track_info.get('album', {}).get('release_date')
                spotify_url = track_info.get('external_urls', {}).get('spotify')

                artists = track_info.get('artists', [])
                artist_names = ', '.join([artist.get('name') for artist in artists])

                track_data = {
                    'name': track_name,
                    'release_date': release_date,
                    'spotify_url': spotify_url,
                    'artist_name': artist_names
                }
                tracks_info.append(track_data)

            return tracks_info
        else:
            print(f"Erreur lors de la récupération des éléments de la playlist: {response.status_code}")
            return None

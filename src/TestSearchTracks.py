import unittest
from unittest.mock import patch
from SearchTracks import SearchTracks

class TestSearchTracks(unittest.TestCase):
    @patch('SearchTracks.requests.get')
    def test_get_song_info_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "tracks": {
                "items": [
                    {
                        "uri": "spotify:track:abc123",
                        "name": "Test Song",
                        "external_urls": {
                            "spotify": "https://open.spotify.com/track/abc123"
                        }
                    }
                ]
            }
        }

        song_title = "Test Song"
        token_access = "mock_token"
        expected_result = {
            "name": "Test Song",
            "uri": "spotify:track:abc123",
            "spotify_url": "https://open.spotify.com/track/abc123"
        }
        result = SearchTracks.get_song_info(song_title, token_access)
        self.assertEqual(result, expected_result)

    @patch('SearchTracks.requests.get')
    def test_get_song_info_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        song_title = "Nonexistent Song"
        token_access = "mock_token"
        result = SearchTracks.get_song_info(song_title, token_access)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

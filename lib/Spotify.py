import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import string


class Spotify():
    """
    Custom python class that leverages the spotipy python package to interface the spotify API and perform custom actions and data manipulations
    """

    def __init__(self, client_id, client_secret):
        """
        Create's an instance of the custom Spotify class. For this application, no user data is required, this only the client crednetials flow is necessary.

        :param client_id: a valid Client ID obtained from Spotify's developer dashboard
        :param client_secret: a valid Client Secret obtained from Spotify's developer dashboard
        "
        """
        self._client_id = client_id
        self._client_secret = client_secret
        self._spotify = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=self._client_id,
                client_secret=self._client_secret))

    def get_random_song(self):
        """
        This function will be used to get a random track from the Spotify API.

        I am folloiwng the generic model laid out in this medium article: https://medium.com/@perryjanssen/getting-random-tracks-using-the-spotify-api-61889b0c0c27

        Steps involved:
        1.) generate a random character
        2.) randomly decide to either a.) place wildcard after character, OR b.) wrap character in wildcards
        3.) genearte random offset page to select from

        :return track: a track object from the spotify API
        """
        char = random.choice(string.ascii_lowercase)
        wild_choice = random.choice([0, 1])
        offset = random.choice(range(2000))

        if wild_choice:
            q = char + '%'
        else:
            q = '%' + char + '%'

        return self._spotify.search(q, limit=1, offset=offset, type='track')['tracks']['items'][0]


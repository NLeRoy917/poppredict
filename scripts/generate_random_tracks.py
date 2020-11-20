import os
import sys
sys.path.append('..')

from lib.Spotify import Spotify

from dotenv import load_dotenv
load_dotenv()

sp = Spotify(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

tracks = []
for i in range(5):
    tracks.append(sp.get_random_song())

for track in tracks:
    print(track['name'],'|',track['artists'][0]['name'])
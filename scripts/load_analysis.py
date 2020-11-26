from dotenv import load_dotenv
from progress.bar import Bar
import os
import argparse
import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from spotify.Spotify import Spotify

parser = argparse.ArgumentParser(description='Load track data into the db')
parser.add_argument('--db', dest='db', default='../data.db',
                    help='Path to database file for sqlite')
args = parser.parse_args()

load_dotenv()

sp = Spotify(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
sql = SqlClient(db_file=args.db)

def chunk_tracks(tracks, n=100):
    """
    Chunk a list of tracks into groups of n.

    :param n: - The number to chunk into
    """
    i = 0
    chunk = []
    chunks = []
    for track in tracks:
        # once we reach chunk size, n, store into chunks and reset
        if i == n:
            chunks.append(chunk)
            i = 1
            chunk = []
        chunk.append(track)
        i += 1
    
    return chunks

if __name__ == '__main__':
    tracks = sql.get_all_tracks()
    feature_bar = Bar('Analyzing tracks...', max=len(tracks))
    tracks_chunked = chunk_tracks(tracks)
    features_full = []
    for chunk in tracks_chunked:
        ids = [t['ID'] for t in chunk]
        features_chunk = sp.audio_features(ids)
        for feature in features_chunk:
            try:
                sql.insert_analysis(uri=feature['uri'],
                                    id=feature['id'],
                                    acousticness=feature['acousticness'],
                                    danceability=feature['danceability'],
                                    duration_ms=feature['duration_ms'],
                                    energy=feature['energy'],
                                    instrumentalness=feature['instrumentalness'],
                                    key=feature['key'],
                                    liveness=feature['liveness'],
                                    loudness=feature['loudness'],
                                    mode=feature['mode'],
                                    speechiness=feature['speechiness'],
                                    tempo=feature['tempo'],
                                    time_signature=feature['time_signature'],
                                    valence=feature['valence'])
                feature_bar.next()
            except:
                continue
    
    feature_bar.finish()
                

    


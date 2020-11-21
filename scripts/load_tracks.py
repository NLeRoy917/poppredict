from dotenv import load_dotenv
from progress.bar import Bar
import os
import argparse
import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from spotify.Spotify import Spotify

parser = argparse.ArgumentParser(description='Load track data into the db')
parser.add_argument('--db', dest='db', default='data.db',
                    help='Path to database file for sqlite')
parser.add_argument('-n', dest='n', required=True, type=int,
                    help='Number of random tracks to store in database')
args = parser.parse_args()


load_dotenv()

sp = Spotify(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
sql = SqlClient(db_file=args.db)

id_gen_bar = Bar('Finding tracks...', max=args.n)
for i in range(args.n):
    try:
        track = sp.get_random_song()
        sql.insert_track(
            name=track['name'],
            artist=track['artists'][0]['name'],
            uri=track['uri'],
            id=track['id'],
            href=track['href'],
            popularity=track['popularity'])
    except KeyboardInterrupt:
        print('Stopping ...')
        sys.exit(0)
    except:
        continue
    id_gen_bar.next()
id_gen_bar.finish()

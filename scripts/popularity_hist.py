import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from spotify.Spotify import Spotify

sql = SqlClient(db_file='../data.db')

pop_data = sql.popularity_data()

plt.hist(pop_data, bins=30, facecolor='grey')
plt.title('Spotify Song Popularity Distribution (n={})'.format(len(pop_data)))
plt.xlabel('Popularity')
plt.ylabel('Count')
plt.show()


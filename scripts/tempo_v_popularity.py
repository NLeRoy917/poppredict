import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('..')

from sql.SQLite import SqlClient
from utils.Utils import Utils

utils = Utils()
sql = SqlClient(db_file='data.db')

tempo_pop = sql.tempo_pop_data()

tempo_x = []
tempo_y = []
for datapoint in tempo_pop:
    tempo_x.append(datapoint['Tempo'])
    tempo_y.append(datapoint['Popularity'])

plt.scatter(tempo_x, tempo_y, s=1, color='k')
plt.title('Tempo v Popularity')
plt.xlabel('Tempo')
plt.ylabel('Popularity')
plt.show()
import tensorflow as tf

from poppredict import PopPredict
from sql import SQLite

sql = SQLite.SqlClient(db_file='data.db')
pp = PopPredict.PopPredict(path='./model/')

pp.summary()
for i in range(100):
    random = sql.get_random_datapoint()
    inputs = random[:-1]
    popularity = random[-1]
    pop_predict = pp.predict(tf.expand_dims(inputs, axis=0))[0][0]
    # err = round((popularity-pop_predict)/popularity*100,2)
    # print('Real:',str(int(popularity)).ljust(3), '| ', 'Prediction:', str(int(pop_predict)).ljust(4), '| ', 'Err:', str(err).ljust(3),'%')
    print('Real:',str(int(popularity)).ljust(3), '| ', 'Prediction:', str(int(pop_predict)).ljust(4))





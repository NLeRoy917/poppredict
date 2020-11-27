import sys
sys.path.append('../')

from poppredict import PopPredict
from sql import SQLite


sql = SQLite.SqlClient(db_file='../data.db')
pp = PopPredict.PopPredict()
x_train, y_train, x_valid, y_valid = sql.get_training_validation_data()
pp.compile()
pp.fit(x_train, y_train, epochs=500, batch_size=32)
pp.save('../model')
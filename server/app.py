# import flask
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from flask import send_from_directory
from flask_cors import CORS
app = Flask(__name__, static_folder='./dist')
CORS(app)

##
# API routes
##

@app.route('/api/items')
def items():
  '''Sample API route for data'''
  return jsonify([{'title': 'A'}, {'title': 'B'}])

##
# View route
##

# Testing route/main route
@app.route('/')
def base():
	return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
	app.run()
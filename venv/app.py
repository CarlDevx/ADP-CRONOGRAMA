from flask import Flask, render_template
app = Flask(__name__)
import  firebaseAPI
import bd
firebase_url = "https://andatabaseteste-default-rtdb.firebaseio.com/"
firebase_route = 'Cronograma.json'

@app.route('/')
def index():
#	data = firebaseAPI.getData(firebase_url, firebase_route)
#	databaseJson = firebaseAPI.unpackData(data)
#	databaseList = firebaseAPI.mountTag(databaseJson)
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)

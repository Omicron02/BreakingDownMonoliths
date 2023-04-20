from flask import Flask
from flask_restful import Resource, Api
import math

class gcd(Resource): 
	def get(self, num1, num2):
		return {'result': math.gcd(int(num1), int(num2))}

app = Flask(__name__)
api = Api(app)
api.add_resource(gcd, '/<int:num1>/<int:num2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5057,
		host="0.0.0.0"
	)

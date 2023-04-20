from flask import Flask
from flask_restful import Resource, Api

class exp(Resource): 
	def get(self, num1, num2):
		return {'result': int(num1) ** int(num2)}

app = Flask(__name__)
api = Api(app)
api.add_resource(exp, '/<int:num1>/<int:num2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5056,
		host="0.0.0.0"
	)

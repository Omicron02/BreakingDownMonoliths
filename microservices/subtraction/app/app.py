from flask import Flask
from flask_restful import Resource, Api

class sub(Resource): 
	def get(self, num1, num2):
		return {'result': int(num1) - int(num2)}

app = Flask(__name__)
api = Api(app)
api.add_resource(sub, '/<int:num1>/<int:num2>')

if __name__ =="__main__":
	app.run(
		debug=True,
		port=5052,
		host="0.0.0.0"
	)
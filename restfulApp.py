#Required imports
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

#initialise app and Api constructors
app = Flask(__name__)
api = Api(app)

#define the resources
class Add(Resource):
  pass
class Subtract(Resource):
  pass

class Multiply(Resource):
  pass

class Divide(Resource):
  pass

#run the main application
if __name__ == "__main__":
  app.run(debug=True)
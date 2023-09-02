#Required imports
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

#initialise app and Api constructors
app = Flask(__name__)
api = Api(app)

#define the resources
class Add(Resource):
  #define post and get methods
  def post(self):
    #handles resources add requested using method POST
    #STEP 1: Get posted data
    postedData =  request.get_json()
    x = int(postedData['x'])
    y = int(postedData['y'])
    #STEP2: perform computation and prepare return data
    ret = x+y 
    retMap = {
      'Message':ret,
      'Status Code':200
    }
    #STEP3: return data
    return jsonify(retMap)
    
  ''' 
  THESE ARE ONLY HERE TO DEMO HOW HANDLERS FOR OTHER METHODS WOULD BE IMPLEMENTED
  def get(self):
    #handles resources add requested using method GET
    pass
  def put(self):
    pass
  def delete(self):
    pass
 '''
class Subtract(Resource):
  pass

class Multiply(Resource):
  pass

class Divide(Resource):
  pass

#Map resource to an end point
api.add_resource(Add, "/add")

#run the main application
if __name__ == "__main__":
  app.run(debug=True)
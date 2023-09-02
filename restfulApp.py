#Required imports
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

#initialise app and Api constructors
app = Flask(__name__)
api = Api(app)

#posted data validity checker
def checkPostedData(PostedData, functionName):
  if functionName in("add", "sub", "mult", ):
    if "x" not in PostedData or "y" not in PostedData:
      return 301
    else:
      return 200
  elif functionName =="div":
    if "x" not in PostedData or "y" not in PostedData:
      return 301
    elif PostedData["y"] ==0:
      return 302
    else:
      return 200
#generalise the handle post request method
def handle_post_request(postedData, operation):
    status_code = checkPostedData(postedData, operation)
    if status_code != 200:
        retJson = {
            'Message': "An Error happened",
            'Status Code': status_code
        }
        return jsonify(retJson)
    else:
        x = int(postedData['x'])
        y = int(postedData['y'])
        result = None

        if operation == "add":
            result = x + y
        elif operation == "sub":
            result = x - y
        elif operation == "mult":
            result = x * y
        elif operation == "div":
            result = x / y

        retMap = {
            'Message': result,
            'Status Code': 200
        }
        return jsonify(retMap)

#define the resources
class Add(Resource):
  #define post and get methods
  def post(self):
  #   #handles resources add requested using method POST
  #   #STEP 1a: Get posted data
  #   postedData =  request.get_json()
  #   #STEP 1b: Verify validity of posted data
  #   status_code = checkPostedData(postedData, "add")
  #   if status_code !=200:
  #     retJson={
  #        'Message':"An Error happened",
  #       'Status Code':status_code
  #     }
  #     return jsonify(retJson)
  #   else:
  #     x = int(postedData['x'])
  #     y = int(postedData['y'])
  #     #STEP2: perform computation and prepare return data
  #     ret = x+y 
  #     retMap = {
  #       'Message':ret,
  #       'Status Code':200
  #     }
  #     #STEP3: return data
  #     return jsonify(retMap)
    postedData = request.get_json()
    return handle_post_request(postedData, 'add')
  
 
  def get(self):
        return "This is the GET endpoint for Subtract resource"

  '''THESE ARE ONLY HERE TO DEMO HOW HANDLERS FOR OTHER METHODS WOULD BE IMPLEMENTED
  def put(self):
    pass
  def delete(self):
    pass
 '''
class Subtract(Resource):
  def post(self):
    postedData = request.get_json()
    return handle_post_request(postedData, 'sub')
class SubtractGet(Resource):
  def get(self):
      #handles resources add requested using method GET
      return "This is the GET endpoint for Subtract resource"
class Multiply(Resource):
  def post(self):
    postedData = request.get_json()
    return handle_post_request(postedData, 'mult')  
class Divide(Resource):
  def post(self):
    postedData = request.get_json()
    return handle_post_request(postedData, 'div') 

#Map resource to an end point
api.add_resource(Add, "/add")
api.add_resource(Subtract,'/sub')
api.add_resource(SubtractGet, '/sub/get')
api.add_resource(Multiply, "/mult")
api.add_resource(Divide,'/div')

#run the main application
if __name__ == "__main__":
  app.run(debug=True)
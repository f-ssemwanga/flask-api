#Required imports
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient #mongo db import


#initialise app and Api constructors
app = Flask(__name__)
api = Api(app)

#initialise mongoclient to the point to the build db in docker
#add the default port for mongodb
client = MongoClient("mongodb://db:27017")

#create a database
db = client.aNewDB
#create a collection
UserNum = db["UserNum"]
#insert one document if it doesnot exist
if UserNum.count_documents({}) ==0:
  UserNum.insert_one({
  'num_of_users':0
})

#create a resource i.e. class to increment number of users visiting my application
class Visit(Resource):
  def get(self):
    #get previous no of visitors
    prev_num = UserNum.find({})[0]['num_of_users']
    #increment previous
    visitor_num = prev_num +1
    #update the no of visitors in the database
    UserNum.update_one({}, {"$set":{'num_of_users':visitor_num}})
    return f'Hello user, {visitor_num}'
  


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
api.add_resource(Visit, '/greet')

#run the main application
if __name__ == "__main__":
  app.run(host='0.0.0.0')
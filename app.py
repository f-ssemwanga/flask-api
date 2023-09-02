#basic web service in flask
from flask import Flask, request, jsonify
app = Flask(__name__)
#127.0.0.1:5000/

''''Different  end points'''

@app.route('/')
def first_app():
  return 'first App'
@app.route('/route1')
def listen_route1():
  return 'response at route 1'
@app.route('/jsonRoute')
def json_route():
  age =int(input('Enter your age: '))
  some_json={'name':'Francis',
             'age':age,
             "phones":[
               {
                 "phoneName": "Iphone 10",
                 "PhoneNumber":123344
               },
               {
                 "phoneName":'Nokia',
                 "PhoneNumber":1772882
               }
             ]
             }
  return some_json
#End post for post request
#by default all routes support GET  i.e. @app.route('/jsonRoute', methods=['GET'])
#to accept post requests we override that as show below
@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
  #get x, y from the posted data - get posted data from the request
  dataDict = request.get_json()
  #check if x and y are present in the JSON data
  if 'x' in dataDict and 'y' in dataDict:
    x = dataDict['x']
    y = dataDict['y']
    
    #add z= x+y
    z = x+y
    #return the jason
    return jsonify({"z":z}), 200
  else:
    return jsonify({'Error':"Missing 'x' or 'y' in json request"}), 400

'''Start running Server'''

if __name__ == "__main__":
  #pass debug=True  to see the errors
  #we however normally pass the host server to app.run()
  #i.e. host="127.0.0.1", port 80
  app.run(debug=True)
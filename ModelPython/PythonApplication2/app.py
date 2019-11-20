from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


variables = [{'name': 'Fzm', 'value': 10.0 },
			 {'name': 'To', 'value' : -5.0},
			 {'name': 'Tpco', 'value': 27.0},
			 {'name': 'Tpm', 'value': 0.0},
			 {'name': 'Tzco', 'value': 0.0},
			 {'name': 'Tzm', 'value': 97.5}]
			 
			 
			 
				
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/variables', methods=['GET'])
def returnAll():
    return jsonify({'variables' : variables})

@app.route('/variables/<string:name>', methods=['GET'])
def returnOne(name):
    theOne = variables[0]
    for i,q in enumerate(variables):
      if q['name'] == name:
        theOne = variables[i]
    return jsonify({'variables' : theOne})

@app.route('/variables', methods=['POST'])
def addOne():
    variables = request.get_json()
    variables.append(variables)
    return jsonify({'variables' : variables})

@app.route('/variables/<string:name>', methods=['PUT'])
def editOne(name):
    new_variables = request.get_json()
    for i,q in enumerate(variables):
      if q['name'] == name:
        variables[i] = new_variables    
    qs = request.get_json()
    return jsonify({'variables' : variables})

@app.route('/variables/<string:name>', methods=['DELETE'])
def deleteOne(name):
    for i,q in enumerate(variables):
      if q['name'] == name:
        del variables[i]  
    return jsonify({'variables' : variables})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

regulation = [{'Fzm': 30,'U':1}] #to będzie pobierał od nas moduł 6
Tpm = [{'Tpm': 0}] #tak samo
dostawca = [{'T_o':0,'T_zm':70}]
budynek1 = [{'Tpco':20,'Fzm':2}]
budynek2 = [{'Tpco':20,'Fzm':2}]
budynek3 = [{'Tpco':20,'Fzm':2}]
#methods			 
@app.route('/dostawca', methods=['GET'])
def getdostawca():
    return jsonify({'dostawca' : dostawca})

@app.route('/regulation', methods=['PUT'])
def editregulation():
    new_Tzco = request.get_json()
    Tzco[0] = new_Tzco   
    qs = request.get_json()
    return jsonify({'regulation':regulation}) 

@app.route('/budynek1', methods=['GET'])
def getbud1o():
    return jsonify({'budynek1' : budynek1})
@app.route('/budynek2', methods=['GET'])
def getbud2():
    return jsonify({'budynek2' : budynek2})
@app.route('/budynek3', methods=['GET'])
def getbud3():
    return jsonify({'budynek3' : budynek3})

if __name__ == "__main__":
    app.run(debug=True)


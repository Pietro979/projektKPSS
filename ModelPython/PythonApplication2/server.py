from flask import Flask
from flask import jsonify
from flask import request
import requests
app = Flask(__name__)

start = [{}]  #metoda put do modułu czasowego 
time  = [{"speed":0,"symTime" : "2019-11-18+18:40:15" }]  #metoda put do modułu czasowego
Tzco = [{"Tzco": 0}] #to będzie pobierał od nas moduł 6
Tpm = [{"Tpm": 0}] #tak samo
impuls = [{"impuls": 0}]
#methods			 
@app.route('/Tzco', methods=['GET'])
def getTzco():
    return jsonify({'Tzco' : Tzco})

@app.route('/Tpm', methods=['GET'])
def getTpm():
    res = requests.put("http://127.0.0.1:5000/Tzco",json={'Tzco':2137})
    return jsonify({'Tpm' : Tpm})

@app.route('/Tpm', methods=['PUT'])
def editTpm():
    new_Tpm = request.get_json()
    Tpm[0] = new_Tpm    
    qs = request.get_json()
    return jsonify({}) 
@app.route('/Tzco', methods=['PUT'])
def editTzco():
    new_Tzco = request.get_json()
    Tzco[0] = new_Tzco    
    qs = request.get_json()
    return jsonify({}) 

@app.route('/start', methods=['GET'])
def getStart():
    return jsonify({'start' : start})

@app.route('/time', methods=['GET'])
def getTime():
    return jsonify({'time' : time})

@app.route('/impuls', methods=['GET'])
def getimpuls():
    return jsonify({'impuls' : impuls})

@app.route('/impuls', methods=['PUT'])
def editimpuls():
    new_impuls = request.get_json()
    impuls[0] = new_impuls    
    qs = request.get_json()
    return jsonify({})  

@app.route('/time', methods=['PUT'])
def editTime():
    new_time = request.get_json()
    time[0] = new_time    
    qs = request.get_json()
    impuls = {"impuls": 1}
    return jsonify({})       
       
@app.route('/start', methods=['PUT'])
def editStart():
    new_start = request.get_json()
    start[0] = new_start    
    qs = request.get_json()
    impuls[0] = {"impuls": 1}
    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)


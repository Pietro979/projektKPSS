from flask import Flask
from flask import jsonify
from flask import request
import time
app = Flask(__name__)

#Constants
Mm = 3000;          #Masa wymiennika po stronie pierwotnej
Mco = 3000;         #Masa wymiennika po stronie wtornej

cwym = 2700;        #zastepcze cieplo wlasciwe wymiennika
ro = 1000;          #gestosc wody
cw = 4200;          #cieplo wlasciwe wody
kw = 250000;        #wspolczynnik przenikania ciepla
Fzco = 40;
#endpoints
start = [{"speed":0,"symTime" : "2019-11-18+18:40:15" }]  #metoda put do modułu czasowego 
timeS  = [{"speed":0,"symTime" : "2019-11-18+18:40:15" }]  #metoda put do modułu czasowego

Tzco = [{"Tzco": 0}] #to będzie pobierał od nas moduł 6
Tpm = [{"Tpm": 0}] #tak samo
			 
@app.route('/timeS', methods=['PUT'])
def editTimeS():
    new_time = request.get_json()
    timeS[0] = new_time    
    qs = request.get_json()
    return jsonify({})			 
			 
@app.route('/start', methods=['PUT'])
def editStart():
    new_start = request.get_json()
    start[0] = new_start    
    qs = request.get_json()
    return jsonify({})

@app.route('/Tzco', methods=['GET'])
def getTzco():
    return jsonify({'Tzco' : Tzco})

@app.route('/Tpm', methods=['GET'])
def getTpm():
    return jsonify({'Tpm' : Tpm})

@app.route('/start', methods=['GET'])
def getStart():
    return jsonify({'start' : start})

@app.route('/timeS', methods=['GET'])
def getTime():
    return jsonify({'timeS' : timeS})

if __name__ == "__main__":
    app.run(debug=True)

def Tpmf(Fzm,ro,cw,Tzm,Tpm,Tzco,Mm,cwym): #zwraca Tpm[i+1]
  difference = ((Fzm*ro*cw*(Tzm - Tpm)) - (kw * (Tpm - Tzco)) )/ (Mm*cwym)
  return (difference*d)+Tpm

def Tzcof(Fzco,ro,cw,Tzco,Tpco,kw,Tpm,Mco,cwym): #zwraca Tzco[i+1]
  difference = ((-Fzco) * ro*cw*(Tzco - Tpco) + kw * (Tpm - Tzco))/(Mco*cwym)
  return (difference*d)+Tzco;

#Variables
Fzm = 1;          #Strumien ogrzanej wody od 0 do ok. 22
To = -5;          #Temperatura zewnetrzna
Tpco = 27;          #Temperatura wody wyplywajacej z budynku
Fzco = 10;          #nie wiem xd
Tzm = 70 - 2.5*(To - 6);  #strumien ogrzanej wody
d = 0.05

module3_address = "http://127.0.0.1:5000"
module5_address = "http://127.0.0.1:5000"
module61_address = "http://127.0.0.1:5000"
module62_address = "http://127.0.0.1:5000"
module63_address = "http://127.0.0.1:5000"

while(1):
############
  #dwa requesty do modulu 3

  #res = requests.get(module3_address + "/To")
  #data = res.json()
  #To = data[0]['To']

  #res = requests.get(module3_address + "/Tzm")
  #data = res.json()
  #Tzm = data[0]['Tzm']

###########
  #jeden request do modułu 5, w tym requescie wysyłamy im wartość Tzco

  #res = requests.get(module5_address + "/Fzm")
  #res.json()
  #data = res.json()
  #Fzm = data[0]['Fzm']

##########
  #3requesty do modułu 6, do każdego budynk osobno

  #res = requests.get(module61_address + "/Tpco")
  #data = res.json()
  #Tpco1 = data[0]['Tpco']

  #res = requests.get(module62_address + "/Tpco")
  #data = res.json()
  #Tpco2 = data[0]['Tpco']

  #res = requests.get(module63_address + "/Tpco")
  #data = res.json()
  #Tpco3 = data[0]['Tpco']  

  #Tpco = (Tpco1+Tpco2+Tpco3)/3 #tutaj ma być chyba średnia ważona 

Tpm[0]['Tpm'] = Tpmf(Fzm, ro, cw, Tzm, Tpm[0]['Tpm'], Tzco[0]['Tzco'], Mm, cwym)
Tzco[0]['Tzco'] = Tzcof(Fzco, ro, cw, Tzco[0]['Tzco'], Tpco, kw, Tpm[0]['Tpm'], Mco, cwym)
print({'Tzco' : Tzco})
time.sleep(10)

  #no i w sumie nie wiem czy my mamy to wysyłać do loggera czy gdziś, czy on sam sobie weźmie
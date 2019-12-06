from flask import Flask
from flask import json
#from flask import request
import requests
Mm = 3000;          #Masa wymiennika po stronie pierwotnej
Mco = 3000;         #Masa wymiennika po stronie wtornej

cwym = 2700;        #zastepcze cieplo wlasciwe wymiennika
ro = 1000;          #gestosc wody
cw = 4200;          #cieplo wlasciwe wody
kw = 250000;        #wspolczynnik przenikania ciepla
Fzco = 60;
String sim_time;
#Variables
Fzm = 10          #Strumien ogrzanej wody od 0 do ok. 22
To = 20          #Temperatura zewnetrzna
Tpco = 30          #Temperatura wody wyplywajacej z budynku
Fzco = 20          #nie wiem xd
Tzm = 70 - 2.5*(To - 6);  #strumien ogrzanej wody
d = 0.01
Tzco = [{"Tzco": 0}] #to będzie pobierał od nas moduł 6
Tpm = [{"Tpm": 0}] #tak samo
#adress
ur_address = "http://127.0.0.1:5000"
module3_address = "http://72e859c9.ngrok.io"
module5_address = "http://d2e5f426.ngrok.io"
module61_address = "http://b9d02260.ngrok.io"
module62_address = "http://5f1ec98c.ngrok.io"
module63_address = "http://18585e2a.ngrok.io"
#endpoints


#differentials
def Tpmf(Fzm,ro,cw,Tzm,Tpm,Tzco,Mm,cwym): #zwraca Tpm[i+1]
  difference = ((Fzm*ro*cw*(Tzm - Tpm)) - (kw * (Tpm - Tzco)) )/ (Mm*cwym)
  return (difference*d)+Tpm

def Tzcof(Fzco,ro,cw,Tzco,Tpco,kw,Tpm,Mco,cwym): #zwraca Tzco[i+1]
  difference = ((-Fzco) * ro*cw*(Tzco - Tpco) + kw * (Tpm - Tzco))/(Mco*cwym)
  return (difference*d)+Tzco;

def calculate(Mm, Mco,cwym,ro,cw,kw,Fzco):
  #dwa requesty do modulu 3
  
  '''res = requests.get(module3_address+"/dostawca")
  data = res.json()
  To = data['dostawca'][0]['T_o']

  res = requests.get(module3_address+"/dostawca")
  data = res.json()
  Tzm = data['dostawca'][0]['T_zm']'''

  ###########
  #jeden request do modułu 5, w tym requescie wysyłamy im wartość Tzco
  res = requests.put(module5_address+"/regulation",json = {'Tzco':Tzco[0]['Tzco']})
  data = res.json()
  Fzm = data['Fzm']
 

  ##########
  #3requesty do modułu 6, do każdego budynk osobno

  '''res = requests.get(module61_address + "/data")
  data = res.json()
  Tpco1 = data['T_pcob']
  Fcob1 = data['F_cob']'''

  res = requests.get(module62_address + "/data")
  data = res.json()
  Tpco2 = data['T_pcob']
  Fcob2 = data['F_cob']

  res = requests.get(module63_address + "/data")
  data = res.json()
  Tpco3 = data['T_pcob']
  Fcob3 = data['F_cob']

  '''res = requests.get(module61_address + "/Fcob")
  data = res.json()['Fcob']
  sim_time=data[0]['time']
  Fcob1 = data[0]['Fcob']
  res = requests.get(module62_address + "/Fcob")
  data = res.json()['Fcob']
  Fcob2 = data[0]['Fcob']
  res = requests.get(module63_address + "/Fcob")
  data = res.json()['Fcob']
  Fcob3 = data[0]['Fcob'] '''
  
  Tpco1 = Tpco3
  Fcob1 = Fcob3
  Fzco = Fcob1 + Fcob2 + Fcob3
  Tpco = (Tpco1*Fcob1+Tpco2*Fcob2+Tpco3*Fcob3)/(Fcob1+Fcob2+Fcob3) #średnia ważona '''
  print(Tpco)
  for i in range (1,10):
    Tpm[0]['Tpm'] = Tpmf(Fzm, ro, cw, Tzm, Tpm[0]['Tpm'], Tzco[0]['Tzco'], Mm, cwym)
    Tzco[0]['Tzco'] = Tzcof(Fzco, ro, cw, Tzco[0]['Tzco'], Tpco, kw, Tpm[0]['Tpm'], Mco, cwym)

speed=0;  
while(1):
  res = requests.get(ur_address + "/impuls")
  data = res.json()['impuls']
  impuls = data[0]['impuls']

#Skalowanie czasu
  if (speed==0):
    res1=requests.get(ur_address + "/time")
    data1= res1.json()['time']
    speed = data1[0]['speed']
  
  if (speed != 0):
    res1 = requests.get(ur_address + "/start")
    data1 = res1.json()['start']
    speed = data1[0]['start']
#Koniec skalowania czasu  
  #impuls = 1
  
  if(impuls == 1):
    print("test1")
    for i in range(0,3):
      res = requests.get(ur_address + "/Tzco")
      data = res.json()
      Tzco = data['Tzco']

      res = requests.get(ur_address + "/Tpm")
      data = res.json()
      Tpm = data['Tpm']
  
      
      calculate(Mm, Mco,cwym,ro,cw,kw,Fzco)
      
      #{'Fzm': 22.22222222222222, 'Um': 1}
      #Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym)
      #Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym)
      res = requests.put(ur_address + "/Tpm",json={'Tpm':Tpm[0]['Tpm']})
      res1 = requests.put(ur_address + "/Tzco",json={'Tzco':Tzco[0]['Tzco']})
      res = requests.post(module7_adress+"/modul4",json=[[{"id":6,"name":"Tzco","value";Tzco[0]['Tzco']},{"id":8,"name":"Tpm","value";Tpm[0]['Tpm']}]

    res2 = requests.put(ur_address + "/impuls",json={'impuls':0})

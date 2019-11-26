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
Fzco = 40;

#Variables
Fzm = 1;          #Strumien ogrzanej wody od 0 do ok. 22
To = -5;          #Temperatura zewnetrzna
Tpco = 27;          #Temperatura wody wyplywajacej z budynku
Fzco = 10;          #nie wiem xd
Tzm = 70 - 2.5*(To - 6);  #strumien ogrzanej wody
d = 0.01

#adress
ur_address = "http://127.0.0.1:5000"
module3_address = "http://127.0.0.1:5000"
module5_address = "https://f5a8b30a.ngrok.io"
module61_address = "http://127.0.0.1:5000"
module62_address = "http://127.0.0.1:5000"
module63_address = "http://127.0.0.1:5000"
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

  '''res = requests.get(module3_address)
  data = res.json()
  To = data[0]['T_o']

  res = requests.get(module3_address)
  data = res.json()
  Tzm = data[0]['T_zm']

  ###########
  #jeden request do modułu 5, w tym requescie wysyłamy im wartość Tzco

 

  ##########
  #3requesty do modułu 6, do każdego budynk osobno

  res = requests.get(module61_address + "/Tpco")
  data = res.json()['Tpco']
  Tpco1 = data[0]['Tpco']

  res = requests.get(module62_address + "/Tpco")
  data = res.json()['Tpco']
  Tpco2 = data[0]['Tpco']

  res = requests.get(module63_address + "/Tpco")
  data = res.json()['Tpco']
  Tpco3 = data[0]['Tpco']  

  res = requests.get(module61_address + "/Fcob")
  data = res.json()['Fcob']
  Fcob1 = data[0]['Fcob']

  res = requests.get(module62_address + "/Fcob")
  data = res.json()['Fcob']
  Fcob2 = data[0]['Fcob']

  res = requests.get(module63_address + "/Fcob")
  data = res.json()['Fcob']
  Fcob3 = data[0]['Fcob']
  Tpco = (Tpco1*Fcob1+Tpoc2*Fcob2+Tpco3*Fcob3)/(Fcob1+Fcob2+Fcob3) #średnia ważona '''

  res = requests.put(module5_address+"/regulation",json = {'Tzco':Tzco})
  data = res.json()['Fzm']
  Fzm = data[0]['Fzm']

  Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym)
  Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym)
  
#while(1):
res = requests.get(ur_address + "/impuls")
data = res.json()['impuls']
impuls = data[0]['impuls']
impuls = 1
print(impuls)
if(impuls == 1):
  print("test1")
  for i in range(0,100):
    res = requests.get(ur_address + "/Tzco")
    data = res.json()['Tzco']
    Tzco = data[0]['Tzco']

    res = requests.get(ur_address + "/Tpm")
    data = res.json()['Tpm']
    Tpm = data[0]['Tpm']
  
    print(data[0]['Tpm'])

    print(Tpm)
        #calculate(Mm, Mco,cwym,ro,cw,kw,Fzco)
    res = requests.put(module5_address+"/regulation",json = {'Tzco':Tzco})
    data = res.json()['Fzm']
    Fzm = data[0]['Fzm']
    #{'Fzm': 22.22222222222222, 'Um': 1}
    Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym)
    Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym)
    
    print(Tzco)
    res = requests.put(ur_address + "/Tpm",json={'Tpm':Tpm})
    res1 = requests.put(ur_address + "/Tzco",json={'Tzco':Tzco})
    res2 = requests.put(ur_address + "/impuls",json={'impuls':0})


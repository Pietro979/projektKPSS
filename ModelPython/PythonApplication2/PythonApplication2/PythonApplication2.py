import time
import json
import requests

def Tpmf(Fzm,ro,cw,Tzm,Tpm,Tzco,Mm,cwym): #zwraca Tpm[i+1]
	difference = ((Fzm*ro*cw*(Tzm - Tpm)) - (kw * (Tpm - Tzco)) )/ (Mm*cwym)
	return (difference*d)+Tpm

def Tzcof(Fzco,ro,cw,Tzco,Tpco,kw,Tpm,Mco,cwym): #zwraca Tzco[i+1]
	difference = ((-Fzco) * ro*cw*(Tzco - Tpco) + kw * (Tpm - Tzco))/(Mco*cwym)
	return (difference*d)+Tzco;


#Constants

Mm = 3000;					#Masa wymiennika po stronie pierwotnej
Mco = 3000;					#Masa wymiennika po stronie wtornej

cwym = 2700;				#zastepcze cieplo wlasciwe wymiennika
ro = 1000;					#gestosc wody
cw = 4200;					#cieplo wlasciwe wody
kw = 250000;				#wspolczynnik przenikania ciepla
	


#Variables
Fzm = 10;					#Strumien ogrzanej wody od 0 do ok. 22
To = -5;					#Temperatura zewnetrzna
Tpco = 27;					#Temperatura wody wyplywajacej z budynku
Tpm = 0;					#woda wracajaca do elektrowni
Tzco = 0;					#woda idąca do budynku
Fzco = 10;					#nie wiem xd
Tzm = 70 - 2.5*(To - 6);	#strumien ogrzanej wody

d = 0.05					#krok różniczki	

while(1):
	#dane od modułu 3 
	res = requests.get(server_addres + "/Tzm") #pobranie jsona
	data = res.json() 
	Tzm = data['variables']['value'] #przypisanie do zmiennej
	
	res = requests.get(server_addres + "/To")
	data = res.json()
	To = data['variables']['value']
	
	#dane od modułu 5
	res = requests.get(server_addres + "/Fzm")
	data = res.json()
	Fzm = data['variables']['value']
	
	#dane od modułu 6 ten będzie 3 razy i później średnia z tego
	res = requests.get(server_addres + "/Tpco")
	data = res.json()
	Tpco = data['variables']['value']
	
	#nasze obliczenia
	Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym)
	Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym)
	time.sleep(2)
	
	
	#wysyłanie do loggera (chyba xd)
	res = requests.put(server_addres + "/Tpm",json={"name":"Tpm","value":Tpm}) #metoda put niekoniecznie coś zwraca ale tak było w przykładzie, jutro to zmienie
	res = requests.put(server_addres + "/Tzco",json={"name":"Tpm","value":Tzco})
	
	print(Tpm)
	print(Tzco)

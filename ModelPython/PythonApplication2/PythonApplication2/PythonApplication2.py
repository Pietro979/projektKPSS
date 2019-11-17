import time

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
#time4 = clock();
Tpm = 0;					#woda wracajaca do elektrowni
Tzco = 0;					#woda idąca do budynku
Fzco = 10;					#nie wiem xd
Tzm = 70 - 2.5*(To - 6);	#strumien ogrzanej wody

d = 0.05					#krok różniczki	

while(1):
	Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym)
	Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym)
	time.sleep(2)
	print(Tpm)
	print(Tzco)

// pch.cpp: plik źródłowy odpowiadający wstępnie skompilowanemu nagłówkowi, niezbędny do powodzenia kompilacji

#include "pch.h"
double Tpmf(double Fzm, double ro, double cw, double Tzm, double Tpm, double Tzco, double Mm, double cwym) { //zwraca Tpm[i+1]
	double difference;

	difference = ((Fzm*ro*cw*(Tzm - Tpm)) - (kw * (Tpm - Tzco)) )/ (Mm*cwym);
		

	return (difference*d)+Tpm;
}
double Tzcof(double Fzco, double ro, double cw, double Tzco, double Tpco, double kw, double Tpm, double Mco, double cwym) { //zwraca Tzco[i+1]
	double difference;

	difference = ((-Fzco) * ro*cw*(Tzco - Tpco) + kw * (Tpm - Tzco))/(Mco*cwym);

	return (difference*d)+Tzco;
}
// Ogólnie rzecz biorąc, zignoruj ten plik, ale miej go pod ręką, jeśli używasz wstępnie skompilowanych nagłówków.

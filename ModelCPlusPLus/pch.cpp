// pch.cpp: plik źródłowy odpowiadający wstępnie skompilowanemu nagłówkowi, niezbędny do powodzenia kompilacji

#include "pch.h"
int Tpm(int Fzm, int ro, int cw, int Tzm, int Tpm, int Tzco, int Mm, int cwym) {
	int result;
	result=Fzm*ro*cw*(Tzm - Tpm) - kw * (Tpm - Tzco)/Mm/cwym;
	return result;
}
int Tzco(int Fzco, int ro, int cw, int Tzco, int Tpco, int kw, int Tpm, int Mco, int cwym) {
	int result;
	result = (-Fzco) * ro*cw*(Tzco - Tpco) + kw * (Tpm - Tzco)/Mco/cwym;
	return result;
}
// Ogólnie rzecz biorąc, zignoruj ten plik, ale miej go pod ręką, jeśli używasz wstępnie skompilowanych nagłówków.

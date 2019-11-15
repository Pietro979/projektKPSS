// ModelCPlusPLus.cpp : Ten plik zawiera funkcję „main”. W nim rozpoczyna się i kończy wykonywanie programu.
//

#include "pch.h"
#include <iostream>
#include <time.h>
#include <Windows.h>
#include <ctime>
#include <cstdio>
using namespace std;
int main()
{
	double Fzm = 10;		//Strumien ogrzanej wody od 0 do ok. 22
	double To = -5;			//Temperatura zewnetrzna
	double Tpco = 27;		//Temperatura wody wyplywajacej z budynku
	//int time4 = clock();
	double Tpm = 0;		//woda wracajaca do elektrowni
	double Tzco = 0;		//woda idąca do budynku
	double Fzco = 10;		//nie wiem xd
	double Tzm = 70 - 2.5*(To - 6);//strumien ogrzanej wody
	int timescale = 60;
	
	time_t Timerrr; // czas systemowy
	time(&Timerrr);
	time_t localtime = Timerrr; //czas który dostajemy na początku, dla przykładu wstawiłem tutaj systemowy

	while (1) {
		//if(!impuls)
		if (GetKeyState('A') & 0x8000/*Check if high-order bit is set (1 << 15)*/) {
			for (int i = 1; i <= 100; i++) {
				cout << "Time: " << localtime << endl;
				Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym);
				Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym);
				cout <<i<<". "<< Tpm << "  " << Tzco << endl;
				if (i == 20 || i == 40 || i == 60 || i == 80 || i == 100) localtime += 1 * timescale;
			}
			
		}
		/*iteracja++;
		Tpm = Tpmf(Fzm, ro, cw, Tzm, Tpm, Tzco, Mm, cwym);
		Tzco = Tzcof(Fzco, ro, cw, Tzco, Tpco, kw, Tpm, Mco, cwym);
		Sleep(1000);
		std::cout << "wcisnij A aby dzielic dane\n";
		while (GetKeyState('A') & 0x8000/*Check if high-order bit is set (1 << 15)
		{
			std::cout << "A jest wcisniete - data sharing\n("<<iteracja<<"iteracja symulacji)\n";
			Sleep(1000);
		}*/
	}
	
	
}

// Uruchomienie programu: Ctrl + F5 lub menu Debugowanie > Uruchom bez debugowania
// Debugowanie programu: F5 lub menu Debugowanie > Rozpocznij debugowanie

// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln

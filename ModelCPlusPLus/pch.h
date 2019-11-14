// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln

#ifndef PCH_H
#define PCH_H
//otrzymywane oraz wartosci fizyczne 
const double Mm = 3000;	//Masa wymiennika po stronie pierwotnej
const double Mco = 3000;	//Masa wymiennika po stronie wtornej

const double cwym = 2700;	//zastepcze cieplo wlasciwe wymiennika
const double ro = 1000;	//gestosc wody
const double cw = 4200;	//cieplo wlasciwe wody
const double kw = 250000;	//wspolczynnik przenikania ciepla

// do wlasciwego wyliczenia rozniczki w funkcjach Tpmf oraz Tzcof
double d = 0.05; //KROK!!!! zmierza do 0
int scale = 60; //skala czasu
double Tpmf(double Fzm, double ro, double cw, double Tzm, double Tpm, double Tzco, double Mm, double cwym); //zwraca Tpm[i+1]
double Tzcof(double Fzco, double ro, double cw, double Tzco, double Tpco, double kw, double Tpm, double Mco, double cwym );//zwraca Tzco[i+1]
// TODO: w tym miejscu dodaj nagłówki, które mają być wstępnie kompilowane

#endif //PCH_H

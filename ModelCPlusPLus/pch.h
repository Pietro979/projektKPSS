// Porady dotyczące rozpoczynania pracy:
//   1. Użyj okna Eksploratora rozwiązań, aby dodać pliki i zarządzać nimi
//   2. Użyj okna programu Team Explorer, aby nawiązać połączenie z kontrolą źródła
//   3. Użyj okna Dane wyjściowe, aby sprawdzić dane wyjściowe kompilacji i inne komunikaty
//   4. Użyj okna Lista błędów, aby zobaczyć błędy
//   5. Wybierz pozycję Projekt > Dodaj nowy element, aby utworzyć nowe pliki kodu, lub wybierz pozycję Projekt > Dodaj istniejący element, aby dodać istniejące pliku kodu do projektu
//   6. Aby w przyszłości ponownie otworzyć ten projekt, przejdź do pozycji Plik > Otwórz > Projekt i wybierz plik sln

#ifndef PCH_H
#define PCH_H
//otrzymywane

const int Mm = 3000;	//Masa wymiennika po stronie pierwotnej
const int Mco = 3000;	//Masa wymiennika po stronie wtornej

const int cwym = 2700;	//zastepcze cieplo wlasciwe wymiennika
const int ro = 1000;	//gestosc wody
const int cw = 4200;	//cieplo wlasciwe wody
const int kw = 250000;	//wspolczynnik przenikania ciepla


int Tpm(int Fzm, int ro, int cw, int Tzm, int Tpm,int Tzco, int Mm, int cwym);
int Tzco(int Fzco, int ro, int cw, int Tzco, int Tpco, int kw, int Tpm, int Mco, int cwym );
// TODO: w tym miejscu dodaj nagłówki, które mają być wstępnie kompilowane

#endif //PCH_H

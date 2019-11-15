#ifndef SERVICE_H_INCLUDED
#define SERVICE_H_INCLUDED
#include "BasicController.h"
#include <vector>
using std::string;
using std::vector;

class Service : public BasicController {
    public:
        Service(const std::string& address,const std::string& port) : BasicController(address,port) {}
        ~Service() {}
        void handleGet(http_request message);
        void handlePut(http_request message);
        void initRestOpHandlers() override;
    private:
        string startTime;           //format:2019-10-28+16:50:45
        string realTime;            //format:2019-10-28+16:50:45
        string startSymTime = "2009-12-11+00:00:00"; //format:2019-10-28+16:50:45
            //TO DO: jako struktura i obsluga w PUT
            int startSymTimeYear = 2009;
            int startSymTimeMonth = 12;
            int startSymTimeDay = 11;
            int startSymTimeHour = 0;
            int startSymTimeMinutes = 0;
            int startSymTimeSeconds = 0;
        string symTime;             //format:2019-10-28+16:50:45
            //TO DO: jako struktura
            int symTimeYear;
            int symTimeMonth;
            int symTimeDay;
            int symTimeHour;
            int symTimeMinutes;
            int symTimeSeconds;
        int startDayOfWeek = 5;     //format: 1 (Monday)
        int dayOfWeek;              //format: 1 (Monday)
        int startUnixDecySecs;      //tak naprawde to nie unix tylko pomniejszony zeby miescily sie decysekundy
        int symSecs;                //ilosc sekund symulowanego czasu
        int speed;                  //przyspieszenie czasu w symmulacji
};
#endif // SERVICE_H_INCLUDED

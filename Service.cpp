#include "Service.h"
#include <string>

#include "cpprest/http_client.h"

using std::string;
using std::to_string;
void Service::initRestOpHandlers() {
    _listener.support(methods::GET,std::bind(&Service::handleGet,this,std::placeholders::_1));
    _listener.support(methods::PUT,std::bind(&Service::handlePut,this,std::placeholders::_1));
}

void Service::handleGet(http_request message) {
    vector<string> path = requestPath(message);
    if(path.empty()) {
    // moze cos tu kiedys bedzie
        }
        else if(path[0]=="time")
        {  //zwraca symSecs w JSON
            web::http::client::http_client worldTimeAPI(U("http://worldtimeapi.org/api/timezone/Europe/Warsaw"));
            worldTimeAPI.request(methods::GET).then([=](http_response response)
            {
                if(response.status_code() == status_codes::OK)
                {
                    json::value jsonFromAPI = response.extract_json().get();
                    std::cout << jsonFromAPI<<std::endl;
                    int unixTime = jsonFromAPI[U("unixtime")].as_number().to_int32()-1571900000; //tak naprawde to nie unix tylko pomniejszony zeby miescily sie decysekundy
                    string dateTime = jsonFromAPI[U("datetime")].as_string();
                    std::cout<<dateTime<<std::endl;
                    int unixDecySecs = (dateTime[20]-48)*10+(dateTime[21]-48);
                    std::cout<<unixDecySecs<<std::endl;
                    unixDecySecs+=unixTime*100; //obecne
                    symSecs = (unixDecySecs-startUnixDecySecs)*speed/100;
                    std::cout << startUnixDecySecs<<"-"<<unixDecySecs<<"="<<symSecs<<std::endl<<std::endl;

                    json::value jsonSymSecs;
                    jsonSymSecs["symSec"] = json::value::number(symSecs);

                    message.reply(status_codes::OK,jsonSymSecs);
                }
            });
        }
        else if(path[0]=="details") //zwraca jsony ze szcegolami
        {
            web::http::client::http_client worldTimeAPI(U("http://worldtimeapi.org/api/timezone/Europe/Warsaw"));
            worldTimeAPI.request(methods::GET).then([=](http_response response)
            {
                if(response.status_code() == status_codes::OK)
                {
                    //pobieranie danych
                    json::value jsonFromAPI = response.extract_json().get();
                    std::cout << jsonFromAPI<<std::endl;
                    int unixTime = jsonFromAPI[U("unixtime")].as_number().to_int32()-1571900000; //tak naprawde to nie unix tylko pomniejszony zeby miescily sie decysekundy
                    string dateTime = jsonFromAPI[U("datetime")].as_string();

                    //symSecs
                    std::cout<<dateTime<<std::endl;
                    int unixDecySecs = (dateTime[20]-48)*10+(dateTime[21]-48);
                    std::cout<<unixDecySecs<<std::endl;
                    unixDecySecs+=unixTime*100; //obecne
                    symSecs = (unixDecySecs-startUnixDecySecs)*speed/100;
                    std::cout << startUnixDecySecs<<"-"<<unixDecySecs<<"="<<symSecs<<std::endl<<std::endl;

                    //realTime
                    realTime=dateTime.substr(0,22);
                    realTime[10]='+';


                    //symTime - udajemy ze zawsze nieprzestepny, miesiace 31 dni..
                    int symSecTmp = symSecs;
                    symTimeYear = startSymTimeYear + symSecTmp/315360000;
                    symSecTmp %= 31536000;
                    symTimeMonth = startSymTimeMonth + symSecTmp/2678400;
                    symSecTmp %= 2678400;
                    symTimeDay = startSymTimeDay + symSecTmp/86400;
                    symSecTmp %= 86400;
                    symTimeHour = startSymTimeHour + symSecTmp/3600;
                    symSecTmp %= 3600;
                    symTimeMinutes = startSymTimeMinutes + symSecTmp/60;
                    symTimeSeconds = startSymTimeSeconds + symSecTmp%60;
                    if (symTimeSeconds >= 60){
                            symTimeMinutes += symTimeSeconds/60;
                            symTimeSeconds %= 60;
                    }
                    if (symTimeMinutes >= 60){
                            symTimeHour += symTimeMinutes/60;
                            symTimeMinutes %= 60;
                    }
                    if (symTimeHour >= 24){
                            symTimeDay += symTimeHour/24;
                            symTimeHour %= 24;
                    }
                    if (symTimeDay > 31){
                            symTimeMonth += symTimeDay/31;
                            symTimeDay %= 31;
                    }
                    if (symTimeMonth > 12){
                            symTimeYear+= symTimeMonth/12;
                            symTimeMonth %= 12;
                    }
                    symTime = to_string(symTimeYear) + '-' + to_string(symTimeMonth) + '-' + to_string(symTimeDay) + '+' + to_string(symTimeHour) + ':' + to_string(symTimeMinutes) + ':' + to_string(symTimeSeconds);
                    if (symTimeMonth < 10)  symTime.insert(5,"0");
                    if (symTimeDay < 10)  symTime.insert(8,"0");
                    if (symTimeHour < 10)  symTime.insert(11,"0");
                    if (symTimeMinutes < 10)  symTime.insert(14,"0");
                    if (symTimeSeconds < 10)  symTime.insert(17,"0");

                    //dayOfWeek
                    dayOfWeek = startDayOfWeek + symSecs/86400;
                    dayOfWeek = dayOfWeek%7 + 1;

                    json::value jsonDetails;
                    jsonDetails["startTime"] = json::value::string(startTime);
                    jsonDetails["realTime"] = json::value::string(realTime);
                    jsonDetails["startSymTime"] = json::value::string(startSymTime);
                    jsonDetails["symTime"] = json::value::string(symTime);
                    jsonDetails["dayOfWeek"] = json::value::number(dayOfWeek);
                    jsonDetails["symSec"] = json::value::number(symSecs);
                    jsonDetails["speed"] = json::value::number(speed);

                    message.reply(status_codes::OK,jsonDetails);
                    /*
                    JSON:
                        string startTime; //format:2019-10-28+16:50:45
                        string realTime; //format:2019-10-28+16:50:45
                        string symTime; //format:2019-10-28+16:50:45
                        int dayOfWeek; //format: 1 (Monday)
                        int startUnixDecySecs; //tak naprawde to nie unix tylko pomniejszony zeby miescily sie decysekundy    JEST
                        int symSecs; //ilosc sekund symulowanego czasu
                        int speed; //przyspieszenie czasu w symmulacji8/
                    */
                }
            });
        }
        else if(path[0]=="prettytime") //zwraca czas w stringu
        {
            web::http::client::http_client worldTimeAPI(U("http://worldtimeapi.org/api/timezone/Europe/Warsaw"));
            worldTimeAPI.request(methods::GET).then([=](http_response response)
            {
                if(response.status_code() == status_codes::OK)
                {
                    //pobieranie danych
                    json::value jsonFromAPI = response.extract_json().get();
                    std::cout << jsonFromAPI<<std::endl;
                    int unixTime = jsonFromAPI[U("unixtime")].as_number().to_int32()-1571900000; //tak naprawde to nie unix tylko pomniejszony zeby miescily sie decysekundy
                    string dateTime = jsonFromAPI[U("datetime")].as_string();

                    //aktualizacja symSecs
                    std::cout<<dateTime<<std::endl;
                    int unixDecySecs = (dateTime[20]-48)*10+(dateTime[21]-48);
                    std::cout<<unixDecySecs<<std::endl;
                    unixDecySecs+=unixTime*100; //obecne
                    symSecs = (unixDecySecs-startUnixDecySecs)*speed/100;
                    std::cout << startUnixDecySecs<<"-"<<unixDecySecs<<"="<<symSecs<<std::endl<<std::endl;

                    //symTime - udajemy ze zawsze nieprzestepny, miesiace 31 dni..
                    int symSecTmp = symSecs;
                    symTimeYear = startSymTimeYear + symSecTmp/315360000;
                    symSecTmp %= 31536000;
                    symTimeMonth = startSymTimeMonth + symSecTmp/2678400;
                    symSecTmp %= 2678400;
                    symTimeDay = startSymTimeDay + symSecTmp/86400;
                    symSecTmp %= 86400;
                    symTimeHour = startSymTimeHour + symSecTmp/3600;
                    symSecTmp %= 3600;
                    symTimeMinutes = startSymTimeMinutes + symSecTmp/60;
                    symTimeSeconds = startSymTimeSeconds + symSecTmp%60;
                    if (symTimeSeconds >= 60){
                            symTimeMinutes += symTimeSeconds/60;
                            symTimeSeconds %= 60;
                    }
                    if (symTimeMinutes >= 60){
                            symTimeHour += symTimeMinutes/60;
                            symTimeMinutes %= 60;
                    }
                    if (symTimeHour >= 24){
                            symTimeDay += symTimeHour/24;
                            symTimeHour %= 24;
                    }
                    if (symTimeDay > 31){
                            symTimeMonth += symTimeDay/31;
                            symTimeDay %= 31;
                    }
                    if (symTimeMonth > 12){
                            symTimeYear+= symTimeMonth/12;
                            symTimeMonth %= 12;
                    }
                    symTime = to_string(symTimeYear) + '-' + to_string(symTimeMonth) + '-' + to_string(symTimeDay) + '+' + to_string(symTimeHour) + ':' + to_string(symTimeMinutes) + ':' + to_string(symTimeSeconds);
                    if (symTimeMonth < 10)  symTime.insert(5,"0");
                    if (symTimeDay < 10)  symTime.insert(8,"0");
                    if (symTimeHour < 10)  symTime.insert(11,"0");
                    if (symTimeMinutes < 10)  symTime.insert(14,"0");
                    if (symTimeSeconds < 10)  symTime.insert(17,"0");

                    json::value jsonPrettyTime;
                    jsonPrettyTime["symTime"] = json::value::string(symTime);

                    message.reply(status_codes::OK,jsonPrettyTime);
                }
            });
        }
        else //zle zapytanie
        {
            message.reply(status_codes::BadRequest);
        }
    }

void Service::handlePut(http_request message) {
    message.extract_json().then([=](pplx::task<json::value> task)
    {
        try
        {
            web::http::client::http_client worldTimeAPI(U("http://worldtimeapi.org/api/timezone/Europe/Warsaw"));
            worldTimeAPI.request(methods::GET).then([=](http_response response)
            {
                if(response.status_code() == status_codes::OK)
                {
                    json::value jsonFromAPI = response.extract_json().get();
                    std::cout << jsonFromAPI<<std::endl;
                    int unixTime = jsonFromAPI[U("unixtime")].as_number().to_int32()-1571900000; //tak naprawde to nie unix tylko pomniejszony zeby miescily sie decysekundy
                    string dateTime = jsonFromAPI[U("datetime")].as_string();
                    //startTime = dateTime
                    std::cout<<dateTime<<std::endl;
                    int unixDecySecs = (dateTime[20]-48)*10+(dateTime[21]-48);
                    std::cout<<unixDecySecs<<std::endl;
                    unixDecySecs+=unixTime*100;
                    startUnixDecySecs = unixDecySecs;
                    startTime=dateTime.substr(0,22);
                    startTime[10]='+';
                    std::cout << startUnixDecySecs<<","<<startTime<<std::endl<<std::endl;

                    json::value val = task.get();
                    int newSpeed = val[U("speed")].as_number().to_int32();
                    speed = newSpeed;  //nowa predkosc
                    std::cout<<newSpeed<<std::endl;

                    message.reply(status_codes::OK);
                }
            });  //nowy czas startu dodano
        }
        catch(std::exception& e)
        {
            message.reply(status_codes::NotFound);
        }
    });
}

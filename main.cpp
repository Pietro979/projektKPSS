#include <iostream>
#include "Service.h"
using namespace std;

int main()
{
    Service serv("0.0.0.0","8080");
    serv.setEndpoint("/api");
    serv.accept().wait();
    while(1==1)
    {
        sleep(10);
    }
    return 0;
}

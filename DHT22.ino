
#include <DHT.h>;

#define DHTPIN 7     
#define DHTTYPE DHT22   
DHT dht(DHTPIN, DHTTYPE); 


int chk;
float hum; 
float temp; 

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
    hum = dht.readHumidity();
    temp= dht.readTemperature();
    Serial.println(String(hum, DEC) + ", " + String(temp, DEC));
    delay(1000); 
}

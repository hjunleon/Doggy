
#include "DHT.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <PubSubClient.h>

#define DHTPIN 16
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);


const char* ssid = "Home";
const char* password = "09021964";
 
IPAddress mqtt_server(127, 0, 0, 1); // local LAN Address
const char* mqtt_user = "mqtt";
const char* mqtt_password = "__mqttpassword__";
 
const char* mqtt_channel_pub = "esp32.out";
const char* mqtt_channel_sub = "esp32.in";
 
WiFiClient wifi;
PubSubClient mqtt(wifi);
 
#define MSG_BUFFER_SIZE (128)
char msg[MSG_BUFFER_SIZE];


void setup_wifi(){
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
   
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("Connecting to ");
  Serial.println(ssid);
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println(F("DHTxx test!"));
  
  dht.begin();

}



void test_DHT(){
  // Wait a few seconds between measurements.
  delay(2000);
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
}

void loop() {
//  test_DHT();

  while (!mqtt.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (mqtt.connect(clientId.c_str())) {   //, mqtt_user, mqtt_password
      Serial.println("connected");
      // Once connected, publish an announcement...
      mqtt.publish(mqtt_channel_pub, "hello ESP32");
      // ... and resubscribe
      mqtt.subscribe(mqtt_channel_sub);
    } else {
      Serial.print("failed, rc=");
      Serial.print(mqtt.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
 
  mqtt.loop();
}

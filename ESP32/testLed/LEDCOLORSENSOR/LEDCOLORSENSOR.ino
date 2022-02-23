#define LED_PIN 25
//void setup() {
//  // put your setup code here, to run once:
//  pinMode(LED_PIN,OUTPUT);
//  digitalWrite(LED_PIN, HIGH);  
//}

//void loop() {
//  // put your main code here, to run repeatedly:
//  digitalWrite(LED_PIN, HIGH);   
//  delay(1000);              
//  digitalWrite(LED_PIN, LOW);   
//  delay(1000);   
//}


/*********
  Rui Santos
  Complete project details at http://randomnerdtutorials.com  
*********/

// TCS230 or TCS3200 pins wiring to Arduino
#define S0 26
#define S1 27
#define S2 21
#define S3 32
#define sensorOut 33

// Stores frequency read by the photodiodes
int redFrequency = 0;
int greenFrequency = 0;
int blueFrequency = 0;

void setup() {
  pinMode(LED_PIN,OUTPUT);
  digitalWrite(LED_PIN, HIGH); 

  
  // Setting the outputs
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  
  // Setting the sensorOut as an input
  pinMode(sensorOut, INPUT);
  
  // Setting frequency scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  
   // Begins serial communication 
  Serial.begin(9600);
}
void loop() {
  // Setting RED (R) filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  
  // Reading the output frequency
  redFrequency = pulseIn(sensorOut, LOW);
  
   // Printing the RED (R) value
  Serial.print("R = ");
  Serial.print(redFrequency);
  delay(100);
  
  // Setting GREEN (G) filtered photodiodes to be read
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  
  // Reading the output frequency
  greenFrequency = pulseIn(sensorOut, LOW);
  
  // Printing the GREEN (G) value  
  Serial.print(" G = ");
  Serial.print(greenFrequency);
  delay(100);
 
  // Setting BLUE (B) filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  
  // Reading the output frequency
  blueFrequency = pulseIn(sensorOut, LOW);
  
  // Printing the BLUE (B) value 
  Serial.print(" B = ");
  Serial.println(blueFrequency);
  delay(100);
}

#include <SoftwareSerial.h>
#define swRX 2
#define swTX 3
#define BAUD 115200

String AP =  "";   // your AP SSID
String Password  = "";  // your AP Password

int redPin = 4;
int greenPin = 5;
int bluePin = 6;
const int motorPin1  = 12;  // Pin 14 of L293
const int motorPin2  = 11;  // Pin 10 of L293
// left
const int motorPin3  = 10; // Pin  7 of L293
const int motorPin4  = 9;  // Pin  2 of L293

SoftwareSerial wifi(swRX, swTX);
String data = "";
void setup() {
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);

  rgb(255, 0, 0); // not ready
  wifi.begin(BAUD);
  execute("AT+RST\r\n"); // Reset the wifi
  rgb(255, 255, 255);
  execute("AT+CWMODE=1\r\n"); //Set station mode Operation
  rgb(255, 0, 0);
  execute("AT+CWJAP=\"" + AP + "\",\"" + Password + "\"\r\n");
  rgb(255, 255, 255);
  while(!wifi.find("OK")); // use if the wifi is connecting in my case its fasr AF
  rgb(255, 0, 0);
  execute("AT+CIPMUX=1\r\n");
  rgb(255, 255, 255);
  execute("AT+CIPSERVER=1,80\r\n"); // server at 80 port
  rgb(0, 255, 0); // ready
}
void rgb(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, 255 - redValue);
  analogWrite(greenPin, 255 - greenValue);
  analogWrite(bluePin, 255 - blueValue);
}

/*
  
*/
String execute(String cmd) {
  String resp = "";
  wifi.print(cmd);
  long int time = millis();
  while ( (time + 5000) > millis())
  {
    while (wifi.available())
    {
      char c = wifi.read();
      resp += c;
    }
  }
  return resp;
}


void loop() {

  rgb(0, 255, 0);
  if (wifi.available())
  {
    rgb(255, 255, 0);

    if (wifi.find("+IPD,"))
    {
      String msg;
      wifi.find("?");
      msg = wifi.readStringUntil(' ');
      String command1 = msg.substring(0, 5);
      String command2 = msg.substring(7);

      if (command2 == "brk") {
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, LOW);
        rgb(255, 222, 173);
      } else if (command2 == "lft") {
        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, HIGH);
        rgb(255, 0, 255);
      } else if (command2 == "fwd")  {
        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, HIGH);
        digitalWrite(motorPin4, LOW);
        rgb(240, 230, 140);
      } else if (command2 == "rgt") {
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin2, HIGH);
        digitalWrite(motorPin3, HIGH);
        digitalWrite(motorPin4, LOW);
        rgb(0, 0, 255);
      } else if (command2 == "bck") {
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin2, HIGH);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, HIGH);
        rgb(255, 165, 0);
      }
    }
  }
}

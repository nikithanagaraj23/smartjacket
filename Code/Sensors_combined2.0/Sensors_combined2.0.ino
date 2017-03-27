// By kevin@playwithmyled.com - 2009-10-17.
// 2010-05-11: Better and lighter.

// Define a function pointer and initialize to NULL.
typedef void (*FunctionPointer) ();
int ledPin = 13;
int sensorPin = 0;
double alpha = 0.75;
int period = 20;
double change = 0.0;
float tempC;
int tempPin = 4;
int i=0;int j=0;

#include <MPU6050.h>
#include <I2Cdev.h>
#include <Wire.h>
 
MPU6050 accelgyro;
 
int ax, ay, az;
int gx, gy, gz;
int led = 13;

// Declare looping actions function names, declared lower.
FunctionPointer xActions[] = {loopActionA,loopActionB,loopActionC, loopActionD};
// Define actions status flags. Set to 1 to auto execute a start.
int xActionsFlags[] = {0,0,0,0}; 

int xActionsCount = sizeof(xActions);

void xActionTrigger(int id=0, int action=0) {
  // The id represent it's position in the flags array.
  // Action 1 = executed, 0 not.
  xActionsFlags[id] = action;
}

// LOOPING FUNCTIONS
/*
void loopActionA() {
        // Do something...
    static double oldValue = 0;
    static double oldChange = 0;
    analogRead(sensorPin);
    delay(10);
    int rawValue = analogRead (sensorPin);
    double value = alpha * oldValue + (1 - alpha) * rawValue;
   
    Serial.print (rawValue);
    Serial.print (",");
    Serial.println (value);
    oldValue = value;
    delay (2000);
  }
*/
void loopActionA()
{
  
  analogRead(sensorPin);
  //delay(10);
  int sensorValue = analogRead(sensorPin);
/*  Serial.print("P");
  Serial.println(sensorValue);*/
  //Serial.println(j);
  j=j+1;
  if (sensorValue>500)
  {
     i=i+1;
  
  }
   if(j==350)
  {
    Serial.print("H");
    Serial.println(i);
    Serial.println();
    
  j=0;
  i=0;
  }
  
  delay(100);
 
}

void loopActionB() {
	// Do something...
analogRead(tempPin);
delay(10);
   tempC = analogRead(tempPin);
  //tempC = (5.0*tempC*100.0)/1024.0;
   tempC=tempC * 0.48828125;
  
   Serial.print("T");
   Serial.println((byte)tempC);
   delay(70);
}

void loopActionC() {

  int a = analogRead(1);
  // Sleep for 50ms, which provides the recommended sample rate (20Hz)
  delay(50);
  Serial.print("G");
  Serial.println(a);
  delay(70);

}


void loopActionD()
{
  accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  Serial.print("A");
 Serial.println(ax);
  delay(50);
}

// Exectute all loop functions.

void xDoActions() {
	// Execute all looped function.
	for(unsigned int j=0; j < xActionsCount; j++) {
		if( xActionsFlags[j] == 1 ) { // Execute the action if.
			xActions[j](); // Call the related loop action.
		}
	}
}


void setup() {
  
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Wire.begin();
  accelgyro.initialize();
  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  accelgyro.setFullScaleAccelRange(1);
  
  
      xActionTrigger(1,1); // temp
        
      xActionTrigger(0,1); // heartbeat
      
      xActionTrigger(2, 1); //gsr
      
      xActionTrigger(3,1); // accel
      
}

void loop() {
	xDoActions();


}

void delay_x(uint32_t millis_delay)
{
  uint16_t micros_now = (uint16_t)micros();

  while (millis_delay > 0) {
    if (((uint16_t)micros() - micros_now) >= 1000) {
      millis_delay--;
      micros_now += 1000;
    }
  }  
}

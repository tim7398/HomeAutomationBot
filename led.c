#include <stdio.h>
#include <wiringPi.h>
//https://pinout.xyz/pinout/pin22_gpio25 for pin layout 
int main (void)
{
  printf ("Raspberry Pi blink\n") ;
 
  if (wiringPiSetup () == -1)
    return 1 ;
 
  pinMode (0, OUTPUT) ;         // aka BCM_GPIO pin 17



  if(digitalRead(0) == 0)
   {
       digitalWrite(0,1);
   }

  else
   {
       digitalWrite(0,0);
   }
 
  return 0 ;
}

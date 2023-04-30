from machine import PWM, Pin
from utime import sleep

class Motor():
    def __init__(self, A,B):
        self.A = PWM(A) # Creating a PWM object for motor phase A
        self.A.freq(500) # Establishing PWM frequency
        self.A.duty_u16(0) # Setting 0% duty cycle
        self.B = B # Creating a Pin for motor phase B
        self.B.off() # State of closing
        
    def u16(self,percent): # Helper function converting the speed to u16
        return int(percent * 65536) 

    def speed(self, vel):
        speed = self.u16(min(abs(vel/100),1)) # Define the speed of the motor
        if vel < 0:
            self.B.off()
        else:
            self.B.on()
        self.A.duty_u16(speed)  # to float between pulses, make this a 1

        

from time import sleep
from machine import Pin
from machine import PWM

#Function to set an angle

#The position is expected as a parameter

def moveServo_forward(PWMpin):
    pwm = PWM(Pin(PWMpin))
    pwm.freq(50)

    for position in range(1000,9000,50):
        pwm.duty_u16(position)
        sleep(0.01)
 # type: ignore
    
def moveServo_backward(PWMpin):
    pwm = PWM(Pin(PWMpin))
    pwm.freq(50)

    for position in range(9000,1000,-50):
        pwm.duty_u16(position)
        sleep(0.01)
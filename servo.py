from time import sleep
from machine import Pin
from machine import PWM

#Function to set an angle

#The PWMpin is expected as a parameter

#full range = 9000 / 1000

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

    for position in range(6000,5000,-50):
        pwm.duty_u16(position)
        sleep(0.01)

def servo_Home(PWMpin, homeposition):
    pwm = PWM(Pin(PWMpin))
    pwm.freq(50)

    pwm.duty_u16(homeposition)
    sleep(0.01)
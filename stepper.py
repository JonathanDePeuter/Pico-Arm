from machine import Pin
import utime

pins = [
    Pin(15, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(16, Pin.OUT),
    Pin(17, Pin.OUT)
]

full_step_sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

for step in full_step_sequence:
    for i in range (len(pins)):
        pins[i].value(step[i])
        utime.sleep(0.01)
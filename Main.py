import network
import socket
from time import sleep
import machine
import servo
from machine import Pin

led = Pin("LED", Pin.OUT)

ssid = 'Kelly & Jonathan'
password = 'kumkoy2012'

def abort():
    print("abort")

def axis1_left():
    print("axis 1 left")

def axis1_right():
    print("axis 1 right")

def axis2_plus():
    print("axis 2 plus")
    servo.moveServo_forward(4)

def axis2_min():
    print("axis 2 min")
    servo.moveServo_backward(4)

def axis3_plus():
    print("axis 3 plus")
    servo.moveServo_forward(5)

def axis3_min():
    print("axis 3 min")
    servo.moveServo_backward(5)

def axis4_plus():
    print("axis 4 plus")
    servo.moveServo_forward(6)

def axis4_min():
    print("axis 4 min")
    servo.moveServo_backward(6)

def axis5_plus():
    print("axis 5 plus")
    servo.moveServo_forward(7)

def axis5_min():
    print("axis 5 min")
    servo.moveServo_backward(7)

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    led.on()
    return ip

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Pico Arm Robot Control</title>
            </head>
            <center><b>

            <form action="./Z+">
            <input type="submit" value="Z+ / J3+" style="height:120px; width:120px" />
            </form>

            <form action="./Y+">
            <input type="submit" value="Y+ / J2+" style="height:120px; width:120px" />
            </form>
            <table><tr>

            <td><form action="./J4-">
            <input type="submit" value="J4-" style="height:120px; width:120px" />
            </form></td>

            <td><form action="./X-">
            <input type="submit" value="X- / J1-" style="height:120px; width:120px" />
            </form></td>

            <td><form action="./abort">
            <input type="submit" value="Abort" style="height:120px; width:120px" />
            </form></td>

            <td><form action="./X+">
            <input type="submit" value="X+ / J1+" style="height:120px; width:120px" />
            </form></td>

            <td><form action="./J4+">
            <input type="submit" value="J4+" style="height:120px; width:120px" />
            </form></td>
            </tr></table>

            <form action="./Y-">
            <input type="submit" value="Y- / J2-" style="height:120px; width:120px" />
            </form>

            <form action="./Z-">
            <input type="submit" value="Z- / J3-" style="height:120px; width:120px" />
            </form>
            </body>
            </html>
            """
    return str(html)

def server(connection):
    #Start web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/Z+?':
            axis3_plus()
        elif request == '/Y+?':
            axis2_plus()
        elif request == '/J4-?':
            axis4_min()
        elif request =='/X-?':
            axis1_left()
        elif request =='/abort?':
            abort()
        elif request =='/X+?':
            axis1_right()
        elif request == '/J4+?':
            axis4_plus()
        elif request =='/Y-?':
            axis2_min()
        elif request =='/Z-?':
            axis3_min()
        html = webpage()
        client.send(html)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    server(connection)
except KeyboardInterrupt:
    machine.reset()
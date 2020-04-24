#ModbusTCP communication to blink a light
#connected to DO4 on SCADAPack
import socket
from umodbus import conf
from umodbus.client import tcp
from time import sleep

SCADAIP = '192.168.0.12'


# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True

# open connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SCADAIP, 502))

#loop to blink light
for loop in range(20):
    
    # start with 'on' command (1)
    # make sure range value is even if you want to end with light off
    onoff = 1 if (loop%2==0) else 0 
        
    # set message to write to coil (DO4)
    message = tcp.write_single_coil(slave_id=1, address=4, value=onoff)

    # send message
    response = tcp.send_message(message, sock)
    
    # wait 0.5 second before looping
    sleep(0.5)


#close connection
sock.close()

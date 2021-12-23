import socket
import re
from uuid import getnode
from _thread import *
# getting mac physical add:
MacAddr = getnode()

#converting the raw formating into hex code format
address_mac = str(":".join(re.findall('..', '%012x' % MacAddr)))

socketserver = socket.socket()
localhostt = '127.0.0.1'
portnumber = 2005
Threadnumber = 0
try:
    socketserver.bind((localhostt, portnumber))
except socket.error as f:
    print(str(f))

print('Socket is ready to funtion..')
socketserver.listen(14)

def multipleclients(client_connectionn):
    client_connectionn.send(str.encode('Server is successfuly in charge:'))
    while True:
        information = client_connectionn.recv(2048)
        reply = 'Server send this message:  ' + information.decode('utf-8')
        if not information:
            break
        client_connectionn.sendall(str.encode(reply))
    client_connectionn.close()

while True:
    Clientside, clientaddress = socketserver.accept()
    print('server has been connected to:  ' + clientaddress[0] + ':' + str( clientaddress [1] ))
    print("The hex code for the mac address is:"  + address_mac)
    start_new_thread ( multipleclients, (Clientside, ) )
    Threadnumber += 1
    print('the thread number for this client is: ' + str(Threadnumber))
socketserver.close()
import socket
import sys
import traceback
import re
from uuid import getnode
from threading import Thread

MacAddr = getnode()
#converting the raw formating into hex code format
address_mac = str(":".join(re.findall('..', '%012x' % MacAddr)))

def mainprogram():
    starting_UDPserver()


def starting_UDPserver():
    localhost = "127.0.0.1"
    portnumber = 1111        

    UDPsocket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    UDPsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    print("UDP Socket has been successfully created!")

    try :
        UDPsocket.bind((localhost, portnumber))
    except :
        print("CONNECTION FAILED ...try again : " )
        sys.exit()

    UDPsocket.listen(10)       # queue up to 10 clients
    print("Socket has been created is ready to listen")

    while True:
        UDPconnectionn, addressserver = UDPsocket.accept()
        ipaddress, portnumber = str(addressserver[0]), str( addressserver [1] )
        print("Connected from " + ipaddress + ":" + portnumber)
        print("The hex code for the mac address is:"  + address_mac)

        try:
            Thread(target=threaded_client, args=(UDPconnectionn, ipaddress, portnumber) ).start()
        except:
            print("Thread hasn't started yet...")
            traceback.print_exc()

    UDPsocket.close()


def threaded_client(UDPconnectionn, ipaddress, portnumber, buffersize_max = 5120):
    activestate = True

    while activestate:
        input_message = recieving_data(UDPconnectionn, buffersize_max)

        if '–QUIT–' in input_message:
            print("Client request to exit...")
            UDPconnectionn.close()
            print("Connection from " + ipaddress + ":" + portnumber + " is closed")
            activestate = False
        else:
            print("message recieved: {}".format(input_message))
            UDPconnectionn.sendall('-'.encode( 'utf8' ))


def recieving_data(UDPconnectionn, buffersize_max):
    input_message = UDPconnectionn.recv(buffersize_max)
    input_messagesize = sys.getsizeof( input_message )

    if input_messagesize > buffersize_max:
        print("The message is too big {}".format(input_messagesize))

    decoding_message = input_message.decode('utf8').rstrip( )  
    outcome = processing_data(decoding_message)

    return outcome


def processing_data(string_message):
    print("processing data recieved from the UDP client screen.")

    return "HEYY " + str(string_message).upper()

if __name__ == "__main__":
    mainprogram()

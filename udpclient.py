import socket
import sys

def mainprogram():
    UDPsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    localhost = "127.0.0.1"
    portnumber = 1111

    try:
        UDPsoc.connect((localhost, portnumber))
    except:
        print("connection failed!! try again")
        sys.exit()

    print(" type 'quit' if you would like to exit")
    inputted_data= input(" ->>> ")

    while inputted_data != 'quit':
        UDPsoc.sendall(inputted_data.encode('utf8'))
        if UDPsoc.recv(5120).decode('utf8') == "-":
            pass        

        inputted_data = input(" ->>>> ")

    UDPsoc.send('-----quit screen-----')

if __name__ == "__main__":
    mainprogram()
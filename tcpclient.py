import socket

multisockets_clients = socket.socket()
localhostt = '127.0.0.1'
portnumber = 2005

print('waiting for the connection to be achieved...')
try:
    multisockets_clients.connect((localhostt, portnumber))
except socket.error as error:
    print(str(error))

response = multisockets_clients.recv(1024)
while True:
    Welcomemessage = input('Welcome to client side: ')
    multisockets_clients.send(str.encode(Welcomemessage))
    response = multisockets_clients.recv(1024)
    print(response.decode('utf-8'))

multisockets_clients.close()
import socket



IP = "192.168.0.157"
PORT = 9001
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket):
    print(clientsocket)
    calc_tres = clientsocket.recv(2048).decode("utf-8")

    if calc_tres[0] == '1':
        resultado = str(int(calc_tres[1])+ int(calc_tres[2]))
        salida = str.encode(resultado)
        clientsocket.send(salida)

    elif calc_tres[0] == '2':
        resultado = str(int(calc_tres[1]) * int(calc_tres[2]))
        salida = str.encode(resultado)
        clientsocket.send(salida)

    clientsocket.close()







serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:

        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)


except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
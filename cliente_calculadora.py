import socket

IP = "192.168.0.157"
PORT = 9001

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))


except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

def menu():
    print("Calculadora")
    print("0.Terminar")
    print("1.Sumar")
    print("2.Multiplicar")
    opcion = input("Elija una opción:")
    return opcion

opcion = menu()
while opcion != '0' and opcion != '1' and opcion != '2':
    print('Lo siento. Valor incorrecto')
    menu()
if opcion != '0':
    def par():
        numeros = input('Introduzca dos números: ')
        return numeros
    numeros = par()

    try:
        numeros = int(numeros)

    except ValueError:
        print('Error. Pruebe otra vez')
        par()

    numeros = str(numeros)
    numeros = numeros[0:2]
    calc_tres = opcion + str(numeros)
    output = str.encode(calc_tres)
    s.send(output)

    resultado = s.recv(2048).decode("utf-8")
    print('El resultado es:', resultado)

else:
    numeros = '00'
    calc_tres = opcion + str(numeros)
    output = str.encode(calc_tres)
    s.send(output)











s.close()

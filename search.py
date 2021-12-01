import socket


LocalIP = socket.gethostbyname(socket.gethostname())
port = 5555
u = 1
find = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print("This program will try to find a copy of itself on the local subnet")
print("type help for a list of commands")
while u == 1:

    command = input('Type your command: ')
    if command == 'help':
        print("Type copy to make this file listen")
        print("Type find to find a copy")
        print("type help for a list of commands")
        print("type stop to end the program")
    elif command == 'copy':
        J = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        msg = "Hello"
        J.bind((LocalIP, port))
        J.listen(1)
        print("Waiting for connection")

        while True:
            copysock, addr = J.accept()
            print("A copy has found you!")
            copysock.send(bytes(msg.encode('utf-8')))
            msg_y = copysock.recv(1024)
            msgDeco = msg_y.decode('utf-8')
            print(msgDeco)
            copysock.close()
            J.close()
            break

    elif command == 'find':
        J = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        J.connect((LocalIP, port))
        while True:
            print("You found a copy!")
            msg_h = J.recv(1024)
            msgDecoded = msg_h.decode('utf-8')
            print(msgDecoded)
            msg = "hello"
            J.send(bytes(msg.encode('utf-8')))
            break

    elif command == 'stop':
        break

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
while True:
    msg = input('Input Msg :')
    msgs = msg.encode()
    y = s.send(bytes(msg, 'utf-8'))
    print(msg)
    msg = s.recv(1024).decode()
    print("Admin's msg : **", msg)
    continue
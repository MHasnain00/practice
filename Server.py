import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(2)
print('Listening')
while True:
    connection, Adress = s.accept()
    print(Adress)
    y= True
    while y:
        msg = connection.recv(1024).decode()
        print(Adress,msg)
        nawan = input('Your msg :')
        sender = connection.send(bytes(nawan, 'utf-8'))
        if len(msg) < 1:
            y = False
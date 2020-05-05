import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
############
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #открываем окно к серверу
mysock.connect(('data.pr4e.org', 80)) #подключаемся к порту 80
terminal = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()#http rule get. encode нужен для того чтобы данные стринг in python поменялись в UTF-8
mysock.send(terminal)#Отправляем файл на сервер

while True: 
    data = mysock.recv(512)#recv methode используется для принятия ответа от сервера
    if (len(data)<1):
        break
    print(data.decode())
mysock.close()
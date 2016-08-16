import datetime
now = datetime.datetime.now()
from socket import *
serverName = '192.168.2.8'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect((serverName, serverPort))
clientSocket.settimeout(1)
t = 0
while t < 10:
    clientSocket.send("")
    time = now.strftime("%Y-%m-%d %H:%M")
    data = clientSocket.recv(1024)
    if data is None:
        print 'Requst time out'
    else:
        print 'Ping', t, time

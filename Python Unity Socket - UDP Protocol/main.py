import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#get ip adress
ip = socket.gethostbyname('www.google.com')
print(ip)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
# default port for socket
port = 80
# connecting to the server
s.connect((ip, port))
print ("the socket has successfully connected to google on port == %s" %(ip))

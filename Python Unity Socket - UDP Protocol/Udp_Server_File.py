import socket

# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 1234
# declare our serverSocket upon which
# we will be listening for UDP messages
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# One difference is that we will have to bind our declared IP address
# and port number to our newly declared serverSock
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
print('socket listensing ... ')
while True:
    data, addr = serverSock.recvfrom(1024)
    print ("Message: ", data.decode("utf-8"),"Adrees is ",addr)
    # list = data.decode("utf-8").split(' ')  # cominda data in string  so we split into list on basis of space
    # value1 = float(list[0])
    # value2 = float(list[1])
    # UpdateValue = str(value1) + " " + str(value2) + " "  # +str(value3)
    # # c.sendall(UpdateValue.encode("utf-8"))#then encode and send that string back to unity
    # print(UpdateValue)
    UpdateValue="Hello client"
    serverSock.sendto(UpdateValue.encode("utf-8"), (addr))
    print("Message sent ")
    # serverSock.sendto(UpdateValue.encode("utf-8"), (UDP_IP_ADDRESS, UDP_PORT_NO))
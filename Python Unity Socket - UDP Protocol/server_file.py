import  socket
def sending_and_reciveing():
    s = socket.socket()
    print('socket created ')
    port = 1234
    s.bind(('127.0.0.1', port)) #bind port with ip address
    print('socket binded to port ')
    s.listen(5)#listening for connection
    print('socket listensing ... ')
    while True:
        c, addr = s.accept() #when port connected
        print("\ngot connection from ", addr)
        de=c.recv(1024).decode("utf-8") #Collect data from port and decode into  string
        print('Getting Data from the Unity : ',de)

        list=de.split(' ') #cominda data in string  so we split into list on basis of space
        value1 = int(list[0])
        value2 = int(list[1])
        value3 = int(list[2])
        print("Value 1 :",value1)
        print("Value 2 :", value2)
        print("Value 3 :", value3)
        #Adding values into that variables to change numbers
        value1 = value1 + 2
        value2 = value2 + 3
        value3 = value3 + 4
        UpdateValue=str(value1)+" "+str(value2)+" "+str(value3)
        c.sendall(UpdateValue.encode("utf-8"))#then encode and send that string back to unity
        c.close()

sending_and_reciveing()#calling the function to run server
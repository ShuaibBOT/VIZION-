#run client on other terminal
import  socket
#from Unity_to_python_socket import server_file
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=1234
s.connect(('127.0.0.1', port))
#s.bind(('127.0.0.1', port))
s.listen(5)
c, addr = s.accept()
print(c.recv(1024))
#s.sendall(b'Thank you for connecting i am hamza here')
s.close()
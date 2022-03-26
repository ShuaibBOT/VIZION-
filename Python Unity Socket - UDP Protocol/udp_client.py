#run client on other terminal
import  socket
#from Unity_to_python_socket import server_file

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO =1234
Message = b"Hello, Server"
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
s.close()
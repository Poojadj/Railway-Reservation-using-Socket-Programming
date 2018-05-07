#python tcp client A
import menu
import socket

host=socket.gethostname()
port=7777
BUFFER_SIZE=2000
#MESSAGE=raw_input("tcpCLientA: enetr mesggage/enter exit:")
tcpCLientA=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcpCLientA.connect((host,port))
menu.menu()
tcpCLientA.close()




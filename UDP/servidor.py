import socket
from socket import *
HOST = '127.0.0.1'              # Endereco IP do Servidor
PORT = 6789                     # Porta que o Servidor esta
udp = socket(AF_INET, SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
print("Bem vindo!")
msg,addr = udp.recvfrom(1024)
arq =  open("arquivo_do_cliente.txt","wb");
try:
    while(msg):
        arq.write(msg)
        udp.settimeout(2)
        msg, addr = udp.recvfrom(1024)
except timeout:
    arq.close()
    udp.close()
print("Download Completo")
#print(len(arq))
arq = open("/Users/PH/Desktop/arquivo_do_cliente.txt","r")

size = 0
for l in arq.readlines():
    size += len(l)
print("Tamanho total: %d " % size)


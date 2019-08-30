import socket
import os
HOST = '127.0.0.1'          # Endereco IP do Servidor
PORT = 6789                 # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

arquivo = open("/Users/PH/Desktop/seila.txt","rb")
byte = arquivo.read(1)
while byte != '':
    udp.sendto (byte, dest)
    byte = arquivo.read(1)
udp.close()




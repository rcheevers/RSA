import socket
import threading
import time

def display(sock):
    while(True):
        print("s")
        msg = sock.recv(1024).decode('UTF-8')
        print("received: ",msg)

def send(sock):
    msg = ""
    while(msg != "quit"):
        msg = input("next message: ")
        sock.send(msg.encode('UTF-8'))
        msg = sock.recv(1024).decode('UTF-8')
        print("from: ",sock,"received: ",msg)
    sock.close

def client():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.sendto("hello".encode('utf-8'),("192.168.15.247",1024))
    data, addr = sock.recvfrom(1024)
    print(data.decode('utf-8'))
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("192.168.15.247",int(data)))

    send(sock)
    #display1 = threading.Thread(target=display,args=(sock,))
    #send1 = threading.Thread(target=send,args=(sock,))

    #display1.start()
    #send1.start()

def two():
    client1 = threading.Thread(target=client)
    client2 = threading.Thread(target=client)
    client1.start()
    time.sleep(10)
    client2.start()
    

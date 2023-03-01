import socket

host = input("Enter target ip/domain")
port = int(input("Enter Port"))

def portscan(host):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connect = s.connect_ex((host,port))
    if(connect == 0):
        print("Port",str(port),"is open")
    else:
        print("Port",str(port),"is close")
        s.close()
portscan(host)
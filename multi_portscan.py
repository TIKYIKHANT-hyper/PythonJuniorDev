import socket,sys

host = input("Enter host: \t")
ip = socket.gethostbyname(host)

open_ports = []
start_port = int(input("Enter Start Port:\t"))
end_port = int(input("Enter End Port:\t"))

def probe_port(host, port, result = 1):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((host,port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

for p in range(start_port,end_port+1):
    response = probe_port(host,p)
    if response == 0:
        open_ports.append(p)
    if not p == end_port:
        sys.stdout.write('\b'* len(str(p)))

if open_ports:
    print("Your target",host,"Ports",open_ports,"is open")
else:
    print("Sorry, No open ports found.!!")
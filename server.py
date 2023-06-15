import socket

s = socket.socket()
host = "192.168.100.122"
port = 8080
s.bind((host,port))
s.listen(1)
print("Waiting for any incoming connections",port)
conn,addr = s.accept()
print(addr,"Has connected to the server")

filename = input("Please enter the filename of the file:")
file = open(filename,'rb')
file_data = file.read(1024)
conn.send(file_data)
print("Data has been transmitted success")
import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("",bluetooth.PORT_ANY))
server_sock.listen(1)

client_sock,address=server_sock.accept()
print("Accepted conn from:",address)

data = client_sock.recv(1024)
print("recieved:",data)
offMsg="OFF"
client_sock.send(offMsg)

client_sock.close()
server_sock.close()

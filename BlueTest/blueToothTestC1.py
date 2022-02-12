import bluetooth

bd_addr="DC:A6:32:1D:83:E0"

port=1
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr,port))

sock.send("hello!!")
data = sock.recv(1024)
if data=="OFF":
	print("shut off")
sock.close()

import bluetooth

number_conn_to_try = 3

target_name = "raspberrypi"
target_address=None

for try_cnt in range(number_conn_to_try):
	nearby_devices = bluetooth.discover_devices()
	for bdaddr in nearby_devices:
		if target_name==bluetooth.lookup_name(bdaddr):
			target_address=bdaddr
			break

	if target_address is not None:
		print("found target with address:", target_address)
		break;
	else:
		print("could not find target")

if target_address is None:
	print("Connection sequence failed")
	quit()

port=1
print("Connecting to address:",target_address)
sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

sock.send("test data")
com_msg=sock.recv(128)
print(com_msg)

sock.close()

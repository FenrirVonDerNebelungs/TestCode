
# NO WARRANTY: USER/DOWNLOADER ASSUMES ALL LIABILITY
# this code may or may not function and is in no way
# guaranteed against causing damage directly or indirectly 

from ctypes import *

tPylib = ctypes.cdll.LoadLibrary("/home/usrname/tobjpyc_lib.so")

tPylib.wrap_init.restype = ctypes.c_void_p

tPylib.wrap_reciv.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
tPylib.wrap_reciv.restype = ctypes.c_void_p

tPylib.wrap_send.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
tPylib.wrap_send.restype = ctypes.c_void_p

#start the program by creating the object
pyCptr = wrap_init()
#initialize the message buffer that will be use to receive msgs
msgbufr = create_string_buffer(100)
msgbufs = create_string_buffer(100)

#reset the buffers with some inital string values
msgbufr.value = b"original recieve values"
msgbufs.value = b"sending message"
#print test values
print(sizeof(msgbufr), repr(msgbufr.raw))
print(sizeof(msgbufs), repr(msgbufs.raw))

#for loop where program does what it does
for cnt_i in range(7):
    print(cnt_i)
    tPylib.wrap_send(pyCptr, msgbufs, 15)
    tPylib.wrap_reciv(pyCptr, msgbufr, 100)
    print("\nrecived msg: ")
    print(sizeof(msgbufr), repr(msgbufr.raw))

#assume that python will automatically clean up the pointer and delete the object
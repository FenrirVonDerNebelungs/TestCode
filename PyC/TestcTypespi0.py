from ctypes import *

msg_buff = create_string_buffer(b"message contents from master")
print(sizeof(msg_buff), repr(msg_buff.value))

#testcode
strchr = libc.strchr
strchr.restype = ctypes.c_char_p
print(strchr(msg_buff, ord("c")))

#objcode
CTest = ctypes.cdll.LoadLibrary("Testctypes.so") #c library

class Foo_Test_PyMod(object):
    def __init__(self,val):
        CTest.wrap_init_foo_test.argtypes = [ctypes.c_void_p]
        CTest.wrap_init_foo_test.restype = ctypes.c_void_p

        #void* wrap_sendMsg(void* ptr, char msg[], int len)
        CTest.wrap_sendMsg.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
        CTest.wrap_sendMsg.restype = ctypes.c_void_p

        #void* wrap_recivMsg(void* ptr, char msg[], int len)
        CTest.wrap_recivMsg.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
        CTest.wrap_recivMsg.restype = ctypes.c_void_p

    def sendMsg(self, msg_pointer, msg_len):
        CTest.wrap_sendMsg(self.obj, msg_pointer, msg_len)

    def recivMsg(self, msg_ret_pointer, msg_max_len):
        CTest.wrap_recivMsg(self.obj, msg_ret_pointer, msg_max_len)


from ctypes import *

CTest = ctypes.cdll.LoadLibrary("Testctypes.so") #c library

#define passing values
#definintions for the init
#CTest.wrap_init_foo_test.argtypes = [ctypes.c_void_p]
CTest.wrap_init_foo_test.restype = ctypes.c_void_p

#void* wrap_sendMsg(void* ptr, char msg[], int len)
CTest.wrap_sendMsg.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
CTest.wrap_sendMsg.restype = ctypes.c_void_p

#void* wrap_recivMsg(void* ptr, char msg[], int len)
CTest.wrap_recivMsg.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
CTest.wrap_recivMsg.restype = ctypes.c_void_p

#assuming cleanup for python will be able to delete the object without any explicit call to deletion

#create the object for use during the program
CObjTest = CTest.wrap_init_foo_test()

testmsg = create_string_buffer(b"test string: hello world")
CTest.wrap_sendMsg(CObjTest, c_char_p(testmsg), 22)

testinmsg  = create_string_buffer(20)
CTest.wrap_recivMsg(CObjTest, c_char_p(testinmsg), 20)
print(sizeof(testinmsg), repr(testinmsg))


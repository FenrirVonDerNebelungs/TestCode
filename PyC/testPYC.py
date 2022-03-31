# NO WARRANTY: USER/DOWNLOADER ASSUMES ALL LIABILITY
# this code may or may not function and is in no way
# guaranteed against causing damage directly or indirectly 

from ctypes import *

CTest = ctypes.cdll.LoadLibrary("/home/usrname/TestPYC.so") #c library

CTest.wrap_msg.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int]
CTest.wrap_msg.restype = ctypes.c_void_p

tmsg  = create_string_buffer("original test buffer")
ptr = 0
print(sizeof(tmsg), repr(tmsg))

retptr = CTest.wrap_msg(ptr, tmsg, 12)
print(retptr)
print(sizeof(tmsg), repr(tmsg))


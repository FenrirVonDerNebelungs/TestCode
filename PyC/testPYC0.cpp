/* NO WARRANTY: USER/DOWNLOADER ASSUMES ALL LIABILITY
this code may or may not function and is in no way
guaranteed against causing damage directly or indirectly */

#include <stdio.h>
#include <iostream>

void recivMsg(char* msg, int maxlen) {
	if (4 < maxlen) {
		msg[0] = 'h';
		msg[1] = 'e';
		msg[2] = 'l';
		msg[3] = 'l';
	}
	std::cout << "filling msg\n";
	return;
}

extern "C"
{
	void* wrap_msg(void* ptr, char* pmsg, int len) {
		recivMsg(pmsg, len);
		return ptr;
	}
}

/* NO WARRANTY: USER/DOWNLOADER ASSUMES ALL LIABILITY
this code may or may not function and is in no way
guaranteed against causing damage directly or indirectly */

#include "tobjPYC.h"

extern "C"
{
	void* wrap_init(void)
	{
		return new(std::nothrow) testPy;
	}
	void* wrap_reciv(void* ptr, char* pmsg, int len) {
		testPy* objptr = reinterpret_cast<testPy*>(ptr);
		if (objptr != NULL)
			objptr->recivMsg(pmsg, len);
		else
			return 0;
		return ptr;
	}
	void* wrap_send(void* ptr, char* pmsg, int len) {
		testPy* objptr = reinterpret_cast<testPy*>(ptr);
		if (objptr != NULL)
			objptr->sendMsg(pmsg, len);
		else
			return 0;
		return ptr;
	}
}

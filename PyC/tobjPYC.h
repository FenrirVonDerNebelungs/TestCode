/* NO WARRANTY: USER/DOWNLOADER ASSUMES ALL LIABILITY
this code may or may not function and is in no way
guaranteed against causing damage directly or indirectly */

#pragma once
#ifndef TOBJPY_H
#define TOBJPY_H
#include <iostream>
#include "tobjPYC_dum.h"

#define TOBJPY_LEN 100

class testPy {
public:
	testPy();
	~testPy();

	void init();
	void release();

	void recivMsg(char* msg, int maxlen);
	void sendMsg(char* msg, int len);
protected:
	dummyPYC* m_dum;
	char* m_msg;
	int   m_len;
	int   m_cnt;
};
#endif

/* NO WARRANTY: USER/DOWNLOADER ASSUMES ALL LIABILITY
this code may or may not function and is in no way
guaranteed against causing damage directly or indirectly */

#include "tobjpyc.h"

testPy::testPy() {
	init();
}
testPy::~testPy() {
	release();
}

void testPy::init() {
	m_dum = NULL;
	m_dum = new dummyPYC();
	m_msg = NULL;
	m_msg = new char[TOBJPY_LEN];
	m_len = 0;
	m_cnt = 0;
}
void testPy::release() {

	m_len = 0;
	m_cnt = 0;
	if (m_dum != NULL)
		delete m_dum;
	m_dum = NULL;
	if (m_msg != NULL)
		delete[] m_msg;
	m_msg = NULL;
}

void testPy::recivMsg(char* msg, int maxlen) {
	if (4 < maxlen) {
		msg[0] = 'h';
		msg[1] = 'e';
		msg[2] = 'l';
		msg[3] = 'l';
	}
	std::cout << "filling msg\n";
	return;
}
void testPy::sendMsg(char* msg, int len) {
	std::cout << "cnt: " << m_cnt << ":  ";
	if (len < TOBJPY_LEN) {
		for (int i = 0; i < len; i++)
			m_msg[i] = msg[i];
		m_len = len;
		for (int i = 0; i < m_len; i++)
			std::cout << m_msg[i];
	}
	std::cout << '\n';
	return;
}
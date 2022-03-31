#include <stdio.h>

class foo_test {
public:
	foo_test();
	~foo_test();

	char* m_charStr;
	int m_msgLen;
	
	void sendMsg(char msg[], int len);
	int getMsgLen() { return m_msgLen; }/*gets the length of the message recived*/
	void recivMsg(char* msg, int maxlen);
};

foo_test::foo_test() {
	m_charStr = NULL;
	m_charStr = new char[100];
	m_charStr[0] = 'h';
	m_charStr[1] = 'e';
	m_charStr[2] = 'l';
	m_charStr[3] = 'l';
	m_charStr[4] = '2';
	m_charStr[4] = '\0';
	m_msgLen = 5;
}
foo_test::~foo_test() {
	if (m_charStr != NULL)
		delete[] m_charStr;
	m_msgLen = 0;
}
void foo_test::recivMsg(char* msg, int maxlen) {
	if (4 < maxlen) {
		msg[0] = 'h';
		msg[1] = 'e';
		msg[2] = 'l';
		msg[3] = 'l';
		m_msgLen = 4;
	}
	return;
}
void foo_test::sendMsg(char msg[], int len) {
	std::cout << '\n';
	for (int i = 0; i < len; i++) {
		std::cout << msg[i];
	}
	std::cout << '\n';
}

extern "C"
{
	void* wrap_init_foo_test(void)/*try without: void pointer is there just for python*/
	{
		return new(std::nothrow) foo_test;
	}
	void* wrap_release_foo_test(void* ptr)
	{
		delete(std::nothrow)ptr;
		return 0;/*returning void pointer just for python*/
	}
	void* wrap_recivMsg(void* ptr, char msg[], int len) {/*returning void* just for python */
		try
		{
			foo_test* foot = reinterpret_cast<foo_test*>ptr;
			foot->recivMsg(msg, len);
		}
		catch (...)
		{
			return 0;
		}
		return 0;
	}
	void* wrap_sendMsg(void* ptr, char msg[], int len) {
		try
		{
			foo_test* foot = reinterpret_cast<foo_test*>ptr;
			return foot->sendMsg(msg, len);
		}
		catch (...)
		{
			return 0;
		}
		return 0;
	}

}
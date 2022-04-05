#include "tobjPYC_dum.h"

dummyPYC::dummyPYC() {
	m_dum = new int[10];
}
dummyPYC::~dummyPYC() {
	if (m_dum != NULL)
		delete[] m_dum;
}
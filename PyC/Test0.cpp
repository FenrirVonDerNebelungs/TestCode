#define PY_SSIZE_T_CLEAN
#include <Python.h>

static char* memhold = NULL;

static char testStr[5] = { 't','e','s','t','.' };

PyMODINIT_FUNC PyInit_footest(void)
{
	PyObject* m;

	return m;
}
static PyObject* footest_init(PyObject* self, PyObject* args) {

}

static char* foo(PyObject* self, PyObject* args)
{
	const char* command;
	if (!PyArg_ParseTuple(args, "s", &command))
		return NULL;
	return PyBytes_AsString(testStr);
}
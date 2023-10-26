#include <Python.h>
/**
* print_python_list_info - print python list info
* @p:python list object
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;

	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
		for (i = 0; i < PyList_Size(p); i++)
		{
			printf("Element %ld: ", i);
			printf("%s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
		}
	}
}

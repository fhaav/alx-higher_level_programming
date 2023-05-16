#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - This function is responsible for
 * presenting essential details regarding Python lists.
 * @p: represents a collection of PyObject objects in the form of a list.
 */

void print_python_list_info(PyObject *p)
{
	long int size = 0;
	int i = 0;
	PyListObject *obj = (PyListObject *)p;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);

	while (i < size)
	{
		printf("Element %d: ", i);
		printf("%s\n", (Py_TYPE(obj->ob_item[i]))->tp_name);
		i++;
	}
}

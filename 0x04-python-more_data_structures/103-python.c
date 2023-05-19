#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list - A function that prints information about Python lists
 * @p: A pointer to the Python object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, alloc, index;
	PyObject *elem;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (index = 0; index < size; index++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
	}
}


/**
 * print_python_bytes - A function that prints information
 * about Python bytes objects
 * @p: A pointer to the Python object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, index;
	char *str = NULL;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");

	for (index = 0; index <= size && index < 10; index++)
		printf("%02x%c", (unsigned char)str[index],
				index == 9 ? '\n' : ' ');
}

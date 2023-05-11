#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int num_nodes; /* number of nodes */

	current = h;
	num_nodes = 0;

	/* loop through the linked list and print each node's value */
	while (current != NULL)
	{	
	printf("%i\n", current->n);
	current = current->next;
	num_nodes++;
	}

	return (num_nodes);
}

/**
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	/* allocate memory for the new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	return (NULL);

	/* set the new node's value and point it to the head of the list */
	new_node->n = n;
	new_node->next = *head;

	/* set the head of the list to the new node */
	*head = new_node;

	return (new_node);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	/* loop through the list, freeing each node as we go */
	while (head != NULL)
	{
	current = head;
	head = head->next;
	free(current);
	}
}

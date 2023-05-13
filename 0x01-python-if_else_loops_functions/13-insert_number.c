#include<stdio.h>
#include<stdlib.h>
#include"lists.h"

/**
 * insert_node - inserts a node with a number into a sorted linked list
 * @head: pointer to the head of the list
 * @number: number to be included in the new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_node;
	listint_t *next_node;

	current_node = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		*head = new_node;
	else
	{
		while (current_node != NULL)
		{
			next_node = current_node->next;

			if (current_node->n >= number)
			{
				*head = new_node;
				new_node->next = current_node;
				break;
			}
			if ((current_node->n < number && next_node && next_node->n >= number) ||
					!next_node)
			{
				current_node->next = new_node;
				if (next_node)
					current_node->next->next = next_node;
				break;
			}
			current_node = current_node->next;
		}
	}

	return (new_node);
}


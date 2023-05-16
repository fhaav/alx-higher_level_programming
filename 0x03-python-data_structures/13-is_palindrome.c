#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * reverse_list - This function is designed to reverse
 * the order of nodes in a linked list.
 *
 * @head: pointer to the first node of the linked list
 * that needs to be reversed.
 * Return: A pointer to the entry point (head) of the reversed linked list.
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome -  validates whether a singly linked list forms a palindrome.
 *
 * @head: A pointer to pointer of first node of listint_t list
 * Return: 0 if the linked list is not a palindrome and
 * 1 if the linked list is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *slow_p = *head;
	listint_t *fast_p = *head;
	listint_t *prev = NULL;
	listint_t *temp = NULL;

	while (fast_p != NULL && fast_p->next != NULL)
	{
		fast_p = fast_p->next->next;

		temp = slow_p;
		slow_p = slow_p->next;
		temp->next = prev;
		prev = temp;
	}

	listint_t *sec_half = (fast_p == NULL) ? slow_p : slow_p->next;

	while (prev != NULL && sec_half != NULL)
	{
		if (prev->n != sec_half->n)
			return (0);

		prev = prev->next;
		sec_half = sec_half->next;
	}

	return (1);
}

#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle
 * @list: A pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle, 0 otherwise
 */

int check_cycle(listint_t *list)
{
listint_t *slow, *fast;
if (!list)
return (0);

slow = list;
fast = list;

while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;

if (slow == fast)
return (1);
}

return (0);
}

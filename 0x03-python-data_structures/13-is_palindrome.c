#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - entry point
 * Description: 'check if list is palindrome'
 * @head: list input
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	int idx = 0, i = 0;
	int arr[100000];
	listint_t *tmp = *head;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	while (tmp)
	{
		arr[idx] = tmp->n;
		idx++;
		tmp = tmp->next;
	}

	for (i = 0; i < idx / 2; i++)
	{
		if (arr[i] != arr[idx - i - 1])
			return (0);
	}

	return (1);
}

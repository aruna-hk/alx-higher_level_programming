#include "lists.h"
/**
* insert_node - insert sorted list
* @head:head of sorted list
* @number: data to insert to the list
* Return: new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	int p;
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *h = *head;

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	while (*head != NULL)
	{
		p = ((*head)->n) - ((*head)->next->n);
		if (p < 0)
		{
			if ((-(p) + (*head)->n) > number)
			{
				new->next = (*head)->next;
				(*head)->next = new;
				*head = h;
				return (new);
			}
		}
		else
		{
			if (((*head)->n - p) < number)
			{
				new->next = (*head)->next;
				(*head)->next = new;
				*head = h;
				return (new);
			}
		}
		*head = (*head)->next;
	}
	return (insert_node(head, number));
}

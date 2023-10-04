#include "lists.h"
/**
* insert_nodeint_at_index - insert node at give index
* @head: ptr to head double
* @idx: index to insert
* @n: value to insert at the give node
* Return:address of new node/NULL
*/
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	listint_t *temp, *new = NULL;
	unsigned int count = 0;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;
	if (head == NULL)
	{
		free(new);
		return (NULL);
	}
	if (idx == 0)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	temp = *head;
	while (temp != NULL)
	{
		if (count == idx - 1)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		count++;
		temp = temp->next;
	}
	free(new);
	return (NULL);
}
/**
* add_node - add node ata the beginning
* @head: pointer to a pointer points to list
* @number: -string to add to string variable in struct
* Return: return null/pointer to addd node
*/
listint_t *add_node(listint_t **head, int number)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	new->next = *head;
	*head = new;
	return (*head);
}
/**
* insert_node - insert sorted list
* @head:head of sorted list
* @number: data to insert to the list
* Return: new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head;
	int p, i = 0;

	if (*head == NULL)
		return (add_node(head, number));
	while (*head != NULL)
	{
		if ((*head)->next == NULL)
		{
			*head = h;
			return (add_nodeint_end(head, number));
		}
		p = ((*head)->n) - ((*head)->next->n);
		if (p < 0)
		{
			if ((-(p) + (*head)->n) > number)
			{
				*head = h;
				if ((*head)->n > number)
					return (insert_nodeint_at_index(head, i, number));
				return (insert_nodeint_at_index(head, i + 1, number));
			}
		}
		else
		{
			if (((*head)->n - p) < number)
			{
				*head = h;
				return (insert_nodeint_at_index(head, i + 1, number));
			}
		}
		i++;
		*head = (*head)->next;
	}
	*head = h;
	return (add_nodeint_end(head, number));
}

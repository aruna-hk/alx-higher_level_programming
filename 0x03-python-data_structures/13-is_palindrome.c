#include "lists.h"
/********************************************
*********************
* check if list is a palindrom
*********************************************
*/
/**
* list_len - finds the len of list
* @list: pointer to head of the list
* Return: len of the list
*/
int list_len(listint_t *list)
{
	int n = 0;

	while (list != NULL)
	{
		n++;
		list = list->next;
	}
	return (n);
}
/**
* getvalue_at_index -  get required value at list index
* @list: pointer to the listt position from where search begin
* @indx: index to locate
* Return: value at given index
*/
int getvalue_at_index(listint_t *list, int indx)
{
	int i = 0;

	while (list->next != NULL)
	{
		if (i == indx)
			break;
		i++;
		list = list->next;
	}
	return (list->n);
}
/**
* is_palindrome- check if a list is palindrome read same from
* both sides
* @head: list head
* Return: 0- if not / 1  if
*/
int is_palindrome(listint_t **head)
{
	int i;
	int len = list_len(*head);
	listint_t *list = *head;

	i = 0;
	if (*head == NULL)
		return (1);
	while (len > i)
	{
		if ((*head)->n != getvalue_at_index(*head, len - 1))
		{
			*head = list;
			return (0);
		}
		len = len - 2;
		i++;
		*head = (*head)->next;
	}
	*head = list;
	return (1);
}

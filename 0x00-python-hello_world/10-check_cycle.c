#include "lists.h"
/**
*check_cycle - check cycle in a linked list
* @list:linked list
* Return: 1-if cycle present 0-if not
*/
int check_cycle(listint_t *list)
{
	long int *p = list;

	if (list == NULL)
		return (0);
	list = list->next;
	if (list == NULL)
		return (0);
	while (list != NULL)
	{
		if ((long int)list == p)
			return (1);
		list = list->next;
	}
	return (0);
}

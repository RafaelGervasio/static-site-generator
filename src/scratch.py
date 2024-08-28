def change_lists(lists):
	cleaned_list = []

	for my_list in lists:
		if my_list == [1, 2]:
			cleaned_list.append("changed!")
		else:
			cleaned_list.append(my_list)

	return cleaned_list


print(change_lists([[1, 2], [1, 2, 3], [1, 2, 3, 4]]))



def increment_two(mylist):
	new_list = []
	for num in mylist:
		if num == 2:
			new_list.append(num + 1)
		else:
			new_list.append(num)

	return new_list


print(increment_two([1, 1, 2, 2, 3, 3]))
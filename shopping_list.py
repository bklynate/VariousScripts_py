shopping_list = []

print("What should we pick up at the store? ")
print("Enter 'DONE' to stop adding items.")

while True:
	new_item = input("> ")

	if new_item == "DONE":
		break

	shopping_list.append(new_item)
	print("Added! Shopping list has {} items.".format(len(shopping_list)))
	
print("Here is your list: ")
for items in shopping_list:
	print(items)
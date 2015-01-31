shopping_list = []

def prompt(words):
	print ("=> {}".format(words))

def show_welcome():
	prompt ("What should we pick up at the store? ")
	prompt ("Enter 'DONE' to stop.")

def show_list():
	prompt("Here is your shopping list")
	for items in shopping_list:
		prompt (items)

def add_to_list(items):
	shopping_list.append(items)
	prompt ("Added! Shopping list has {} items.".format(len(shopping_list)))	


show_welcome()

while True:
	new_items = input("=> ")

	if new_items == "DONE":
		break
	add_to_list(new_items.capitalize())
	continue

show_list()
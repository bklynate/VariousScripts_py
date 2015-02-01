#1. Display instructions on how the "shopping list" works
#2. Have the ability to add items to the shopping
#3. Have the ability to show the current list
#4. Have the ability to print numbered list at the CLOSE of program

shopping_list = []

def prompt(words):
	print ("=> {}".format(words))

def show_welcome():
	prompt ("What should we pick up at the store? ")
	prompt ("Enter 'DONE' to stop. 'HELP' to display directions. 'SHOW' to show current list.")

def show_help():
	prompt ("Enter 'DONE' to stop. 'HELP' to display directions. 'SHOW' to show current list.")

def show_list():
	prompt("Here is your shopping list: ")
	count = 1
	for items in shopping_list:
		prompt("{}. {}".format(count,items))
		count+=1

def add_to_list(items):
	shopping_list.append(items)
	prompt ("Added! Shopping list has {} items.".format(len(shopping_list)))	


show_welcome()

while True:
	new_items = input("=> ")

	if new_items == "DONE":
		break
	elif new_items == "HELP":
		show_help()
		continue
	elif new_items == "SHOW":
		show_list()
		continue
	add_to_list(new_items.capitalize())
	continue

show_list()
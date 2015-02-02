#1. Welcome user and display script instructions.
#2. Accept a word the user wants to remove vowels from.
#3. Loop over the word to detect vowels.
#4. Display the new word with the vowels removed.

def prompt(words):
	print ("=> {}".format(words))

vowels = ['a','e','i','o','u']

prompt("Hello, this program will remove all vowels from the words you input")
prompt("vowels of course are, 'AEIOU'")

user_word = input("Input word: >  ")
user_word_list = list(user_word)

for letters in user_word_list:
	if letters in vowels:
		user_word=user_word_list.remove(letters)
		prompt(user_word)
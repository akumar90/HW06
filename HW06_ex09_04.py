#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: ooh la la
#       2:
#       3:
##############################################################################
# Imports

# Body

def uses_only(word, letterCombination):
	listOfLetters = letterCombination.split(",")

	for char in word:
		if char not in listOfLetters:
			return False

	return True

def get_words(filename,letterCombination):
	with open(filename, 'r') as f:
		listOfWords = []

		for lines in f:
			for words in lines.split():
				if(uses_only(words.strip(),letterCombination)):
					listOfWords.append(words)

	return listOfWords

def form_sentence(listOfWords):
	sentence = []

	while True:
		print
		print
		print
		print ("Valid words : ")
		print (repr(listOfWords))
		
		if sentence:
			print ("Current sentence is : "+repr(fetch_statement(sentence)))
			print
			print
			print

		userInput = raw_input("Pick a word to append to your sentence: ")
		
		if userInput in listOfWords:
			sentence.append(userInput)

		elif userInput == "end_this":
			return sentence

		else :
			print ("Incorrect word entered. Try again or type 'end_this' to complete your sentence")

def fetch_statement(sentence):
	statement = ''
	for words in sentence:
		statement += words + " "

	return statement.strip()
##############################################################################
def main():
	print ("1st Problem")
	print (repr(uses_only("abcbcabcbcba","a,b,c")))
	print
	print ("2nd Problem - Getting all valid words")
	print ("All the valid words are :")
	listOfWords = get_words("words.txt","a,c,e,f,h,l,o")
	print (repr(listOfWords))
	print
	print
	print ("Forming sentence")
	print
	print
	print ("The sentence formed is : "+repr(fetch_statement(form_sentence(listOfWords))))




if __name__ == '__main__':
    main()

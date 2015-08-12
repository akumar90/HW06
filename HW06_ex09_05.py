#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body

def uses_all(word,letterCombination):
	listOfLetters = letterCombination.split(",")

	for letter in listOfLetters:

		if letter.strip() in word:
			pass
		else :
			return False

	return True

def no_of_words(filename, letterCombination):
	with open(filename, 'r') as f:
		count = 0
		for lines in f:
			for words in lines.split():
				if(uses_all(words.strip(),letterCombination)):
					count += 1

	return count


##############################################################################
def main():
	print ("1st problem")
	print(repr(uses_all("ankur","k,a,u,r")))
	print
	print
	print ("2nd problem - Part 1")
	print ("No of words using all vowels i.e. 'a,e,i,o,u' are : "+repr(no_of_words("words.txt","a,e,i,o,u")))
	print
	print
	print ("2nd problem - Part 2")
	print ("No of words containing all the following characters - 'a,e,i,o,u,y' are : "+repr(no_of_words("words.txt","a,e,i,o,u,y")))

if __name__ == '__main__':
    main()
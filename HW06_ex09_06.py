#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words:
##############################################################################
# Imports

# Body

def is_abecedarian(word):
	for i in range(len(word)-1):
		if ord(word[i]) > ord(word[i+1]):
			return False

	return True

def no_of_words(filename):
	with open(filename, 'r') as f:
		count = 0
		for lines in f:
			for words in lines.split():
				if(is_abecedarian(words.strip())):
					count += 1

	return count

##############################################################################
def main():
	print ("1st problem")
	print (repr(is_abecedarian("abcdegjkz")))
	print
	print
	print ("2nd Problem")
	print ("Number of words which have letters in alphabetical order are : "+repr(no_of_words("words.txt")))

if __name__ == '__main__':
    main()

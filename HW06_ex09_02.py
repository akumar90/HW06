#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body

def has_no_e_old(word):
	
	if ('e' in word or 'E' in word):
		return False

	return True

def has_no_e(listOfWords):
	lengthOfList = len(listOfWords)

	count = 0

	for word in listOfWords:
		if(has_no_e_old(word.strip())):
			print (word.strip() +"\n")
			count += 1

	print ("Count of numbers without 'e' : "+repr(count))
	print ("Total number of words : "+repr(lengthOfList))
	print ("percentage of words that have no 'e' : "+repr((float(count)/lengthOfList) * 100) +"%")


##############################################################################
def main():
    print ("9.1")
    has_no_e_old("Ankur")
    print
    print

    print("9.2")
    has_no_e("This is a sentence to test the second problem which prints words with no 'e'".split())



if __name__ == '__main__':
    main()

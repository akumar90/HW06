#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
from collections import Counter
import operator
# Body

# Problem number 1
def avoids(word, forbiddenLetters):
	for letter in forbiddenLetters:
		if letter.lower() in word.lower():
			return False

	return True


# Problem number 2
def avoids_for_second(filename): # the words are fetched from the file

	forbiddenLetters = raw_input("Enter a string of forbidden letters, separated by comma (,) :")
	count  = 0

	with open(filename, 'r') as f:
		for line in f:
			for words in line.split():
				if(avoids(words.strip(),forbiddenLetters)):
					print (words.strip())
					count += 1

	print ("Number of words that do no contain '{forbiddenLetters}' are : ".format(forbiddenLetters = forbiddenLetters)+repr(count))



# Problem number 3
def forbiddenLetter_combo(filename):

	counter = Counter({'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0})

	with open(filename, 'r') as f:

		for lines in f:
			for words in lines.split():
				counter.update(set(words.strip()))

	counter  = counter.most_common()[-5:]

	# counter.items()
	combo = ''
	for i in range(len(counter)):
		combo += counter[i][0] + ", "

	print ("Combination of letters : "+combo[:-2])

# This solution is more appropriate than the last one
# Because this takes into account only one occurence of a letter per word,
# while using counter counts all the occurences of any letter in any word.
# This should not be the case because if a word contains even one occurence of any forbidden letter
# thw word is excluded. Hence counting multiple occurences in the same word will yield incorrect results.
def forbiddenLetter_combo_2(filename):

	d = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}

	with open(filename, 'r') as f:

		for lines in f:
			for words in lines.split():

				for letter in d:
					if letter in words.strip():
						d[letter] += 1

		
		sorted_x = (sorted(d.items(), key=operator.itemgetter(1)))[:5]

		combo = ''
		for i in range(len(sorted_x)):
			combo += sorted_x[i][0] + ", "

		print ("The required combination which will exclude the minimum number of words is : "+ repr(combo[:-2]))
		

##############################################################################
def main():
	print ("1st Problem")
	print (repr(avoids("Python Boot camp","a,b,c")))
	print
	print
	print ("2nd Problem")
	avoids_for_second("words.txt")
	print
	print
	print ("3rd Problem - Solution 1")
	forbiddenLetter_combo("words.txt")
	print
	print
	print ("3rd Problem - Solution 2")
	forbiddenLetter_combo_2("words.txt")

if __name__ == '__main__':
    main()

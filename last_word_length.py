'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.

Difficulty: Easy

Solution notes:
Take care to note the case where the string is something like "apple orange   ".
This should return the length of 'orange' (6), but if you simply split using ' ' as a delimiter
and return the length of [-1] of that list, it'll incorrectly return 0.
An even shorter solution taking advantage of Python's built in whitespace stripping is

def length_of_last_word(s):
  return len(s.rstrip(' ').split(' ')[-1])

O(n) time
O(1) space
'''

def last_word_length(s):
	# create array splitting at ' '
	word_array = s.split(' ')
	# create new array for words with no spaces; account for multiple ' '
	no_spaces = [word for word in word_array if word != ' ']
	# if there exists words then return last indexed word
	if len(no_spaces) > 0:
		return len(no_spaces[-1])
	else :
		return 0

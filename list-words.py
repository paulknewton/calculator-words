# Python program to show words that can be printed on a calcualtor
# by entering digits and turning the calculator upside down
#
# e.g. hello, boobies...
#
# To run, it needs a dictionary as input
# e.g.
# aspell -d fr dump master | aspell -l fr expand | unaccent ISO-8859-1 | python list-words.py | sort
#
# If other languages are needed, change 'en' to another ISO code
# The 'expand' option is needed to expand variations of words
#

calculatorLetters = {
	'o':'0',
	'l':'1',
	'i':'1',
	'z':'2',
	'e':'3',
	'h':'4',
	's':'5',
	'g':'6',
	'l':'7',
	'b':'8'
}

# can a word be encoded on a calculator?
def isEncodable(x):
	s1 = set(x);
	s2 = set(calculatorLetters.keys());
	return s1.issubset(s2)

# return the digits required to show the word (in reverse order)
def encode(x):
	return x.translate(str.maketrans(''.join(calculatorLetters.keys()), ''.join(calculatorLetters.values())))[::-1]

def encodeAndPrintIt(x):
	print("%s -> %s" % (x, encode(x)))

	

# process a fixed list of words
#validWords = filter(isEncodable, [ 'hello', 'goodbye', 'boobies'])
#map(encodeAndPrintIt, validWords)

import sys
#sys.exit()


# read a word at a time
while True:
	try:
		line = input()
	except EOFError:
		break
	for word in line.split():
		if isEncodable(word):
			encodeAndPrintIt(word)

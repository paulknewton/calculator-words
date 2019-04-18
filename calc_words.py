# Python program to show words that can be printed on a calcualtor
# by entering digits and turning the calculator upside down
#
# e.g. hello, boobies...
#
# To run, it needs a dictionary as input
# e.g.
# aspell -d fr dump master | aspell -l fr expand | unaccent ISO-8859-1 | python calc_words.py | sort
#
# If other languages are needed, change 'en' to another ISO code
# The 'expand' option is needed to expand variations of words
#

calculator_letters = {
    'o': '0',
    'l': '1',
    'i': '1',
    'z': '2',
    'e': '3',
    'h': '4',
    's': '5',
    'g': '6',
    'l': '7',
    'b': '8'
}


# can a word be encoded on a calculator?
def is_encodable(x):
    s1 = set(x);
    s2 = set(calculator_letters.keys());
    return s1.issubset(s2)


# return the digits required to show the word (in reverse order)
def encode(x):
    return x.translate(str.maketrans(''.join(calculator_letters.keys()), ''.join(calculator_letters.values())))[::-1]


def encode_and_print_it(x):
    print("%s -> %s" % (x, encode(x)))


if __name__ == "__main__":
    while True:
        try:
            line = input()
        except EOFError:
            break
        for word in line.split():
            if is_encodable(word):
                encode_and_print_it(word)

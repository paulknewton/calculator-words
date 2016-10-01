# calculator-words
Find words that can be entered on a calculator (by turning the calculator upside down)

My sone recently got an old school calculator. We had a lot of fun entering some numbers and showing him how it would read like a word when you turned the calculator upside down. It took me back to my youth!

We looked on the internet for a f ew other examples words (including some rude ones of course!). But it crossed my mind that this would be the sort of thing that could be automated.

This is written in Python because i) it is an elegant language; and ii) it has good support for Sets and other collections which is what I needed. iii) I was pretty sure I could get the main algorithm down a really short and concise set of set operations (which I did)

It starts with a dictionary (in the Python sense) of the valid letters that a calculator can reproduce. Let's call this our 'calculatorLetters'. These are the letters that can be represented by entering digits and rotation the calculator screen.

The basic algorithm is to read through each word in the dictionary (I use the UNIX 'aspell' dictionary but any input wordslist will do) and see if this is can be encoded on our calculator. The candidate word is converted to a set (i.e. discards any repeating letters). We then check if this is a subset of our encodable characters. As long as we can encode each letter, we know this is a word that will work.

All that is left to is to encode the word as a series of numbers (by looking up each letter in our 'calculatorLetters' map) and print it to the screen (remember the digits need to reversed...)

I've included a list of words that I could find using my english, french and german dictionaries (words-en.txt, words-fr.txt, words-de.txt). Once I had the lists, I manually edited them down to only keep words that would make sense for my son.

Overall, it isn't a complex program, but it gave me a refresher in Python (dictionaries, sets etc).


To run the program (assuming you have 'aspell' and 'unaccent' installed):

aspell -d fr dump master | aspell -l fr expand | unaccent ISO-8859-1 | python list-words.py | sort

Note how this uses the 'expand' feature of aspell to list all variations of words, and also strips out any messy accented characters using the 'unaccent' program. You won't need this for English words, but you will for French and German, otherwise the list of matching words starts to shrink too much.

If you have another dictionary - or just a list of words in a file - you can pipe any content into the program. I don't assume a new word per line - it anyway splits the input lines into separate words.

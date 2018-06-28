##  word stemming
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]

"""for w in example_words:
    print(ps.stem(w))
"""

text = "It is not the employees fault if such jobs exists, in fact it is the employer who has to define the correct boundries of the work place"

words = word_tokenize(text)

for w in words:
    print(ps.stem(w))
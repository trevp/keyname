
from pgp_words import even_words, odd_words
import random

r = random.Random()
chosen_words = []
for x in range(8):
	chosen_words.append(r.choice(even_words))
	chosen_words.append(r.choice(odd_words))
print(" - ".join(chosen_words))
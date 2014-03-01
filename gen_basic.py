
"""
s = open("diceware.words").read()
s2 = s.split("\n")
s3 = [s[6:] for s in s2]
print '",\n"'.join(s3)
"""


from basic_english_words import words
import random

r = random.Random()
chosen_words = []
for x in range(13):
	chosen_words.append(r.choice(words))
print(" - ".join(chosen_words))
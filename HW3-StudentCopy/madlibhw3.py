# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk 
import random

nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize
from nltk.book import text2

# debug = False #True
# if debug:
	# print ("Getting information from file madlib_test.txt...\n")

tokens = text2[0:150]
# print('Tokens:')
# print(tokens)
# tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print('\n')
# print("Tagged Tokens")
# print(tagged_tokens)
# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:5]:
# 		print (tup)

def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

t_list = []
for t in tokens:				#for each token (t) in tokens
	t_list.append(spaced(t))	#apply the spaced definition to that token, and append it to t_list

print("START*******")
print ("".join(t_list))		#print each item in t_list together as a string


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective","ADV":"an adverb"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1,"ADV":.1}

tagged_tokens = nltk.pos_tag(tokens)

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))


print("\n\nEND*******")

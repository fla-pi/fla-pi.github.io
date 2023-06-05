import nltk
from nltk.corpus import wordnet as wn



from pprint import pprint
pprint(wn.synset('feeling.n.01').tree())

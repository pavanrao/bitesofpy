import itertools
import os
import urllib.request
import re

# PREWORK
TMP = os.getenv("TMP", "/tmp")
DICT = 'dictionary.txt'
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{DICT}',
    DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    words = _get_permutations_draw(draw)
    possible_dict_words = [word for word in words if word in dictionary]
    return possible_dict_words


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    #p = re.compile('[^A-Z]*') 
    #draw = re.sub('[\W_]+', '',draw.lower())
    draw = [_.lower() for _ in draw]
    words = set()
    for r in range(len(draw)):
        for word in itertools.permutations(draw, r):
            words.add(''.join(word))
    return words

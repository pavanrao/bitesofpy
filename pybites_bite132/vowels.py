import re
from collections import Counter
# VOWELS = list('aeiou')
VOWELS = 'aeiou'


def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
    Return a tuple of the matching word and the vowel count, e.g.
    ('object-oriented', 6)"""
    vowel_count = {}
    for word in text.lower().split(' '):
        # re.subn returns the count of overlapping replacements  
        vowel_count[word] = re.subn(f'[{VOWELS}]', '', word)[1]
    return Counter(vowel_count).most_common()[0]

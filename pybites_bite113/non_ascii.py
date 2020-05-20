
def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    non_ascii = set()
    for word in text.split():
        for letter in word:
            if ord(letter) < 40 or ord(letter) > 127:
                non_ascii.add(word)
    return list(sorted(non_ascii))

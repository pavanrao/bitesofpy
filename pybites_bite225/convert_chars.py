PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    def scase(char): return char if char not in 'PYBITESpybites' else char.swapcase()
    return ''.join([scase(char) for char in text])

HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    str_val = str(value)
    fill_length = column_length - len(str_val)
    return fill_char*fill_length + str_val
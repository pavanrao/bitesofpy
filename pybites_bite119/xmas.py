def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree = ''
    max_width = rows*2 - 1
    for i in range(rows):
        line_width = (i+1)*2 - 1
        line = '*' * line_width
        tree = tree + line.center(max_width) + '\n'
    return tree.strip('\n')

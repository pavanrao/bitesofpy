from collections.abc import Iterable


def _flatten(l,ret):
    for i in l:
        if isinstance(i, Iterable) and type(i) is not str:
            _flatten(i,ret)
        else: 
            ret.append(i)
    return ret

def flatten(l):
    ret = []
    return list(_flatten(l,ret))

if __name__ == "__main__":
    inp = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
    inp2 = ['a', 'b', [1, 2, 3],
           ['c', 'd', ['e', 'f', ['g', 'h']]],
           [4, [5, 6, [7, [8]]]]]
    inp3 = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
    print(list(flatten(inp)))
    print(list(flatten(inp2)))
    print(list(flatten(inp3)))

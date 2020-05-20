# from packaging import version
# packaging is not installed in pybites

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = _get_pkg_dict(old_reqs)
    new = _get_pkg_dict(new_reqs)
    return [
       key for key in old 
       if _split_v(old[key]) < _split_v(new[key])
    ]


def _get_pkg_dict(reqs: str) -> dict:
    return dict(
       line.split('==')
       for line in reqs.strip().splitlines()
    )


def _split_v(v: list) -> list:
    """
    Splits a string of numbers separated by '.' 
    and returns a list of ints
    Alternative : use from distutils.version import StrictVersion
    """
    return list(map(int, v.split('.')))

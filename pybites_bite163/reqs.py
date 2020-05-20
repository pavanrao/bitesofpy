from packaging import version

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = {req.split('==')[0]: req.split('==')[1] for req in old_reqs.strip().split('\n')}
    new = {req.split('==')[0]: req.split('==')[1] for req in new_reqs.strip().split('\n')}
    return [
       key for key in old 
       if version.parse(old[key]) < version.parse(new[key])
    ]

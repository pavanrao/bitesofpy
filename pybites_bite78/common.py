def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    # convert each dict values to set and create a list of sets
    # unpack the list and pass to set.intersection
    return set.intersection(* [set(langs) for langs in programmers.values()])
        

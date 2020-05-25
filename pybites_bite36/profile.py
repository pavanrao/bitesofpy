def get_profile(name, age, *sports, **awards):
    if not name:
        raise TypeError('Error: missing required argument: name')
    if not isinstance(age, int):
        raise ValueError('Error: required argument age should be an integer')
    if len(sports) > 5:
        raise ValueError('Error: get_profile accepts 5 or less optional arguments')
    ret = dict()
    ret['name'] = name
    ret['age'] = age
    if sports: ret['sports'] = sorted(list(sports))
    if awards: 
        ret['awards'] = awards
    return ret
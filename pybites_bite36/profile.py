def get_profile(name, age, *args, **kwargs):
    if not name:
        raise TypeError('Error: missing required argument: name')
    if not isinstance(age, int):
        raise ValueError('Error: required argument age should be an integer')
    if len(args) > 5:
        raise ValueError('Error: get_profile accepts 5 or less optional arguments')
    ret = dict()
    ret['name'] = name
    ret['age'] = age
    if args: ret['sports'] = sorted(list(args))
    if kwargs: 
        ret['awards'] = {key:value for key, value in kwargs.items()}
    return ret
def generate_affiliation_link(url):
    ''' Returns pybytes affiliation link from an Amazon linu
    '''
    base_url = 'http://www.amazon.com/dp/'
    tag = '/?tag=pyb0f-20'
    id = url.split('/')[5]
    return F'{base_url}{id}{tag}'

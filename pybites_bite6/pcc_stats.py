"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request

from itertools import tee

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

# users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


def gen_files(f):
    """Return a generator of dir names reading in tempfile

       tempfile has this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    return (line.strip('\n').split(',')[0] 
            for line in f 
            if line.strip('\n').split(',')[1] == 'True' 
            )


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
        made the most PRs (ignoring the users in IGNORE) and a challenge tuple
        of most popular challenge and the amount of PRs for that challenge.
        Calling this function on the dataset (held tempfile) should return:
        Stats(user='clamytoe', challenge=('01', 7))
    """
    f = open(tempfile, 'r')
    # Send a file handler to gen_files to get a generator of directories
    dirs = gen_files(f)

    # Use itertools.tee to split dir iterable into 2 iterators
    dir1, dir2 = tee(dirs, 2)

    #Now we can Count on 2 copies of iterators
    users = Counter((line.split('/')[1] for line in dir1 if line.split('/')[1] not in IGNORE))
    bites = Counter((line.split('/')[0] for line in dir2))
    f.close()
    return Stats(users.most_common()[0][0], bites.most_common()[0])


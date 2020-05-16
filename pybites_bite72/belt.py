from itertools import takewhile
scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = dict(zip(scores, belts))


def get_belt(user_score):
    badges = list(takewhile(lambda x:x <= user_score, HONORS.keys() )  )
    if len(badges):
        return HONORS[badges[-1]]
    else:
        return None
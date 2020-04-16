from pytz import timezone, utc
import datetime 

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    naive_dt = naive_utc_dt.replace(tzinfo = utc)
    aus_dt = naive_dt.astimezone(AUSTRALIA).replace(tzinfo=None)
    es_dt = naive_dt.astimezone(SPAIN).replace(tzinfo=None)
    return aus_dt, es_dt
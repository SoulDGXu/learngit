import datetime
print('Now is %s' % datetime.datetime.now())
today = datetime.date.today()
print('Last weekday is ', today - datetime.timedelta(7))

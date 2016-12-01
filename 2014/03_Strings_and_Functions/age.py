import datetime as dt

my_birthday = dt.datetime(1988,2,14)
today = dt.datetime.now()

diff = today - my_birthday


print diff

diff_hours = diff * 24

print diff_hours

future = today + 1000

print future
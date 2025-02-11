import datetime
def date_diff_in_Seconds(date2, date1):
  delta = date2 - date1
  return delta.days * 24 * 3600 + delta.seconds
x=datetime.datetime(2020,10,5,7,45,12)
y=datetime.datetime(2022,4,14,7,47,52)
print(date_diff_in_Seconds(y,x))


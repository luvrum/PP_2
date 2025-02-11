from datetime import date, timedelta
date = date.today() + timedelta(1)
date1=  date.today() - timedelta(1)
print('Current Date :',date.today())
print('Tomorrow :',date)
print('Yesterday:' , date1)

from datetime import date
from dateutil.relativedelta import relativedelta

bday = date(1973, 6, 12)
def ager(bday):
    today = date.today()


    age = relativedelta(today, bday)

    return age.years

x = ager(bday)
print (type(x))
print ("Age",x)

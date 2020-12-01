# 1
import calendar as c
m,y = map(int, eval(dir()[0])[0].split("-"))

while 1:
    y += m>11
    m = m%12 + 1
    if c.weekday(y,m,1)<1:
        return f'{m:02}-{y}'


# 2
import calendar

def regularMonths(currMonth):
    day = 1
    month, year = currMonth.split('-')
    month, year = int(month), int(year)
    while day != 0:
        if month == 12:
            year+=1
            month=1
        month+=1
        day = calendar.weekday(day=1, month=month, year=year)
    return f"{month:0>2}-{year}"
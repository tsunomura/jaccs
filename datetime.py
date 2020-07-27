import datetime

def last_day_of_month(any_day):
    """Get dates and months, not time."""
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    return next_month - datetime.timedelta(days=next_month.day)

def getOnlyDate(strdatetime):
    """Convert string to date only."""
    if strdatetime:
        dt = datetime.datetime.strptime(strdatetime, '%Y/%m/%d')
        return dt.date()
    return ''

def getLastDayOfMonth(strdatetime):
    """Convert string to last date of month."""
    return last_day_of_month(getOnlyDate(strdatetime))

def getStrYearMonth():
    """Get year month in string."""
    strYM = datetime.date.today().strftime('%Y') + datetime.date.today().strftime('%m')
    return strYM

def getStrDate():
    tdatetime = datetime.datetime.now()
    tstr = tdatetime.strftime('%Y%m%d')
    return tstr

FIRST_DAY_THIS_MONTH = datetime.date.today().replace(day=1)
LAST_DAY_THIS_MONTH = last_day_of_month(datetime.date.today())

FIRST_DAY_NEXT_MONTH = LAST_DAY_THIS_MONTH + datetime.timedelta(1)
LAST_DAY_NEXT_MONTH = last_day_of_month(FIRST_DAY_NEXT_MONTH)

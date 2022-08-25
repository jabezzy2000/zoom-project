import datetime

def format_date(date):
    date_list = date.split(sep="-")
    return list(map(int, date_list)) #returns a list of date list characters passed through int func

def format_time(time):
    time_list = time.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):
    # returning the form : YY, MM, DD, HH, MM
    return datetime.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])
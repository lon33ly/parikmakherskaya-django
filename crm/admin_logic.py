import datetime


def add_days(start_date, days):
    dates_list = []
    for i in range(days):
        new_date = start_date + datetime.timedelta(days=i+1)
        dates_list.append(new_date)

    return dates_list

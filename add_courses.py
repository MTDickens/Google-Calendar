from beautiful_date import *
from datetime import timedelta, date
from gcsa.event import Event, date, datetime
from gcsa.google_calendar import GoogleCalendar
import chinese_calendar


def main():

    my_email = "mtdickens1998@gmail.com"
    calendar = GoogleCalendar(my_email)

    # Summary format
    def summary_format(name, count):
        return f"{name}: Lec {count}"

    ## Course information
    course_name = "Complex analysis"

    start_date = (18/Sept/2023)[0]
    tot_count = 35  ## total count of lectures
    duration = 1.5  ## duration of one lecture

    is_default_first_course_index = True ##  whether to 1 or the value below
    first_course_index = 1  ## the index of first lecture that you want to add

    exception_days = ['Sunday']
    exception_dates = []
    exception_dates_check = lambda date: chinese_calendar.get_holiday_detail(date)[1] != None ## real-time check
    ## '!= None' means this date is NOT a special holiday (i.e. just normal weekday or weekend)

    # Aliases
    day = timedelta(days=1)
    hours = timedelta(hours=duration)

    # Main loop for adding courses
    for i in range(1 if is_default_first_course_index else first_course_index, tot_count + 1):
        ## skip the exception days/dates
        while (start_date.strftime('%A') in exception_days
            or start_date in exception_dates
            or exception_dates_check(start_date)):
            start_date += day

        calendar.add_event(
            Event(
                summary=summary_format(course_name, i),
                start=start_date,
                end=start_date + hours
            )
        )

        ## loop to the next day
        start_date += day

if __name__ == '__main__':
    main()
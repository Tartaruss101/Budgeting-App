import calendar
import os
from html.parser import HTMLParser

file_path = os.getcwd() + "\\Python Projects\\Budget App\\calendar.html"

Calendar_String = calendar.HTMLCalendar(calendar.SUNDAY).formatyear(2020, 4)



month_calendar = open(file_path, "w")
month_calendar.write(Calendar_String)
month_calendar.close()


calender_parser = HTMLParser()
calender_parser.feed(Calendar_String)
calender_parser.close()

quit()
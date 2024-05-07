from datetime import datetime

my_data_string = "Feb 25 1988 10:45PM"

datetime_object = datetime.strptime(my_data_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)

print('--------------------------')

from dateutil import parser

date_time = parser.parse('Feb 25 1988 10:53AM')

print(date_time)
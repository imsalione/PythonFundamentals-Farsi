from datetime import datetime

my_data_string = "Mar 11 2024 10:45PM"

datetime_object = datetime.strptime(my_data_string, '%b %d %Y %I:%M%p')

print(type(datetime_object))
print(datetime_object)
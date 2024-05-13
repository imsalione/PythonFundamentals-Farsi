from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUEUSDAY = 2
    WNDNESDAY = 3

# print the enum number 
print(Day.MONDAY)

# get the name of the enum number
print(Day.MONDAY.name)

# get the value of the enum number
print(Day.MONDAY.value)
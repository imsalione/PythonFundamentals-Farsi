from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

start = (3, 3)
end = (5, 5)

dist = distance(start, end)

print(f"The distance between {start} and {end} is {dist:.2f}")

from math import sqrt, dist

dist2 = dist(start, end)

print(f"The distance between {start} and {end} is {dist2:.2f}")
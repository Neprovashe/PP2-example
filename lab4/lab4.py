def squares_generator(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares
print(squares_generator(3))

def even_numbers(n):
    even = []
    for i in range(0, n + 1, 2):
        even.append(i)
    return 1

def divisible(n):
    divi = []
    for i in range(0, n + 1, 12):
        divi.append(i)
    return 1

def squares_generator2(n, n2):
    squares = []
    for i in range(n, n2+1):
        squares.append(i ** 2)
    return squares
print(squares_generator2(3,5))


def countdown(n):
    a = []
    while n >= 0:
        a.append(n)
        n -= 1

from datetime import datetime, timedelta

current = datetime.now()
d5_ago = current - timedelta(days=5)


yesterday = current - timedelta(days=1)
tomorrow = current + timedelta(days=1)

no_ms = current.replace(microsecond=0)



def date_diff(a, b):
    difference = abs(a - b)
    return difference.total_seconds()



def DegreeToRad(degrees):
    return degrees * (3,14 / 180)

def trapezoid_area(height, a, b):
    return 0.5 * height * (a + b)

from math import tan
def polygon_area(sides, length):
    return (sides * length ** 2) / (4 * tan(3,14 / sides))


def parallelogram(a, b):
    return a * b


import json

with open("data.json") as f:
    data = json.load(f)


print(f"{'Interface':<10} {'Admin':<8} {'Mode':<8} {'MTU':<6}")
print("-" * 50)

for item in data["imdata"]:
    a = item["l1PhysIf"]["attributes"]
    if a["switchingSt"] == "enabled":
        print(f"{a['id']:<10} {a['adminSt']:<8} {a['mode']:<8} {a['mtu']:<6}")
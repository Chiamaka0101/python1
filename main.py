#module (importing functions)

from message import get_user_name
import platform
from message import user
import datetime
import math
import json

from maths.geometry import area_circle, area_rectangle
from maths.algebra import add, multiply


from manager import Manager
from developer import Developer

from rest import Calculator

from bank import BankAcount

# print(get_user_name("Chiamaka"))

# pf = platform.system()

pf = dir(platform)
# print(pf)


# print(user["gender"])

us = json.dumps(user)  #convert to json file
# print(us)
# print(type(us))

dt = datetime.datetime.now()
#print(type(dt))
# print(dt.day)
# print(dt.strftime("%A"))
# print(dt.strftime("%dth"))


#print(math.sin(0.5))
# print(pow(2, 5))

# number = max(55, 72, 13, 0, 5, 16, 103)
# print(number)

product = '{"name":"David", "age":26, "city":"Abuja"}'
pdc = json.loads(product)

# print(pdc)
# print(type(pdc))


# print(add(7, 3))

# print(area_circle(12))




# emp1 = Manager("Shera", 2000, "IT")
# emp2 = Developer("Amaka", 1500, "Python")

# emp2.show_details()
# print()

# calc = Calculator()
# print(calc.add(8, 7))
# print(calc.add(8, 7, 5, 10))
# print(calc.add(8, 7, 10, 10))


# employees = [
#   Manager("Gift", 4500, "HR"),
#   Developer("Sofia", 6000, "Python")
# ]

# for emp in employees:
#   print(f"{emp.name}'s Bonus: {emp.calculate_bonus()}")


acc = BankAcount("Prince", 4500)
acc.deposit(45000)
print(acc.get_balance())





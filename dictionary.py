car = {
  "brand":"Toyota",
  "model":"Corolla",
  "year":2020,
  "automatic_transmission":True,
  "colors":["burungdy","white","black"]
}

# print(car)

# print(len(car))
# print(type(car)) #dictionary 

# # to get a single value
# print(car.get("model"))

# # to get all the keys as a list
# print(car.keys())

# # or
# ky = car.keys()
# print(ky)


# # assign a new value
# car["tinted"] = ["factory", "grade 0", "grade 1"]
# print(ky)
# print(car)


# # to get all value
# car_values = car.values()
# print(car_values)


# print(car.items())  #items


# # updating the value in key
# if "year" in car:
#   car["year"] = 2030

#   print (car)


# #remove items in a dictionary
# # car.pop("model")

# #or
# del car["brand"]

# # del car  this deletes the entire dictionary
# print(car)



# # to loop thru  each becomes a string
# for x in car:
#   print(x) 


# for x in car:
#   if x.startswith("y"):
#     result = x.upper()
#     print(result)


# # to loop thru the values each becomes a string
# for value in car.values():
#   print(value)
   

# # to loop thru the keys each becomes a string
# for key in car.keys():
#   print(key)
   
# # make a copy of the dictionary
# mycopy = car.copy()
# print(mycopy)

# my_copy = dict(car)
# print(my_copy)


user1 = {
  "name":"Amaka",
  "gender":"female"
}

user2 = {
   "name":"Jennica", "gender":"female", "skills":["HTML", "CSS", "JAVASCRIPT", "TIKTOK"]}

user3 = {
   "name":"Precious", "gender":"female"}

users = {"first": user1, "second":user2, "third":user3} 

print(users)

# to access user1 name
print(users["second"]["skills"][3])








class Info():
  greet = "How are you doing?"

# print(Info)

info1 = Info()
# print(info1.greet)



class Person():
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName

  def __str__(self):
    return f"FullName: {self.firstName} {self.lastName}"
  
  # def user_details(self):
  #   return f"FullName: {self.firstName} {self.lastName}"
  
  

p1 = Person("Chiamaka", "Uzoho")
p2 = Person("David", "Hangieor")
p1.lastName = "Okeke" #modify an object
# print(p1.firstName)
# print(p1.lastName)

print(p2)



#create a laptop class with different objects
class Laptop():
  def __init__(name, Brand, Color, RAM, Year):
    name.Brand = Brand
    name.Color = Color
    name.RAM = RAM
    name.Year = Year

  def __str__(name):
    return f"My laptop is: {name.Brand} {name.Color} {name.RAM} {name.Year}"

    #create the object and pass the fields
l1 = Laptop("ASUS Notebook", "Deep Blue", "128GB RAM", 2018)
l2 = Laptop("HP", "Dove Gray", "256GB RAM", 2022)
l3 = Laptop("MacBook Air", "Black", "128GB RAM", 2025)
l4 = Laptop("ASUS Chromebook", "Ash", "484 RAM", 2023)
l5 = Laptop("ASUS Notebook", "Deep Blue", "128GB RAM", 2020)
# print(l1)
# print(l2)
# print(l3)
# print(l4)
# print(l5)



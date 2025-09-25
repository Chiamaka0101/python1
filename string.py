#a string is a sequence of character. example "Damilola" ''
#to access first element in a string
name = "King"
#print(name[0])

#How does python memory work in handling strings and other data structures(list, tuples, dictionaries)



sentence = """
This is the car I want to buy in the future
I really love it 
It is beautiful!

"""
#print(sentence)

school = "aptech port harcourt"  #to print every singlen character, use for loop

for x in school:
  print(x)

print(len(school)) #length of the string

#to check if part of exists
if "port" in school:
  print("please specify which of the port? ")
else:
  print("Port does not exist")


#to slice a string
message = "This is the place"
print(message[:13])  #dont slice with a tuple()
print(message[7:])
print(message[-5:-2])

print(message.upper())  #print upper or lowercase
print(message.lower())   



msg = "        hello" #whitespaces are counted
print(len(msg))
print(len(msg.strip())) #remove whitespaces


ex = "Uche, Bimbo, Mario"
print(ex.replace("Bimbo", "Ada")) #replace an item in a string

newStr = ex.split(",") #convert string to list
print(type(newStr))
print(newStr)


#concatenation "+"


#formatting a string
friend = "Zion"
print(f"My friend's name is {friend.upper()}")  #or

txt = f"{friend} is a boy"
print(txt)


price = 45
txt2 = f"the current price is {price: .2f} naira"
print(txt2)


#arithmetic
quantity = 3
unit_price = 400
total_sale = f"Total: {quantity * unit_price}"
print(total_sale)


#to capitalize first letter
user_name = "daniel"
print(user_name.capitalize())


#count how many times a letter appears
user_name = "daniel dog door"
print(user_name.count('d',0))


print(user_name.endswith("door")) #if a string ends with something

#check if string is alphabetic or numeric or both
account_number = "Chiamaka"
print(account_number.isnumeric())



#reverse a string
def reverseStr(str):
  return str[::-1]

print(reverseStr("hello"))

#write python to verify if a given string is a palindrome
def isPalindrome(str):
  new_str = str.lower()
  return new_str[::-1] == new_str

print(isPalindrome("EBube"))


#write a python program to return vowels
def vowel_count(str):
  vowels = "aeiouAEIOU"

  return sum(1 for char in str if char in vowels)

print(vowel_count("Amaka"))
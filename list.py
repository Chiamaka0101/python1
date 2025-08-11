a = "mango"
b ="cashew"
c = "pear"

fruits = ["mango", "cashew", "pear","watermelon"] #array or list
           #0         #1       #2        #3
#print(fruits[0])

size = len(fruits) #total number of items in the list
#print(size)

last = fruits[size - 1] 
#print(last)

#print(fruits[-1]) #accessing the items in the list using negative indexing
#print(fruits[-2])

#print(fruits[:2]) #accessing the items in the list using range indexing or Slice
#print(fruits[1:3])



fruits[0] = "apple" #changing the value of an item in the list

#print(fruits)

fruits = ["mango", "cashew", "pear","watermelon"] 
#fruits.insert(2,"Pineapple")  #to addd new item

#print(fruits)

#fruits.append("banana")  #to add new item to the end of a list
#print(fruits)


#type2 = ["lemon", "kiwifruit"]  
#fruits.extend(type2) #to add more than 1 item to a list
#print(fruits)


#fruits.remove("mango") # to remove an item from a list
#print(fruits)

#fruits.pop(2)  #to remove using index
#print(fruits)


#for fruit in fruits:  #iteration
  #print(fruit)

#for i in range(len(fruits)):
  #print(fruits[i])


[print(x) for x in fruits]
print(fruits)



#return true if first or last element in any given list is 6 otherwise return false
def either6(values):
  return values[0]==6 or values[len(values)-1]==6

#print(either6([2,1,5,4,7,8,23,0]))


#create a list of 5 car brands then change the brand name of 1:3
cars = ["Porshe", "Toyota", "Honda", "Hyundai", "Bugatti"]

#print(cars)

cars[1:3] = "Amaka", "Jen"  #this changes the name of 1 and 2
#print(cars)



def highest_discovery(nums):

  max_value = max(nums)
  max_index = nums.index(max_value)
  for num in nums:
    if num > max_value:
      max_value = num
  return max_value, max_index



print(highest_discovery([300, 750, 120, 800, 10, 620]))   #return the index



# def total_liters_delivered(nums):
    
#     if total sum > 10000: 
#       return Capacity Exceeded
  


#print(total_liters_delivered([1200, 1800, 1500, 2000, 1750, 1400, 1650]))    
    



# def parts_defected(nums):
#   for num in nums:
#     if num > 5:
#      parts_defected.append(num > 5)
    
#      return parts_defected
    
# print(parts_defected([2, 8, 5, 7, 9, 1, 0]))


# def two_consecutive_zero(nums):
#   for num in nums:
#     if num == 0 
#     return num


# def number_of_passengers(list):


  
  









def digit_classifier(num):
  if num == 0:
    return "Zero"
  elif num % 2 == 0 and num % 3 == 0:
    return "Even and divisible by 3"
  elif num % 2 == 0:
    return "Even"
  else:
    return "Odd"
  
#print(digit_classifier(5))





# def reverse_number(num):





def double_evens_keep_odds(nums):
  result = []
  for num in nums:
    if num % 2 == 0:
      result.append(num * 2)
    

  return result

# print(double_evens_keep_odds([1, 2, 3, 4, 5, 6, 7, 8]))



def collatz_steps_taken(num):
  steps = 0 
  while num != 1:
    if num % 2 == 0:
     num = num // 2
    else: 
     num = 3 * num + 1

     steps += 1
  return steps


# number = 6
# print(f"Steps to reach 1 from {number}: {collatz_steps_taken(number)}")
#print(collatz_steps_taken(9))



def find_second_largest(nums):
  largest = max(nums)
  second_largest = None

  for n in nums:
    if n != largest:
      if second_largest is None or n > second_largest:
        second_largest = n
  return second_largest
      

#print(find_second_largest([20, 11, 7, 9]))



def find_missing_number(nums):
  n = len(nums) + 1
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)

  return expected_sum - actual_sum


#print(find_missing_number([1, 2, 4, 5]))



def palindrome_check(num):
  original = num
  reversed_num = 0

  while num > 0:
    digit = num % 10
    
  reversed_num = reversed_num * 10 + digit
  num = num // 10 

  return original == reversed_num

print(palindrome_check(121))







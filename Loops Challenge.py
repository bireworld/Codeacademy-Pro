#DIVISIBLE BY TEN
#Write your function here
def divisible_by_ten(nums):
  count_div_10 = 0
  for i in range(len(nums)):
    if nums[i] % 10 == 0:
      count_div_10 +=1
      #print(count_div_10)
  return count_div_10

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

#GREETINGS
#Write your function here
def add_greetings(names):
  greeting = []
  for x in range(len(names)):
    greeting.append("Hello, " + names[x])
  return greeting

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#DELETE STARTING EVEN NUMBERS
#Write your function here
def delete_starting_evens(lst):
  for x in range(len(lst)):
    if lst[0] % 2 == 0:
      lst.pop(0)
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#ODD INDICES
#Write your function here
def odd_indices(lst):
  odd_lst = []
  for x in range(len(lst)):
    if x % 2 != 0:
      odd_lst.append(lst[x])
  return odd_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#EXPONENTS
#Write your function here
def exponents(bases, powers):
  new_lst = []
  for b in range(len(bases)):
    for p in range(len(powers)):
      new_lst.append(bases[b]**powers[p])
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#LARGER SUM
#Write your function here
def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  for x in range(len(lst1)):
    sum_lst1 += lst1[x]
  for x in range(len(lst2)):
    sum_lst2 += lst2[x]
  if sum_lst2 > sum_lst1:
    return lst2
  else:
    return lst1
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#OVER 9000
#Write your function here
def over_nine_thousand(lst):
  sum = 0
  for x in range(len(lst)):
    sum += lst[x]
    if sum > 9000:
      break
    else:
      continue
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#MAX NUM
#Write your function here
def max_num(nums):
  max = nums[0]
  for x in range(len(nums)):
    if nums[x] > max:
      max = nums[x]
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#SAME VALUES
#Write your function here
def same_values(lst1, lst2):
  ndx_same = []

  for x in range(len(lst1)):
    if lst1[x] == lst2[x]:
      ndx_same.append(x)
  return ndx_same

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#REVERSED LIST
#Write your function here
def reversed_list(lst1, lst2):
  rvsd_lst2 = []
  x = len(lst2)-1
  while x >= 0:
    rvsd_lst2.append(lst2[x])
    x -= 1
  if lst1 == rvsd_lst2:
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

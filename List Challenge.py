#CODE CHALLENGE: Lists
#1.Double Index
#Write your function here
def double_index(lst, index):
  if index >= len(lst):
    print("There is no value at that index. Instead the original list will be displayed.")
    #print(len(lst))
    return lst

  else:
    identify_index = lst[index]
    double_value_at_index = identify_index*2
    lst[index] = double_value_at_index
    print("The number to be doubled at index " + str(index) + " is " + str(identify_index) + ". The new list is displayed with the new doubled value: " + str(double_value_at_index) + ".")
    return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
print('\n')
print(double_index([3, 8, -10, 12], 5))

#2.Remove Middle
#Write your function here
#solution 1 using del
def sol1_remove_middle(lst, start, end):
  del lst[start:end+1]
  return lst
  
#solution 2 slicing the list and then combining it
def sol2_remove_middle(lst, start, end):
  lst1 = lst[:start]
  lst2 = lst[end+1:]
  new_lst = lst1+lst2
  return new_lst

#Uncomment the line below when your function is done
print(sol1_remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
print(sol2_remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#3.More than N
#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#4.More frequent item
#Write your function here
def more_frequent_item(lst, item1, item2):
#Count of item1 in lst
  count_item1 = lst.count(item1)
#Count of item2 in lst
  count_item2 = lst.count(item2)

  if count_item1 >= count_item2:
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#5.Middle Item
#Write your function here
def middle_element(lst):
  len_lst = len(lst)
  odd_or_even_list = len_lst % 2
  mid_index = int(len_lst/2)
  
  if odd_or_even_list == 0:
    mid1 = lst[mid_index-1]
    mid2 = lst[mid_index]
    average = (mid1 + mid2) / 2
    return average
  else:
    mid = lst[mid_index]
    return mid
    
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

#6.Append Sum
#Write your function here
def append_sum(lst):
  last_two_added = lst[-1] + lst[-2]
  appending_sum1 = lst.append(last_two_added)
  last_two_added = lst[-1] + lst[-2]
  appending_sum2 = lst.append(last_two_added)
  last_two_added = lst[-1] + lst[-2]
  appending_sum3 = lst.append(last_two_added)

  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))


#7. Larger List
#Write your function here
def larger_list(lst1, lst2):
  len_lst1 = len(lst1)
  len_lst2 = len(lst2)

  if len_lst2 > len_lst1:
    return lst2[-1]
  else:
    return lst1[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#8. Combine Sort
#Write your function here
def combine_sort(lst1, lst2):
  combine_lst = lst1 + lst2
  combine_lst.sort()
  return combine_lst

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#9. Append Size
#Another way to do it
#def append_size(lst):
#  new_lst = list(range(1,4))
#  return lst+new_lst
#Write your function here
def append_size(lst):
  for x in range(len(lst)):
    lst.append(x+1)
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#10. Every Three Nums
#Write your function here
def every_three_nums(start):
  new_lst = list(range(start, 101, 3))
  return new_lst

#Uncomment the line below when your function is done
print(every_three_nums(91))

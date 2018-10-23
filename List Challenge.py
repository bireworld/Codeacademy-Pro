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

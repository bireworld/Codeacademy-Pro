#CODE CHALLENGE: Lists
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

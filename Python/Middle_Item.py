#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    sum = my_list[int(len(my_list) / 2)] + my_list[int(len(my_list) / 2) - 1]
    return sum / 2
  return my_list[int(len(my_list) / 2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
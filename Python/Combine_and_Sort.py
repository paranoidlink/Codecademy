#Write your function here
def combine_sort(my_list1, my_list2):
  new_list = my_list1 + my_list2
  return sorted(new_list)
  

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
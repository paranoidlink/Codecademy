#Write your function here
def reversed_list(lst1, lst2):
  if len(lst1) != len(lst2):
    return False
  for num in range(len(lst1)):
    if lst1[num] != lst2[-num - 1]:
      return False
  return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
#Write your function here
def divisible_by_ten(nums):
  bool_list = []
  for num in nums:
    if num % 10 == 0:
      bool_list.append(True)
    else:
      bool_list.append(False)
  return bool_list.count(True)

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
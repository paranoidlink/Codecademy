#Write your function here
def max_num(nums):
  highest = nums[0]
  for num in nums:
    if num > highest:
      highest = num
  return highest


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
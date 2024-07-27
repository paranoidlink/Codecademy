#Write your function here
def over_nine_thousand(lst):
  sum = 0
  i = 0
  if lst == []:
    return 0
  while sum < 9000:
    sum += lst[i]
    i += 1
    if i >= len(lst):
      break
  return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
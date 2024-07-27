# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first_result = a + b
  second_result = c - d
  third_result = first_result * second_result

  print(first_result)
  print(second_result)
  print(third_result)
  return third_result % a
# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
weight = 41.5
cost = 0
shipping_type = "Drone"
#Ground Shipping
if shipping_type == "Ground":
  cost = 20
  if weight <= 2:
    cost += weight * 1.5
  elif weight >2 and weight <= 6:
    cost += weight * 3
  elif weight >6 and weight <= 10:
    cost += weight * 4
  else:
    cost += weight * 4.75
elif shipping_type == "Ground Premium":
  cost = 125
elif shipping_type == "Drone":
  if weight <= 2:
    cost = weight * 4.5
  elif weight >2 and weight <= 6:
    cost = weight * 9
  elif weight >6 and weight <= 10:
    cost = weight * 12
  else:
    cost = weight * 14.25
else:
  print("Error - Invalid Shipping Type")

print ("Cost of shipping your package is: ", round(cost, 2))  

#PROJECT: Sal's Shipping

premium_ground_shipping = 125.00

def ground_shipping (weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
    return cost
  elif weight <= 6:
    cost = weight * 3.00 + 20.00
    return cost
  elif weight <= 10:
    cost = weight * 4.00 + 20.00
    return cost
  else:
    cost = weight * 4.75 + 20.00
    return cost
  
#testing function ground_shipping
#print (ground_shipping(8.4))

def drone_shipping (weight):
  if weight <= 2:
    cost = weight * 4.50
    return cost
  elif weight <= 6:
    cost = weight * 9.00
    return cost
  elif weight <= 10:
    cost = weight * 12.00
    return cost
  else:
    cost = weight * 14.25
    return cost
#testing function drone_shipping
#print (drone_shipping(1.5))

def cheapest_shipping_method (weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    return "Ground shipping is the cheapest for a " + str(weight) + " lbs package.\nIt will cost $" + str(ground_shipping(weight))
  elif drone_shipping(weight) < premium_ground_shipping:
    return "Drone shipping is the cheapest for a " + str(weight) + " lbs package.\nIt will cost $" + str(drone_shipping(weight))
  else:
    return "Premium shipping is the cheapest for a " + str(weight) + " lbs package.\nIt will cost $" + str(premium_ground_shipping)
#testing cheapest_shipping_method
#print(cheapest_shipping_method(41.5))
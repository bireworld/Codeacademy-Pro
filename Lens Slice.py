#PROJECT: Len's Slice

#lists 
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]

#Counting and then outputting the amount of pizzas we have
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

#combining two lists prices and toppings to create pizzas
pizzas = list(zip(prices, toppings))

#sorting prices of pizza from lowest to highest
pizzas.sort()
cheapest_pizza = pizzas
#print(pizzas)

#Priciest pizza
priciest_pizza = pizzas[-1]
#print(priciest_pizza)

#Lowest priced pizzas: three
three_cheapest = pizzas[:3]
#print(three_cheapest)

#count of pizzas that cost $2
num_two_dollar_slices = prices.count(2)
print("We have " + str(num_two_dollar_slices) + " kinds of pizzas that only cost $2.")
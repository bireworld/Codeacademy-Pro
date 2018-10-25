#PROJECT: Carly's Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#SECTION: Prices and cuts
total_price = 0

for x in prices:
  total_price += x  
print(total_price)

average_price = total_price/len(prices)
print("Average Haircut Price: $" + str(round(average_price,2)))

new_prices = [price-5 for price in prices]
print(new_prices)

#SECTION:Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: $" + str(round(total_revenue,2)))

average_daily_revenue = total_revenue/7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print(cuts_under_30)

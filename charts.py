#!/usr/bin/env python
from matplotlib import pyplot as plt

#graph
#drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
#sales =  [91, 76, 56, 66, 52, 27]

#x_range = range(len(sales))

#plt.bar(x_range, sales)

#ax = plt.subplot()
#ax.set_xticks(x_range)
#ax.set_xticklabels(drinks, rotation=30)

#plt.show()

#side by side bars

# drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
# sales1 =  [91, 76, 56, 66, 52, 27]
# sales2 = [65, 82, 36, 68, 38, 40]

# #Paste the x_values code here
# n = 1  # This is our first dataset (out of 2)
# t = 2 # Number of datasets
# d = 6 # Number of sets of bars
# w = 0.8 # Width of each bar
# store1_x = [t*element + w*n for element in range(d)]
# plt.bar(store1_x, sales1)


# n = 2  # This is our second dataset (out of 2)
# t = 2 # Number of datasets
# d = 6 # Number of sets of bars
# #w = 0.8 # Width of each bar
# #store2_x = [t*element + w*n for element in range(d)]

# #plt.bar(store2_x, sales2)

# #plt.show()

#bottom and top bars
# drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
# sales1 =  [91, 76, 56, 66, 52, 27]
# sales2 = [65, 82, 36, 68, 38, 40]

# x2_values = range(len(sales2))

# x_values = range(len(sales1))
# plt.bar(x_values, sales1)
# plt.bar(x2_values, sales2, bottom=sales1)
# labels = ["Store 1 Sales", "Store 2 Sales"]
# plt.legend(labels)
# plt.show()

# drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
# ounces_of_milk = [6, 9, 4, 0, 9, 0]
# error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# Plot the bar graph here
# ax = plt.subplot()
# x_val = range(len(drinks))
# ax.set_xticks(x_val)
# plt.bar(x_val, ounces_of_milk)
# plt.ylabel("OZ")

# ax.set_xticklabels(drinks)

# plt.show()

# months = range(12)
# month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]


# ax = plt.subplot()
# plt.plot(months, revenue)
# ax.set_xticks(months)
# ax.set_xticklabels(month_names)
# plt.show()

#!/usr/bin/env python
# coding: utf-8

# # Hardcoded stock prices

# In[3]:


default_prices = {
"AAPL": 180,
"TSLA": 250,
"GOOGL": 140,
"MSFT": 320
}


portfolio = {}


print("Enter stock names and quantities (type 'done' to finish):")


while True:
    stock = input("Stock name: ").upper()
    if stock == "DONE":
        break
    if stock not in default_prices:
        print("Stock not found in price list. Try again.")
        continue
    qty = int(input(f"Quantity of {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty


# Calculate total investment value
total_value = 0
for stock, qty in portfolio.items():
    total_value += qty * default_prices[stock]


print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} shares × ${default_prices[stock]} = ${qty * default_prices[stock]}")


print(f"\nTotal Investment Value: ${total_value}")


# Save output to CSV
import csv
with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Total Value"])
    for stock, qty in portfolio.items():
        writer.writerow([stock, qty, default_prices[stock], qty * default_prices[stock]])
    writer.writerow([])
    writer.writerow(["Total Portfolio Value", total_value])


print("\nSaved results to result.csv")


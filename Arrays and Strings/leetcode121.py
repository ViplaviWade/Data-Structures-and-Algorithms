# Best time to buy and sell stock

def maxProfit(prices):
    minPrice = float('inf')
    maxProfit = 0
    for price in prices:
        if minPrice > price:
            minPrice = price
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
    return maxProfit

res = maxProfit(prices=[7, 1, 5, 3, 6, 4])
print(res)
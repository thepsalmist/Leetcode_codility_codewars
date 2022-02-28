"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""

# Approach 1
# Take a left and right pointer to represent the first two prices in the array.
#


def maxProfit(prices):
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        # check if profitable
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


# Approach 2
def maxProfit(prices):
    minprice = prices[0]
    maxprofit = 0
    if not prices:
        return 0

    for p in prices[1:]:
        maxprofit = max(maxprofit, (p - minprice))
        minprice = min(minprice, p)
    return maxprofit


# Approach 3
# Calculate the max profit you can make at any given price, each time comparing to previous max.
# When the profit, less than 0, startover from 0
def maxProfit(prices):
    # initialize currentmax and globalmax to o
    currentmax = 0
    globalmax = 0

    for i in range(1, len(prices)):
        currentmax = max(currentmax + (prices[i] - prices([i - 1])), 0)
        globalmax = max(globalmax, currentmax)

    return globalmax

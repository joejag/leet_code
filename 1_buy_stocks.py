# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List


def maxProfit(prices: List[int]) -> int:
    profit = 0
    lowest_price = prices[0]

    for price in prices:
        lowest_price = min(lowest_price, price)
        profit = max(profit, price - lowest_price)

    return profit


assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert maxProfit([7, 6, 4, 3, 1]) == 0
assert maxProfit([2, 4, 1]) == 2

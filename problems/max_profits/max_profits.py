#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_max_profit(yesterdays_stocks):
    """
    Keep a running max_profit and min_price as we iterate through the list
    Runtime:
        Time -> O(n): iterate the list once
        Space -> O(1):
    """
    if len(yesterdays_stocks) < 2:
        raise IndexError("Getting a profit requires atleast 2 prices!")

    min_price = yesterdays_stocks[0]
    max_profit = yesterdays_stocks[1] - yesterdays_stocks[0]

    for index, current_price in enumerate(yesterdays_stocks):
        # We can't sell at the first stock, since we have to buy first
        if index == 0:
            continue

        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    return max_profit



def get_max_profit_brute(yesterdays_stocks):
    """
    Brute Force
        Calculate the max profit for every value in the list and return the largest
    Runtime:
        O(n^2): Comparing numbers to all numbers
    """
    # Set to a random small number
    max_profit = -1000

    for earlier_time, buy_price in enumerate(yesterdays_stocks):
        for sell_price in yesterdays_stocks[earlier_time+1:]:
            # compare all values
            max_profit = max(max_profit, (sell_price - buy_price))

    return max_profit


if __name__ == "__main__":
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]   # 6
    print get_max_profit(stock_prices_yesterday)

    stock_prices_yesterday = [10, 7, 5, 4, 3, 2]    # -1
    print get_max_profit(stock_prices_yesterday)

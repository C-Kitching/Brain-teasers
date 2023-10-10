#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'game_value' function below.
#
# The function is expected to return a DOUBLE.
# The function accepts INTEGER deck_size as parameter.
# deck_size is an even non-negative integer
#
def optimal_value(red, green):
    """
    Calculate optimal payoff of N size deck using dynamic programming
    """
    
    # dynamic programming memory
    memo = {}
    
    def dp(red, green):
        """
        Recursive function to calculate the expected value
        red += $1
        green -= $1
        (r,g) = number of red and green cards left in deck
        f(r,g) = value in deck with (r,g) = r - g

        BCs
        f(r,0) = r (only good cards left)
        f(0,g) = 0 (only bad cards left, so shouldn't draw)

        """
        
        if red == 0:
            return 0
        elif green == 0:
            return red
        elif (red, green) in memo:
            return memo[(red, green)]
            
        # calculate the expected value if you draw a card
        # i.e prob of drawing that card plus contribution to payoff, then you have to keep playing with less cards
        draw_red = red/(red+green) * (dp(red - 1, green)) # red
        draw_green = green/(red+green) * (dp(red, green - 1)) # green
        
        # choose the maximum of drawing a card or stopping
        memo[(red, green)] = max(draw_red + draw_green, red - green)
        return memo[(red, green)]
        
    return dp(red, green)
    

def game_value(red, green):
    # Write your code here
    
    # call helper function
    print(optimal_value(red, green))

if __name__ == '__main__':
    red_cards = 10
    green_cards = 8
    game_value(red_cards, green_cards)

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
def optimal_value(N):
    """
    Calculate optimal payoff of N size deck using dynamic programming
    """
    
    # dynamic programming memory
    memo = {}
    
    def dp(red, green):
        """
        Recursive function to calculate the expected value
        """
        
        if red == 0:
            return 0
        elif green == 0:
            return red
        elif (red, green) in memo:
            return memo[(red, green)]
            
        # calculate the expected value if you draw a card
        # i.e prob of drawing that card plus contribution to payoff, then you have to keep playing with less cards
        draw_red = red/(red+green) * (1 + dp(red - 1, green)) # red
        draw_green = green/(red+green) * (-1 + dp(red, green - 1)) # green
            
        # expected payoff if we stopped here
        stop = 0
        
        # choose the maximum of drawing a card or stopping
        memo[(red, green)] = max(draw_red + draw_green, stop)
        return memo[(red, green)]
        
    return dp(N//2, N//2)
    

def game_value(deck_size):
    # Write your code here
    
    # call helper function
    print(optimal_value(deck_size))

if __name__ == '__main__':
    deck_size = 52
    game_value(deck_size)

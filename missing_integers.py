# imports
import numpy as np
import matplotlib.pyplot as plt
from numpy import random
from random import choices

def quadratic_solver(a, b, c):
    """Solve a quadratic equation ax**2 + bx + c = 0

    Args:
        a (float): x**2 coefficient
        b (float): x coefficient
        c (float): _description_

    Returns:
        _type_: _description_
    """
    x_1 = (-b + np.sqrt(b**2-4*a*c))/(2*a)
    x_2 = (-b - np.sqrt(b**2-4*a*c))/(2*a)

    return x_1, x_2

def sum_consecutive_series(N):
  """
  Function to sum an consecutive series from 1 to N
  """
  return N*(N+1)/2

def sum_sq_consecutive_series(N):
  """
  Function to sum square of consecutive series from 1 to N
  """
  return N**3/3 + N**2/2 + N/6

def main():
  """
  Main function to run program
  """

  # paramters
  N = 100

  # create array
  Z_complete = np.arange(1, 101)

  # numbers to delete
  numbers_to_delete = np.array(choices(Z_complete, k = 2))

  # delete numbers from array
  Z = np.delete(Z_complete, numbers_to_delete - 1)

  # sum elements of Z
  sum_Z = np.sum(Z)
  sum_Z_sq = np.sum(Z**2)

  # sum consecutive series to N
  sum_n = sum_consecutive_series(N)
  sum_n_sq = sum_sq_consecutive_series(N)

  # calculate x and y
  x_1, x_2 = quadratic_solver(1, sum_Z - sum_n, sum_Z**2 - sum_Z*sum_n)
  if x_1 > 0:
    x = x_1
  else:
    x = x_2
  y = np.sqrt(sum_Z_sq - sum_n_sq - x**2)

  print(x, y)
  print(numbers_to_delete)
  


# main code
if __name__ == "__main__":
  main()
# Title: Magic squares
# Name: Christopher Robert Kitching
# Date created: 14/10/22
# Last edited: 14/10/22
# Description: 
# Given a 3x3 matrix x, determine the minimum cost to transform
# that matrix into a magic square.
# A magic square is a NxN grid where all rows, columns and the 2 diagonals
# add up to the same number, and all elements in the square are unique
# The total cost is the sum of individual transformations. For example is 
# 3->9 the cost is |9-3| = 6.

# imports
import copy
from copy import deepcopy

def is_magic(s):
    """Determines if s is a magic square
    """
    
    # check all rows
    for i in range(len(s)):
        sum_row = 0
        for j in range(len(s[0])):
            sum_row += s[i][j]
        if sum_row != 15: return False
    
    # check all columns
    for i in range(len(s)):
        sum_col = 0
        for j in range(len(s[0])):
            sum_col += s[j][i]
        if sum_col != 15: return False
    
    # check diagonals
    n = len(s)
    sum_left_diag = 0
    for i in range(len(s)): sum_left_diag += s[i][i]
    if sum_left_diag != 15: return False
    sum_right_diag = 0
    for i in range(len(s)): sum_right_diag += s[n-1-i][n-1-i]
    if sum_right_diag != 15: return False

    # if all checks pass
    return True

def get_cost(ms1, ms2):
    """Determine the cost difference between two magic squares
    
    Args:
        ms1 (int[][]): magic square 1
        ms2 (int[][]): magic square 2
        
    Returns:
        cost (int): cost difference between the two inputs
    """
    cost = sum([abs(ms1[i][j]-ms2[i][j]) for i in range(len(ms1)) for j in 
           range(len(ms1[0]))])
    return cost

def generate_all_magic_squares():
    """Generate all possible magic sqaures
    
    Returns:
        magic_squares (int[][][]): all possible magic sqaures
    """
    x = [[4,3,8], [9,5,1], [2,7,6]]
    magic_squares = []
    for _ in range(4):
        T = deepcopy(transpose(x))
        magic_squares.append(T)
        R = deepcopy(rotate(x))
        magic_squares.append(R)
        x = deepcopy(R)
    return magic_squares

def transpose(M):
    """Tranpose a matrix
    
    Args:
        M (int[][]): matrix
    
    Returns:
        T (int[][]): transpose of M
    """
    T = [[1,2,3], [4,5,6], [7,8,9]]
    for i in range(len(M)):
        for j in range(0, len(M)):
            T[i][j] = M[j][i]
    return T
    
def rotate(M):
    """Rotate corners of a matrix clockwise
    
    Args:
        M (int[][]): matrix
    
    Returns:
        R (int[][]): rotation of M
    """ 
    M[0][0], M[0][2], M[2][2], M[2][0] = M[2][0], M[0][0], M[0][2], M[2][2]
    M[0][1], M[1][2], M[2][1], M[1][0] = M[1][0], M[0][1], M[1][2], M[2][1]
    return M

def formingMagicSquare(s):
    # Write your code here
    
    # calculate all magic square combinations
    magic_squares = generate_all_magic_squares()
    
    # calculate cost of transforming to all magic squares
    costs = []
    for magic_square in magic_squares:
        costs.append(get_cost(magic_square, s))
    
    # reutrn min cost
    return min(costs)

def main():
    """Main function
    """

    s = [[2,2 ,7],[8, 6, 4],[1, 2, 9]] # example matrix
    cost = formingMagicSquare(s)
    print(cost)

# run file
if __name__ == "__main__":
    main()
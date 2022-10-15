# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 05/10/22
# Last editied: 06/10/22
# Description: Round G - Problem 4 - Cute Little Butterfly

def max_energy(grid, i, j, right, E):

    # if at bottom corners of grid
    if (right and i == len(grid)-1 and j == len(grid[0])-1) or \
    (not right and i == len(grid)-1 and j == 0):
        return grid[i][j]

    # if at bottom edge
    elif i == len(grid)-1:
        # moving right
        if right:
            return grid[i][j] + max_energy(grid, i, j+1, right, E)
        # moving left
        else:
            return grid[i][j] + max_energy(grid, i, j-1, right, E)

    # if at left moving left or at right edge moving right
    elif (j == len(grid[0])-1 and right) or (j == 0 and not right):
        # move down
        return grid[i][j] + max(max_energy(grid, i+1, j, not right, E) - E, # switch direction
                                max_energy(grid, i+1, j, right, E)) # dont switch direction

    # if moving right generally
    elif right and j != len(grid[0])-1:
        return grid[i][j] + max(max_energy(grid, i, j+1, right, E), # move right
                                max_energy(grid, i+1, j, right, E)) # move down

    # if moving left generally
    elif not right and j != 0:
        return grid[i][j] + max(max_energy(grid, i, j-1, right, E), # move left
                                max_energy(grid, i+1, j, right, E)) # move down


def main():
    """Main function
    """

    T = int(input())
    for t in range(T):
        N, E = map(int, input().split())

        # read in data
        x, y, c = [], [], []
        for n in range(N):
            X, Y, C = map(int, input().split())
            x.append(X)
            y.append(Y)
            c.append(C)

        # generate grid
        min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)
        delta_x = max_x - min_x
        delta_y = max_y - min_y
        grid = [[0]*(delta_x+1) for _ in range(delta_y + 1)]
        for i in range(len(c)):
            grid[(y[i]-1)%len(grid)][x[i]-1] = c[i]
        grid = grid[::-1]

        # get max energy
        max_E = max_energy(grid, 0, 0, True, E)

        # print solution
        print("Case #{}: {}".format(t + 1, max_E))


# run file
if __name__ == '__main__':
    main()



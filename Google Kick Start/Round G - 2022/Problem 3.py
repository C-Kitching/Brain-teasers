# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 05/10/22
# Last editied: 15/10/22
# Description: Round G - Problem 3 - Happy Subarrays

def is_happy(arr):
    """Determine if an array is happy

    Args:
        arr (int[]): array

    Returns:
        happy (bool): flag if array is happy
    """
    sum = 0
    for ele in arr:
        sum += ele
        if sum < 0:
            return False
    return True

def main():
    """Main function
    """

    # read each test case
    T = int(input())
    for t in range(T):
        N = int(input()) # number of ints in array
        A = list(map(int, input().split())) # array

        # calculate score
        score = 0
        for i in range(len(A)):
            if A[i] >= 0:
                for j in range(i + 1, len(A) + 1):
                    subarray = A[i:j]
                    if is_happy(subarray):
                        score += sum(subarray)
                    else:
                        break

        print("Case #{}: {}".format(t+1, score))

# run file
if __name__ == '__main__':
    main()



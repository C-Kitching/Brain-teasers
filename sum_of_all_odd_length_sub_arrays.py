
class Solution:

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def sumOddLengthSubarrays(self) -> int:
        """Calculates the total of all odd length sub arrays of arr

        Args:
            arr (int[]): array of integers

        Returns:
            s (int): sum of all odd length sub arrays
        """
        s = 0
        for i, a in enumerate(self.arr):
            s += a * (((self.n-i)*(i+1)+1)//2)
        return s


def  main():
    """Main function
    """

    arr = [10,11,12] # create test array
    S = Solution(arr) # solution object
    s = Solution.sumOddLengthSubarrays(S) # solve 
    print(s) # print result


if __name__ == "__main__":
    main()
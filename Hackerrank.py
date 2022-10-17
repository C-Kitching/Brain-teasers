# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 17/10/22
# Last editied: 17/10/22
# Description: File to test Hackerrank solutions


def minimumSwaps(arr):
    
    d = {v:i for i,v in enumerate(arr)}
    swaps = 0
    for i, ele in enumerate(arr):
        if ele != i+1:
            arr[d[i+1]] = ele
            arr[i] = i+1
            d[ele] = d[i+1]
            d[i+1] = i
            swaps += 1
        
    return swaps
    
    
def main():
    """Main function
    """

    arr = [4,3,1,2]
    swaps = minimumSwaps(arr)    
    print(swaps)

# run file
if __name__ == "__main__":
    main()
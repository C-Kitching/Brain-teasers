# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 21/10/22
# Last editied: 21/10/22
# Description: Merge sorting algoirhtm
# References: https://www.geeksforgeeks.org/merge-sort/

def merge_sort(arr, count):
    """Perform a merge sort on an array

    Args:
        arr (int[]): array to sort
        count (int): number of swaps in merge sort

    Returns:
        arr (int[]): sorted array
        count (int): number of swaps in merge sort
    """
    
    if len(arr) > 1:
        
        # find midpoint
        mid = len(arr)//2
        
        # split into left and right array
        l = arr[:mid]
        r = arr[mid:]
        
        # marge sort split arrays
        l, count = merge_sort(l, count)
        r, count = merge_sort(r, count)
        
        # once we reach length 1 arrays we start comparing
        # compare L and R arrays until we exhaust all elements of one array
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j+= 1
                count += len(l) - i
            k += 1
            
        # if any elements left over
        # i.e if we were comparing odd and even length l and r arrays
        # add them to the back of the sorted array
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1
            
    return arr, count
        
def countInversions(arr):
    """Determine the number of adjacent swaps to sort an array using merge sort

    Args:
        arr (int[]): array to be sorted

    Returns:
        count (int): number of swaps to sort
    """
    count = 0
    arr, count = merge_sort(arr, count)
    return count

def main():
    """Main function
    """

    # array to sort
    arr = [7, 5, 3, 1]

    # sort array and print swaps
    swaps = countInversions(arr)
    print("Number of swaps = {}".format(swaps))



# run file
if __name__ == "__main__":
    main()



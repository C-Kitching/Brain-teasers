# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 17/10/22
# Last editied: 17/10/22
# Description: File to test Hackerrank solutions


def minimumBribes(q):
    # Write your code here

    # check all people in queue
    for i, person in enumerate(q):

        # if any person is more than 2 positions ahead of their original
        # position then its too chatoic
        if person - (i+1) > 2:
            print("Too chaotic")
            return
        
        # if person not at initial position
        if person != i + 1:
            
            # count the number of people with a number larger than them 
            # ranging from one position in front of their original position
            # to one person in front of their current position
            for j in range(max(person - 2, 0), i):
                if q[j] > person:
                    bribes += 1
            
    print(bribes)
    return 
        
    
def main():
    """Main function
    """

    q = [2, 1, 5, 3, 4]
    print(minimumBribes(q))


# run file
if __name__ == "__main__":
    main()
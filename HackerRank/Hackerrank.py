# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 17/10/22
# Last editied: 17/10/22
# Description: File to test Hackerrank solutions


def get_median(count, d):
    
    counter = 0
    median = 0
    
    # odd length arrays
    if d%2 != 0:
        
        # loop through counter
        for i in range(len(count)):
            
            # incremenet until we find the midpoint
            counter += count[i]
            if counter > d//2:
                median = i
                break
    
    # even length arrays
    else:
        
        first = 0
        second = 0
        
        # loop through counter
        for i in range(len(count)):
            
            # increment until we find middle points
            counter += count[i]
            if counter >= d//2:
                median = (2*i+1)/2
                break
                
    return median
            

def activityNotifications(expenditure, d):
    # Write your code here
    
    count = [0] * (max(expenditure) + 1)
    
    trailing_days = expenditure[:d]
    for spend in trailing_days:
        count[spend] += 1
        
    warnings = 0
    for i in range(d, len(expenditure)):
        
        new_value = expenditure[i]
        old_value = expenditure[i-d]
        
        median = get_median(count, d)
        if expenditure[i] >= 2*median:
            warnings += 1
            
        count[new_value] += 1
        count[old_value] -= 1
        
    return warnings
            
        
    
    
def main():
    """Main function
    """

    d = 5
    arr = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    w = activityNotifications(arr, d)
    print(w)

# run file
if __name__ == "__main__":
    main()
# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 17/10/22
# Last editied: 17/10/22
# Description: File to test Hackerrank solutions


# Enter your code here. Read input from STDIN. Print output to STDOUT

def main():
    """Main function
    """

    S = ""
    S_changes = []
    
    # read input
    Q = int(input())
    for _ in range(Q):
        operation = input()

        prior_S = S
        
        # handle cases
        if operation[0] == "1":
            W = operation.split()[1]
            S += W
        elif operation[0] == "2":
            to_delete = int(operation.split()[1])
            S = S[:-to_delete]
        elif operation[0] == "3":
            index = int(operation.split()[1]) - 1
            if index <= (len(S) - 1):
                print(S[index])
        else:
            S = S_changes[-1]
            S_changes.pop()
            
        print(S)
                    
        # store change
        if operation[0] != "4" and S != prior_S:
            S_changes.append(prior_S)
            
    return S
            
# run file
if __name__ == "__main__":
    main()

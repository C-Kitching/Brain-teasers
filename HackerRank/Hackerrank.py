# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 17/10/22
# Last editied: 17/10/22
# Description: File to test Hackerrank solutions


<<<<<<< HEAD
# Enter your code here. Read input from STDIN. Print output to STDOUT

=======
>>>>>>> 775ee91f3d1c33ba5e2b84ee1dbb739eec0b42f7
def main():
    """Main function
    """

    S = ""
<<<<<<< HEAD
    S_changes = []
=======
    S_changes = [S]
>>>>>>> 775ee91f3d1c33ba5e2b84ee1dbb739eec0b42f7
    
    # read input
    Q = int(input())
    for _ in range(Q):
        operation = input()
<<<<<<< HEAD

        prior_S = S
=======
>>>>>>> 775ee91f3d1c33ba5e2b84ee1dbb739eec0b42f7
        
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
<<<<<<< HEAD
        if operation[0] != "4" and S != prior_S:
            S_changes.append(prior_S)
=======
        if operation[0] != "4" and S != S_changes[-1]:
            S_changes.append(S)
>>>>>>> 775ee91f3d1c33ba5e2b84ee1dbb739eec0b42f7
            
    return S
            
# run file
if __name__ == "__main__":
    main()

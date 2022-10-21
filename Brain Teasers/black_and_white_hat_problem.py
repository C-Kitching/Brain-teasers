# imports
import numpy as np
import matplotlib.pyplot as plt

def main():
    """Main Function
    """

    # problem parameters
    N = 1000
    p = 0.5 # prob of 1
    number_of_sims = 100

    # container to store death count for each simulation
    death_counts = np.empty(number_of_sims)

    # run each simulation
    for i in range(number_of_sims):

        # create random array of. 0 and 1
        x = np.random.choice([0,1], size = N, p = [1-p, p])
        
        # count number of ones
        one_count = np.count_nonzero(x == 1)

        # set even state 
        even = bool(one_count%2 == 0)

        # death counter
        death_count = 0

        # determine state of the first person 
        if even:
            answer = 1
        else:
            answer = 0

        # kill if answer wrong
        if answer != x[0]:
            death_count += 1

        # loop through the array
        for j in range(1, len(x)):

            # determine the number of ones in front
            one_count -= x[i]

            # determine if number of 1s infront is even
            new_even = bool(one_count%2 == 0)

            # if my state is the same as the global state answer 0
            if new_even == even:
                answer = 0
            # if its different answer 1 and update global state
            else: 
                answer = 1
                even = not even

            # if answer wrong, kill
            if answer != x[i]:
                death_count += 1

        # store death count for that simulation
        death_counts[i] = death_count

    # calculate average death count
    avg_death_count = np.mean(death_counts)    
    survival_rate = (1 - avg_death_count/N) * 100

    # print result
    print("Survival rate = {:.2f}%".format(survival_rate))

# main code
if __name__ == "__main__":
    main()
# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 05/10/22
# Last editied: 15/10/22
# Description: Problem 2

def main():
    """Main function
    """

    T = int(input())
    for t in range(T):
        R_s, R_h = map(int, input().split()) # radius of stones and house

        # team 1
        N = int(input())
        team_1_distance = []
        for _ in range(N):
            x, y = map(int, input().split())
            dist = (x**2 + y**2)**(0.5)
            if dist <= R_s + R_h:
                team_1_distance.append(dist)


        # team 2
        M = int(input())
        team_2_distance = []
        for _ in range(M):
            x, y = map(int, input().split())
            dist = (x**2 + y**2)**(0.5)
            if dist <= R_s + R_h:
                team_2_distance.append(dist)

        # both teams have legal stones
        if team_1_distance and team_2_distance:

            min_1 = min(team_1_distance)
            min_2 = min(team_2_distance)
            team_1_score = 0
            team_2_score = 0
            if min_1 > min_2:
                team_1_score = 0
                team_2_score = len([i for i in team_2_distance if i < min_1])
            else:
                team_2_score = 0
                team_1_score = len([i for i in team_1_distance if i < min_2])

        # if only team 1 has legal stones
        elif team_1_distance:
            team_1_score = len(team_1_distance)
            team_2_score = 0

        # if only team 2 has legal stones
        elif team_2_distance:
            team_1_score = 0
            team_2_score = len(team_2_distance)

        # neither has legal stones
        else:
            team_1_score, team_2_score = 0, 0 

        print("Case #{}: {} {}".format(t + 1, team_1_score, team_2_score))

# run file
if __name__ == '__main__':
    main()



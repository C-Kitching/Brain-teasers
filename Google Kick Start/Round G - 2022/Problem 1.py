# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 05/10/22
# Last editied: 06/10/22
# Description: Round G - Problem 1

def main():
    """Main function
    """
    T = int(input())
    for k in range(T):
        M, N, P = map(int, input().split())

        score_board = []
        for i in range(M):
            scores = list(map(int, input().split()))
            score_board.append(scores)

        additional_score = 0
        for i in range(N):
            johns_score = score_board[P - 1][i]
            temp = []
            for j in range(M):
                if score_board[j][i] > johns_score:
                    temp.append(score_board[j][i] - johns_score)
            if temp:
                additional_score += max(temp)
        print("Case #{}: {}".format(k + 1, additional_score))


# run file
if __name__ == '__main__':
    main()



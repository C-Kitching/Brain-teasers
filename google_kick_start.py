# Title: Google Kick Start
# Name: Christopher Robert Kitching
# E-mail: christopher.kitching@manchester.ac.uk
# Date created: 05/10/22
# Last editied: 06/10/22
# Description: File to test google kick start code

import heapq

def h_index(n, citations):
    """_summary_

    Args:
        n (_type_): _description_
        citations (_type_): _description_

    Returns:
        _type_: _description_
    """
    # TODO: Complete the function to get the H-Index scores after each paper
    citations = list(citations)
    minH = []
    ans = []
    H = 0

    for i in range(n):

        if citations[i] > H:
            heapq.heappush(minH, citations[i])
        while minH and minH[0] <= H:
            heapq.heappop(minH)
        if len(minH) >= H + 1:
            H += 1
        ans.append(H)

    return ans


if __name__ == '__main__':
  t = int(input())

  for test_case in range(1, t + 1):
    n = int(input())                      # The number of papers
    citations = map(int, input().split()) # The number of citations for each paper
    h_index_scores = h_index(n, citations)
    print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))



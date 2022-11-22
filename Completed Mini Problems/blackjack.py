def hand_score(hand):
    """Calculate the score of a single hand
    """
    
    # set score and aces to zero
    hand_score = 0
    hand_aces = 0
    
    # check all cards
    for card in hand:
        # if number card 
        if card not in ['A', 'J', 'Q', 'K']:
            hand_score += int(card)
        # if picture card
        elif card != 'A': hand_score += 10
        # if ace
        else: hand_aces += 1

    # check if bust or if at 21 with aces still to add
    if hand_score > 21 or (hand_score == 21 and hand_aces > 0): return 0
    
    # determine the possible scores given the number of aces
    possible_ace_scores = []
    for i in range(hand_aces + 1):
        possible_ace_scores.append(i*11 + (hand_aces - i)*1) 
        
    # determine combinations of aces that gives the highest score without 
    # busting
    max_score = hand_score
    for ace_score in possible_ace_scores:
        temp = hand_score + ace_score
        if max_score < temp <= 21:
            max_score = temp
    hand_score = max_score   
        
    # if bust
    if hand_score > 21: return 0
    
    return hand_score

        

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total 
    must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a 
    string.
    
    When adding up a hand's total, cards with numbers count for that many 
    points. Face cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count 
    for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way 
    that maximizes the hand's total without going over 21. e.g. the total of 
    ['A', 'A', '9'] is 21, the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    hand_1_score = hand_score(hand_1)
    hand_2_score = hand_score(hand_2)
    return hand_1_score > hand_2_score

def main():
    """Main function
    """

    # set hands
    hand_1 = ['2', 'A', '5', 'Q', '4']
    hand_2 = ['J', '4', '3', 'A', '10']

    # determine if hand one beats hand two
    hand_1_better = blackjack_hand_greater_than(hand_1, hand_2)
    if hand_1_better: print("Hand 1 beats hand 2")
    else: print("Hand 1 doesn't beat hand 2")


# run file
if __name__ == "__main__":
    main()
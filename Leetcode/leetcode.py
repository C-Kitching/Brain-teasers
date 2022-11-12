


def countGoodStrings(low, high, zero, one):
        
    if one > high and zero > high:
        return 0
    
    dp = [0] * (high+1)
    dp[one] += 1
    dp[zero] += 1
    
    total = 0

    for i in range(min(zero, one), high + 1):
        dp[i] += dp[i-one] + dp[i - zero]
        if i>= low: total += dp[i]
        
    return total%(10**9 + 7)

def main():

    low = 2
    high = 3
    zero = 1
    one = 2
    x = countGoodStrings(low, high, zero, one)
    print(x)

main()
def optimal_value(N):
    if N % 2 != 0:
        raise ValueError("Deck size must be even")

    half_N = N // 2

    # Initialize a memoization table to store computed values
    memo = {}

    # Helper function to calculate the expected value
    def dp(red, green):
        if red == 0:
            return 0  # No red cards left, so stop
        elif green == 0:
            return red
        elif (red, green) in memo:
            return memo[(red, green)]

        # Calculate the expected value if you draw a red card
        draw_red = (red / (red + green)) * (1 + dp(red - 1, green))

        # Calculate the expected value if you draw a green card
        draw_green = (green / (red + green)) * (-1 + dp(red, green - 1))

        # Calculate the expected value if you stop drawing cards
        stop = 0

        # Choose the maximum expected value
        memo[(red, green)] = max(draw_red, draw_green, stop)
        return memo[(red, green)]

    return dp(half_N, half_N)

# Example usage:
N = 52  # Deck size must be even
value = optimal_value(N)
print(f"The optimal value for a deck of size {N} is ${value:.2f}")
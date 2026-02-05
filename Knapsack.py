def knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack Problem using Dynamic Programming with space optimization.

    Given a set of items, each with a weight and a value, determine the maximum
    total value that can be placed in a knapsack of fixed capacity. Each item
    can only be included once (0/1 property).

    This implementation uses a 1D array instead of a 2D table, reducing space
    complexity from O(n * capacity) to O(capacity).

    Args:
        weights: List of item weights (non-negative integers).
        values:  List of item values (non-negative integers).
        capacity: Maximum weight the knapsack can hold (non-negative integer).

    Returns:
        The maximum value achievable within the given capacity.

    Time:  O(n * capacity) where n is the number of items
    Space: O(capacity) — only a single 1D array is used
    """
    # Edge case: if no items or no capacity, maximum value is 0
    if not weights or not values or capacity <= 0:
        return 0

    n = len(weights)

    # dp[j] represents the maximum value achievable with capacity j.
    # Initialize all values to 0 (base case: with 0 items, max value is 0).
    dp = [0] * (capacity + 1)

    # Outer loop: iterate through each item
    for i in range(n):
        weight = weights[i]
        value = values[i]

        # Inner loop: iterate capacity in REVERSE order (from capacity down to weight).
        #
        # Why reverse order?
        # - In the 2D DP approach, dp[i][j] depends on dp[i-1][j] and dp[i-1][j-weight].
        # - When using a 1D array, we overwrite values in place.
        # - If we iterate forward (low to high), dp[j-weight] would already be updated
        #   in the current iteration, meaning the same item could be used multiple times.
        # - By iterating backward, dp[j-weight] still holds the value from the previous
        #   item iteration, ensuring each item is used at most once.
        for j in range(capacity, weight - 1, -1):
            # State transition equation:
            # dp[j] = max(dp[j], dp[j - weight] + value)
            #
            # Two choices for each capacity j:
            # 1. Don't take item i: keep dp[j] (value without this item)
            # 2. Take item i: dp[j - weight] + value (value with this item)
            #
            # We choose the maximum of these two options.
            if dp[j - weight] + value > dp[j]:
                dp[j] = dp[j - weight] + value

    # dp[capacity] holds the maximum value achievable with full capacity
    return dp[capacity]


# ---------------------------------------------------------------------------
# Demo / Tests
# ---------------------------------------------------------------------------
def main():
    print("0/1 Knapsack Problem - Space Optimized DP Solution")
    print("=" * 55)

    test_cases = [
        # (description, weights, values, capacity, expected)
        ("Empty lists",
         [], [], 10, 0),

        ("Zero capacity",
         [1, 2, 3], [10, 20, 30], 0, 0),

        ("Single item fits",
         [5], [100], 10, 100),

        ("Single item doesn't fit",
         [15], [100], 10, 0),

        ("Classic example",
         [2, 3, 4, 5], [3, 4, 5, 6], 5, 7),
        # Items: (w=2,v=3), (w=3,v=4), (w=4,v=5), (w=5,v=6)
        # Best: take items with w=2 and w=3 -> total weight=5, value=7

        ("All items fit",
         [1, 2, 3], [10, 20, 30], 10, 60),

        ("No items fit",
         [10, 20, 30], [100, 200, 300], 5, 0),

        ("Optimal selection",
         [10, 20, 30], [60, 100, 120], 50, 220),
        # Best: take items with w=20 and w=30 -> total weight=50, value=220

        ("Greedy trap (value density)",
         [1, 3, 4], [1, 4, 5], 4, 5),
        # Greedy by value/weight ratio would pick (w=3,v=4) first
        # But optimal is (w=4,v=5)
    ]

    all_passed = True
    for desc, weights, values, capacity, expected in test_cases:
        result = knapsack(weights, values, capacity)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"\n{desc}:")
        print(f"  Weights:  {weights}")
        print(f"  Values:   {values}")
        print(f"  Capacity: {capacity}")
        print(f"  Expected: {expected}, Got: {result} [{status}]")

    print("\n" + "=" * 55)
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed!")


if __name__ == "__main__":
    main()

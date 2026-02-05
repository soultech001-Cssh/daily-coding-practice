def binary_search(arr, target):
    """
    Search for `target` in a sorted list `arr` using binary search.

    Binary search works by repeatedly dividing the search interval in half.
    It compares the target value to the middle element and eliminates half
    of the remaining elements each iteration.

    Args:
        arr: A sorted list of comparable elements (ascending order).
        target: The value to search for.

    Returns:
        The index of `target` in `arr` if found, otherwise -1.

    Time:  O(log n) — halves the search space each iteration
    Space: O(1) — uses only a constant amount of extra memory
    """
    # Handle empty array gracefully
    if not arr:
        return -1

    # Initialize two pointers for the search boundaries
    left = 0
    right = len(arr) - 1

    # Continue searching while the window is valid
    while left <= right:
        # Calculate mid using floor division to avoid potential overflow
        # This formula (left + (right - left) // 2) is safer than (left + right) // 2
        # in languages with fixed-size integers, as it prevents overflow
        mid = left + (right - left) // 2

        if arr[mid] == target:
            # Target found at index mid
            return mid
        elif arr[mid] < target:
            # Target is in the right half, move left pointer
            left = mid + 1
        else:
            # Target is in the left half, move right pointer
            right = mid - 1

    # Target not found in the array
    return -1


# ---------------------------------------------------------------------------
# Demo / Tests
# ---------------------------------------------------------------------------
def main():
    # Test cases with expected results
    test_cases = [
        ("Empty array",           [],                      5,   -1),
        ("Single element found",  [5],                     5,    0),
        ("Single element miss",   [5],                     3,   -1),
        ("First element",         [1, 3, 5, 7, 9],         1,    0),
        ("Last element",          [1, 3, 5, 7, 9],         9,    4),
        ("Middle element",        [1, 3, 5, 7, 9],         5,    2),
        ("Not found (too low)",   [1, 3, 5, 7, 9],         0,   -1),
        ("Not found (too high)",  [1, 3, 5, 7, 9],        10,   -1),
        ("Not found (in gap)",    [1, 3, 5, 7, 9],         4,   -1),
        ("Even length array",     [2, 4, 6, 8],            6,    2),
        ("Negative numbers",      [-10, -5, 0, 5, 10],    -5,    1),
        ("Duplicates (finds one)",[1, 2, 2, 2, 3],         2,    2),
    ]

    print("Binary Search Test Results")
    print("=" * 70)

    all_passed = True
    for label, arr, target, expected in test_cases:
        result = binary_search(arr, target)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_passed = False
        print(f"{status}  {label:25s}  arr={str(arr):20s}  "
              f"target={target:3}  result={result:2}  expected={expected:2}")

    print("=" * 70)
    print(f"All tests passed: {all_passed}")


if __name__ == "__main__":
    main()

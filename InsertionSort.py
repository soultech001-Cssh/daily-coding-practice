def insertion_sort(arr):
    """
    Sort `arr` in-place using the insertion sort algorithm.

    Mental model: the list is divided into a sorted region (indices 0..i-1)
    and an unsorted region (indices i..n-1).  Each iteration takes the first
    unsorted element, then shifts sorted elements rightward until the correct
    position is found, and drops the element there.

    Time:  O(n^2) average/worst, O(n) best (already sorted)
    Space: O(1) — in-place
    Stable: yes — equal elements are never moved past each other.
    """
    n = len(arr)

    # Outer loop: pick the next unsorted element starting at index 1.
    # Everything to the left of `i` is already sorted.
    for i in range(1, n):
        key = arr[i]  # the value we need to insert into the sorted region

        # Inner loop: shift elements in the sorted region that are STRICTLY
        # greater than `key` one position to the right.  Using ">" (not ">=")
        # guarantees stability — equal elements keep their original order.
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # shift element rightward
            j -= 1

        # Place the key in its correct position (the gap left by shifting).
        arr[j + 1] = key

    return arr  # convenience return; list is sorted in-place


# ---------------------------------------------------------------------------
# Demo / Tests
# ---------------------------------------------------------------------------
def main():
    cases = [
        ("Empty array",          []),
        ("Single element",       [42]),
        ("Already sorted",       [1, 2, 3, 4, 5]),
        ("Reverse sorted",       [5, 4, 3, 2, 1]),
        ("Duplicates",           [4, 2, 7, 2, 1, 4]),
        ("Negative numbers",     [-3, 0, -1, 5, -2, 3]),
        ("All identical",        [7, 7, 7, 7]),
    ]

    for label, data in cases:
        original = list(data)          # keep a copy for display
        insertion_sort(data)
        print(f"{label:20s}  {str(original):28s} -> {data}")

    # --- Stability demonstration ---
    # Pairs (value, original_index).  After sorting by value, items with the
    # same value must retain their original relative order.
    print("\nStability check (sorting by first element of each tuple):")
    pairs = [(3, "a"), (1, "b"), (3, "c"), (2, "d"), (1, "e")]
    print(f"  Before: {pairs}")
    # Sort only by the first element using a key-aware wrapper.
    insertion_sort_keyed(pairs, key=lambda x: x[0])
    print(f"  After:  {pairs}")
    print("  (1,'b') appears before (1,'e') and (3,'a') before (3,'c') — "
          "original order preserved.")


def insertion_sort_keyed(arr, key):
    """Same algorithm, but compares using a key function."""
    n = len(arr)
    for i in range(1, n):
        current = arr[i]
        current_key = key(current)
        j = i - 1
        while j >= 0 and key(arr[j]) > current_key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


if __name__ == "__main__":
    main()

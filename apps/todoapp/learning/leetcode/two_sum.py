"""
Problem 1 — Two Sum (Easy)

Given an array `nums` and an integer `target`, return the INDICES of the two
numbers that add up to `target`. Exactly one solution; can't reuse an element.

    nums = [2, 7, 11, 15], target = 9  ->  [0, 1]   (2 + 7 = 9)
    nums = [3, 2, 4],       target = 6  ->  [1, 2]

Run it:   python two_sum.py

Approach: single pass + hashmap.
    Time  O(n) — one loop, O(1) average dict lookups.
    Space O(n) — the dict can hold up to n entries.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                        # maps  value -> index where we saw it

    for i, num in enumerate(nums):   # enumerate gives both index (i) and value (num)
        delta = target - num         # the complement we still need to reach target

        if delta in seen:            # have we already passed that complement?
            return [seen[delta], i]  # yes -> return its index, then the current index

        seen[num] = i                # not found yet: remember this value's index
                                     # (stored AFTER the check, so we never reuse an element)

    return []                        # unreachable: problem guarantees one solution


if __name__ == "__main__":
    # Quick tests — these should print True when your solution is correct.
    print(two_sum([2, 7, 11, 15], 9) == [0, 1])
    print(two_sum([3, 2, 4], 6) == [1, 2])
    print(two_sum([3, 3], 6) == [0, 1])

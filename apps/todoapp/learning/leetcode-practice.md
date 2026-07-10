# LeetCode Practice — Python warm-up

Basic problems to shake off the rust before interviews. Each entry: problem, your
attempt, a clean solution, and time/space complexity.

---

### 1. Two Sum  (Easy)

**Problem:** Given an array of integers `nums` and an integer `target`, return the
**indices** of the two numbers that add up to `target`. Exactly one solution; can't use the
same element twice.

```
nums = [2, 7, 11, 15], target = 9   →  [0, 1]   (2 + 7 = 9)
nums = [3, 2, 4],       target = 6   →  [1, 2]
```

**Solution (single pass + hashmap):**

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                        # value -> index
    for i, num in enumerate(nums):
        delta = target - num         # complement needed to reach target
        if delta in seen:
            return [seen[delta], i]
        seen[num] = i                # after the check, so we never reuse an element
    return []
```

- **Time O(n)** — one pass, O(1) average dict lookups.
- **Space O(n)** — dict holds up to n entries.
- Naive double-loop alternative is **O(n²) time, O(1) space** — this problem is about
  trading space for time.

**Gotchas I hit:** must return **indices, not values** (so use a `dict value->index`, not a
`set`); `enumerate` gives the index; store `seen[num]=i` *after* the check.

Runnable: [`leetcode/two_sum.py`](leetcode/two_sum.py)

---

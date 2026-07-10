"""
Problem 2 — Valid Anagram (Easy)

Given two strings `s` and `t`, return True if `t` is an anagram of `s`
(same characters with the same counts, just reordered), else False.

    s = "anagram", t = "nagaram"  ->  True
    s = "rat",     t = "car"      ->  False

Run it:   python valid_anagram.py

Hint: think about counting characters. What's the quickest way to compare
two strings' character counts? (There's a one-liner, and a more explicit way.)
"""


def is_anagram(s: str, t: str) -> bool:
    # TODO: write your solution here
    pass


if __name__ == "__main__":
    # Quick tests — these should print True when your solution is correct.
    print(is_anagram("anagram", "nagaram") == True)
    print(is_anagram("rat", "car") == False)
    print(is_anagram("a", "ab") == False)      # different lengths
    print(is_anagram("", "") == True)

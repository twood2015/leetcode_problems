# First Solution
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(isAnagram('cat', 'act'))

print(isAnagram('rap', 'rat'))
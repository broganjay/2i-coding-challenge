from typing import List


def findMaxSum(strings: List[str]) -> int:
    largestSum = 0
    for i in range(len(strings)):
        stringSum = sum(int(s) for s in strings[i] if s.isnumeric())
        largestSum = max(largestSum, stringSum)
    return largestSum
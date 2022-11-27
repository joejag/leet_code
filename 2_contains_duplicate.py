# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


assert containsDuplicate([1, 2, 3, 1]) == True
assert containsDuplicate([1, 2, 3, 4]) == False
assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    locations = {}
    for idx, num in enumerate(nums):
        required = target - num
        if required in locations:
            return [locations[required], idx]
        locations[num] = idx
    return []


assert twoSum([2, 7, 11, 15], 9) == [0, 1]
assert twoSum([3, 2, 4], 6) == [1, 2]
assert twoSum([3, 3], 6) == [0, 1]

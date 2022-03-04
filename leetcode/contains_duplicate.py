"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false
"""


# Approach 1
# Convert the list of nums to set and compare the lengths, if lengths are not equal then contains duplicate


def containsDuplicate(nums):
    res = set(nums)
    if len(nums) != len(res):
        return True
    return False


print(containsDuplicate([1, 2, 3, 4]))

# Approach 2
# Sort the number, and compare adjacent alements, if they are equal return True, else False
# Time complexity (O(n)), sorting takes an extra time complexity (O(nlogn))
# Space complexity - (O(1))
def containsDuplicate(nums):
    nums = nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums(i - 1):
            return True
        return False


# Approach 3
# Using Ha - Create a hash set where you loop through each element and append to the hashset
# If the element already exists in hashset, retur True - there's a duplicate


# def containsDuplicate(nums):
# issue ????
#     seen = {}
#     for i, n in enumerate(nums):
#         if n in seen:
#             return True
#         seen[i] = n
#     return False


def containsDuplicate(nums):
    seen = {}
    for i in nums:
        if i in seen:
            return True
        seen[i] = 1
    return False

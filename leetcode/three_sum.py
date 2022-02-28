"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

# Approach 1

#Sort the array, helps eliminate duplicates and shifting the left and right pointer

def threeSum(nums):
    res = []
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a ==nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l<r:
            threSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append(a, nums[l], nums(r))
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
        
    return res






















# Approach 2

# Sort the array,and take two pointers left, right. Left starts from i+1 and Right is last element
# Sumtotal = i + (i+1) + R --- (i+1) -left element, R- right element
# If sumtotal == 0(target) L=L+1, R=R-1. If Sumtotal < 0, L=L+1, If Sumtotal > 0, R=R-1
# If Sumtotal == 0 , append(nums(i), nums(L), nums(R)) to output

def threeSum(nums):
    #create an empty list to store result
    res = []
    #sort the nums input
    nums.sort()

    #
    for i in range(0,len(nums)-2):
        if nums[i] == nums[i+1]:
            continue
        l = i+1
        r = len(nums)-1

        while l<r:
            total = nums[i]+ nums[l]+ nums[r]
            if total < 0:
                #increment value of left by 1, 
                l = l+1
            elif total> 0:
                #decrease value right by 1
                r = r -1
            else:
                res.append(nums[i], nums(l), nums(r))








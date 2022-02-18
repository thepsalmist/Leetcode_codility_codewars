# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Example given an array A[0] =2, A[1]=3, A[2]=1, A[3]=5, the function should return 4 as its missing element

# Approach 1 - Brute Solution
# Define an index i =1 to N+1, loop through the array, test if we find i

# Approach 2 - Sort the array in ascending order. The index and the element should be related (index = element +1 since indices are 0 based).Where condition does not hold, return the element


def solution(A):
    #
    if len(A) == 0:
        return 1
    A.sort()

    for i in range(0, len(A)):
        if A[i] != i + 1:
            return i + 1
    return len(A) + 1


# Aproach 3
# You create an array of the size of (A + 1) to accommodate for the missing element and assign each element from A to array at index: (element - 1) (because arrays are indexed from 0) -> so 1 will be at 0, 2 at 1, 3 at 2 and so on.
# Because the missing element is, well, missing, it won't be assigned and the new array will thus contain 0 at its index (the example array would like this: [1, 2, 3, 4, 0, 6, 7, 8]). We have "sorted" A into the new array, but only through a single for loop - O(n).
# Now we can just loop through the sorted array, find 0 and return its (index + 1) (since we offset the array by 1), resulting in O(n + n) => O(n) complexity. You can replace the second loop by a binary search to make it a bit faster if you want to, but the complexity will still end up O(n + log(n)) => O(n)


def solution(A):
    array = [0] * (len(A) + 1)
    for number in A:
        array[number - 1] = number
    for i in range(len(array)):
        if array[i] == 0:
            return i + 1


# Aproach 4
# The second solution is even better, it needs only a single loop, resulting in O(n) complexity.
#  As a bonus, it also cuts down on space complexity from O(n) to O(1).
# What we can do is take the sum of elements from A and find the difference between it and the sum if the element was not missing, which we can calculate since it is 1 + 2 + 3 + 4 + ... + n + (n + 1), where n is the size of A (the formula for this is called "triangular number").
# The difference will be the missing number.
def solution(A):
    expected_sum = ((len(A) + 1) * (len(A) + 2)) // 2
    return expected_sum - sum(A)

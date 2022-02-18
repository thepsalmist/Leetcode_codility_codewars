#  The problem states that any given P, such that 0 < P < N (that is, any element of the array except the first one,
#  is able to successfully split the array into two adjacent arrays,
#  such that A_left = [A[0], A[1], …, A[P-1]] and A_right = [A[P], A[P+1], …, A[N-1]].


# Example A = [3,1,2,4,3], starting =3, sum for (1,2,4,3) =10. Absolute difference btw |3-10| = 7

# Approach 1: Brute force
# Loop through the array starting from position(index) 1, second loop from index 0

# Approach 2:
# Calculate the sum of the array S
# Calculate the sum of the left part Sum_left
# The right sum will be (Total Sum - Left Sum)
# SR = S-SL
# |SL_SR| = |SL-S+SL| = |2.SL-S|


def solution(A):
    if len(A) < 2:
        return 0
    S = sum(A)

    minDiff = 2000
    SL = 0

    for i in range(0, len(A) - 1):
        SL += A[i]
        diff = abs(2 * SL - S)
        minDiff = min(minDiff, diff)

    return minDiff

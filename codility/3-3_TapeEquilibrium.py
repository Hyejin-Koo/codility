# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    list_len = len(A)
    if list_len == 1:
        return A[0]

    
    right = sum(A)
    left = 0
    diff = [[]] * (list_len-1)

    for i in range(list_len-1):
        left += A[i] # if calculate sum in [for] -> poor time effeiciency
        right -= A[i]
        diff[i] = abs(left-right)

    return min(diff)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]
    gap = 0
    gaps = []
    was_zero = False

    while(binary[-1] == '0'):
        binary = binary[:-1]
    
    if len(binary) == 1:
        return 0

    for i in range(len(binary)):
        if binary[i] == '0' and was_zero:
            gap += 1
            was_zero = True
        elif binary[i] == '0':
            was_zero = True
            gap += 1
        else:
            was_zero = False
            gaps.append(gap)
            gap = 0 # initalize

    return max(gaps)

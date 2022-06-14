def solution(lottos, win_nums):
    answer = []
    same = 0
    zero = 0
    
    for lot in lottos:
        if lot in win_nums:
            same += 1
        if lot == 0:
            zero += 1
    
    if same == 6:
        return [1,1]
    elif zero == 6:
        return [1,6]
    elif same == 0 and zero == 0: ## test case 14, 다 틀렸으면서 0도 없을 때
        return [6,6]
    else:
        return [7-same-zero, min(7-same,6)]

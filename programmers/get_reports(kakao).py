def solution(id_list, report, k):
    report = set(report)
    answer = [0] * len(id_list)
    block = [-k+1] * len(id_list)

    #for user in id_list: ##id_list까지 for문으로 할 필요가 없었음(시간 초과 에러만 발생..)
    for rep in report:
        #if rep.split(' ')[0] == user: ## 비교할 필요가 없음.
        block[id_list.index(rep.split(' ')[1])] +=1
    block = [max(block[i],0) for i in range(len(block))]
    
    
    for rep in report:
        if block[id_list.index(rep.split(' ')[1])]:
            answer[id_list.index(rep.split(' ')[0])] += 1
        
    return answer

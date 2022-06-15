def solution(new_id):
    answer = ''
    answer = new_id.lower() # step1
    
    # step2
    allowed = [i for i in range(48,58)] # 0~9
    allowed.extend(range(65,91)) # A~Z  ## range로 추가할 때는 extend를...
    allowed.extend(range(97,123)) # a~z
    allowed.append(45) # -
    allowed.append(46) # .
    allowed.append(95) # _
    for ans in answer:
        if ord(ans) not in allowed:
            answer = answer.replace(ans,'')
    
    # step3
    while '..' in answer:
        answer = answer.replace('..','.')
        
    # step4
    if len(answer) >1 :
        if answer[0] == '.':
            answer = answer[1:]
        if answer[-1] == '.':
            answer = answer[:-1]
    else: # step5
        if answer == '':
            answer = 'a'
    
    # step6
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        if answer[0] == '.':
            answer = ''
        else:
            answer = answer[:14] #answer.replace(answer[-1],'')
    
    #step 5
    if answer == '':
        answer = 'a' #위에서 empty string이 될 수 있으므로 다시 a로 채우기 (step 순서를 맞추는게 아닌가보다)
        
    # step7
    while len(answer) < 3 :
        answer = answer + answer[-1]
        
    return answer

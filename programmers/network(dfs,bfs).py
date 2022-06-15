def solution(n, computer):
    answer = 0
    
    def dfs(c):
        if computer[c][c] == 0:
            return
        else:
            computer[c][c] = 0 # mark as checked
            neighbors = [i for i in range(n) if computer[c][i]==1]
            
            for neighbor in neighbors:
                computer[c][neighbor], computer[neighbor][c] = 0, 0
                dfs(neighbor)
    
    for c in range(n):
        if computer[c][c] != 0:
            dfs(c)
            answer += 1

    return answer

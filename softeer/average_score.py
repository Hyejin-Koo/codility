import sys

a = list(map(int,sys.stdin.readline().split()))
N = a[0] # the number of students
K = a[-1] # the number of cases

score = list(map(int,sys.stdin.readline().split()))

for i in range(K):
    ran = list(map(int,sys.stdin.readline().split()))
    average = sum(score[ran[0]-1:ran[-1]]) / (ran[-1]-ran[0]+1)
    print("%.2f"%round(average,2))

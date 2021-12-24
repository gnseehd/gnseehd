# 예산
# 나의 풀이
from itertools import combinations as cb

def solution(d, budget):
    d.sort() # 오름차순으로 정렬
    cb_ = []
    for i in range(1,len(d)+1): # cb_에 모든 조합을 추가.
        cb_ += cb(d,i)
    
    cb_sum_ = []
    for j in cb_: # cb_sum_에 모든 조합의 합을 추가.
        cb_sum_.append(sum(j))    
    
    max_total = cb_sum_[0] # cb_sum_ 내에서 budget보다 작거나 같을 경우에서의 최대값
    idx = 0 # 최대값일 때의 인덱스값
    
    if max_total > budget: # 가장 첫 요소가 budget보다 클 경우 
        answer = 0
    else: # 그 외에 모든 경우
        for k in cb_sum_[1:]:
            if k <= budget:
                # max_total = k
                idx += 1
        max_combi = cb_[idx]
        answer = len(max_combi)
            
    return answer
# 테스트 케이스는 모두 통과
# 정확성 테스트에선 문제 6번까지만 정답처리가 되고 이후 시간초과
# 효율성이 많이 떨어지는 것 같음.

# 수정된 나의 풀이
def solution(d, budget):
    d.sort() 
    cb_ = []
    for i in range(1,len(d)+1): 
        cb_ += cb(d,i)
    
    idx = 0
    if d[0] > budget:
        return 0
    else:
        for j in cb_[1:]:
            if sum(j) <= budget:
                idx += 1
        return len(cb_[idx])

# 기존의 것을 줄인 것이기 때문에 이상 없음.
# combination의 경우 많은 경우의 수를 생각해 내고 이를 진행하기 때문에
# d의 길이가 커지 경우 런타임에러가 발생할 수도 있음
# combination을 사용하지 않고 푸는 방법을 생각해야함.

# 행렬의 덧셈
# 나의 풀이
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        total = []
        for j in range(len(arr1[i])):
            sum_ele = arr1[i][j] + arr2[i][j]
            total.append(sum_ele)
        answer.append(total)
    return answer

# 다른 사람 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer

# 다른 사람 풀이
def sumMatrix(A,B):
    for i in range(len(A)) :
        for j in range(len(A[0])):
            A[i][j] += B[i][j] 
    return A

# source : https://programmers.co.kr/learn/challenges

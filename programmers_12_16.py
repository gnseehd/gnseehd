# 음양 더하기
# 나의 풀이
def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if signs[i] == True: # == True 를 생략 가능하다. 이전 sign = 0 if sign: 과 동일한 맥락
            total += absolutes[i]
        else:
            total -= absolutes[i]

    return total
# 다른 사람 풀이
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer

# enumerate() 함수는 인자의 값을 추출할 때 인덱스를 추출하는 기법
# zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받아 동일한 개수로 이루어진 자료형을 묶어서 튜플 형태로 반환.

# 소수 만들기
# 나의 풀이
from itertools import combinations
def solution(nums):
    combi = list(combinations(nums,3))
    combi_sum = []
    
    for sum in combi:
        total = sum[0] + sum[1] + sum[2]
        combi_sum.append(total)
        total = 0
    
    prime_num = 0
    divisor = []
    for num in combi_sum:
        for i in range(1, num+1):
            if num %i == 0:
                divisor.append(i)
        
        if len(divisor) == 2:
            prime_num += 1
        else:
            pass
        
        divisor.clear()

    return prime_num

# 다른 사람 풀이
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

# for문 2개가 중첩이 될 경우 효율성이 매우 낮아진다. 실제로 내 코드를 돌렸을 때 시간이 매우 길게 나오는 것을 확인.
# 나는 모든 약수를 구하고 약수 list의 길이가 2일 경우를 찾아 prime_num += 1 을 실행함.
# 굳이 그렇게 하지 않고 제일 안쪽 for문이 돌아갈 때 끝까지 도착하기 전에 한 번이라도 나누어 지면 
# 소수가 아니기 때문에 break를 하는 것이 매우 좋아보임.
# 그리고 다른 사람의 풀이를 보면 if문이 아니라 else문을 사용함으로 바로바로 구해준다.


# 체육복
# 나의 풀이
def solution(n, lost, reserve):
    have_s = []
    for i in range(1, n+1):
        if i not in lost:
            have_s.append(i)
    
    for j in reserve:
        if (j-1) == 0:
            pass
        elif (j-1) not in have_s:
            have_s.append(j-1) 
        else:
            pass
        
        if (j+1) > n:
            pass
        elif (j+1) not in have_s:
            have_s.append(j+1)
        else:
            pass
    print(have_s)
    
    return len(have_s)

# 해결 못함 

# 약수의 개수와 덧셈
# 나의 코드
def solution(left, right):    
    list_di = []
    answer = []
    for num in range(left, right+1):
        for i in range(1, num+1):
            if num %i == 0:
                list_di.append(i)
        
        if len(list_di) %2 == 0:
            answer.append(num)
        else:
            answer.append(-num)
        list_di.clear()
    
    return sum(answer)

# 다른 사람 풀이
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5: # 뭔 개소리야;;
            answer -= i
        else:
            answer += i
    return answer

# 제곱수의 약수의 개수는 홀수이다. => 반례가 존재. 근데 못 찾음. 
# 약수가 홀수일 경우 그 수는 제곱수이다. 라는 명제로 다른 사람은 풀이를 진행함.

# source : https://programmers.co.kr/learn/challenges
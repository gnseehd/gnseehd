# 김서방 찾기
# 나의 풀이
def solution(seoul):
    norm_index = seoul.index(seoul[0])
    for word in seoul:
        if word != 'Kim':
            norm_index += 1
            pass
        else:
            answer = f'김서방은 {norm_index}에 있다'
            
    return answer

# 수정된 나의 풀이
def solution(seoul):
    kim_index = seoul.index('Kim')
    answer = f'김서방은 {kim_index}에 있다'
             
    return answer

# 다른 사람 풀이
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# 소수 찾기
# 나의 풀이
def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i %j == 0:
                break
        else:
            answer += 1
    return answer

# 수정된 나의 풀이 # 에라토스테네스의 체 # 소수 찾기 알고리즘
def solution(n):
    all_nums = [True] * (n+1)
    m = int(n ** 0.5)
    
    for i in range(2, m+1):
        if all_nums[i] == True:
            for j in range(i+i, n+1, i):
                all_nums[j] = False
    answer = 0
    for k in range(2, n+1):
        if all_nums[k] == True:
            answer += 1
            
            
    return answer

# 다른 사람 풀이
# 다 에라토스테네스의 체로 해결함
# 내 기존 풀이의 경우 소수를 찾을 수 있으나, 결국 수가 커질 경우 타임에러가 발생했음.

# 수박수박수박수 ?
# 나의 풀이
def solution(n):
    str_1 = '수'
    str_2 = '박'
    list_str = []
    for i in range(1,n+1):
        if i %2 == 1:
            list_str.append(str_1)
        else:
            list_str.append(str_2)
            
    answer = ''.join(list_str)
    
    return answer

# 다른 사람 풀이
def water_melon(n):
    s = "수박" * n
    return s[:n]

# 현타 옴.

# 문자열 정수로 변환
# 나의 풀이
def solution(s):
    answer = int(s)
    return answer

# 약수의 합
# 나의 풀이
def solution(n):
    answer = 0

    for i in range(1, n+1):
        if n %i == 0:
            answer += i
    return answer

# 다른 사람 풀이
def solution(n):
    answer = n 
    for i in range(1, n//2 +1):
        if n %i == 0:
            answer += i 
    return answer

# 주어진 n값의 절반+1 까지만 진행하여도 상관 없음. 

# 자릿수 더하기
# 나의 풀이
def solution(n):
    n = str(n)    
    answer = 0
    for i in n:
        answer += int(i)
    return answer

# 다른 사람 풀이
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

# 자연수 뒤집어 배열로 만들기
# 나의 풀이
def solution(n):
    n = str(n)
    answer = []
    for i in n[::-1]:
        answer.append(int(i))
    return answer

# 다른 사람 풀이
# map 함수 사용하여 실행 

# 정수 내림차순으로 정리하기
# 나의 풀이
def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    answer = int(''.join(n))
    return answer

# 다른 사람 풀이
# 비슷하게 해결함

# 정수 제곱근 판별
# 나의 풀이
def solution(n):
    str_m = str(n ** 0.5)
    list_m = str_m.split('.')
    if int(list_m[1]) == 0:
        answer = (int(list_m[0]) + 1) ** 2
    else:
        answer = -1

    return answer

# 다른 사람 풀이
def solution(n):
    m = n ** 0.5
    if m %1 == 0:
        answer = (m+1) ** 2
    else:
        answer= -1
         
    return answer

# 처음 type(m) == int: 로 실행을 했으나 m 은 항상 float형태를 가지기 때문에 모든 answer = -1 을 가짐.
# 따라서 m 값을 split을 통해서 소수점 뒷자리가 0 일 경우 m+1 ** 2 를 진행함
# 다른 사람 풀이를 보면 나누기 1을 진행했을 때 나머지가 0 일 경우 == 제곱근이 0 을 의미 

# 제일 작은 수 제거하기
# 나의 코드
def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
    else:
        arr[0] = -1
    return arr

# 다른 사람 풀이
# 비슷함

# 짝수와 홀수
# 나의 풀이
def solution(num):
    if (num == 0) or (num %2 == 0):
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

# 최대 공약수 최소 공배수
# 나의 풀이
def solution(n, m):
    # 약수 구하기
    n_divisor = []
    m_divisor = []
    for i in range(1,n+1):
        if n %i == 0:
            n_divisor.append(i)
    for j in range(1,m+1):
        if m %j == 0:
            m_divisor.append(j)
    
    # 최대공약수 구하기
    max_divisor = n_divisor[0]
    for divisor in n_divisor[1:]:
        if divisor in m_divisor:
            max_divisor = divisor

    
    # 최소공배수 구하기
    n_multi = []
    m_multi = []
    num = 1
    while True:
        n_multi.append(n*num)
        m_multi.append(m*num)
        min_multi = n_multi[num-1]
        if min_multi in m_multi:
            break
        else:
            num += 1
            
    return [max_divisor, min_multi]

# 다른 사람 풀이 # 유클리드 호제법
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 나의 풀이는 런타임 에러 발생함 
# 공약수를 구하고 최대 공약수를 구하는 과정은 문제가 없었으나 while문 사용중에서
# 수가 커질수록 오래 걸리는 단점이 있었음
# 새로 알게 된 사실은 최소 공배수는 최대 공약수를 알고 있을 때
# (m * n)/최대 공약수 라는 사실이다.
# 이렇게 수정하고 프로그램을 실행 시 런타임 에러 발생하지 않음
# 유클리드 호제법은 처음 알았음;;

# source : https://programmers.co.kr/learn/challenges
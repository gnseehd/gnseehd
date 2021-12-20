# 플라츠 추측
# 나의 풀이
def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    else:
        while True:
            if num != 1:
                if num %2 == 0:
                    num = num / 2
                    answer += 1
                else:
                    num = num * 3 + 1
                    answer += 1

            else:
                break
            
            if answer >= 500:
                answer = -1
                break
    return answer

# 수정된 나의 풀이
def solution(num):
    answer = 0
    while True:
        if num != 1:
            if num %2 == 0:
                num = num / 2
            else:
                num = num * 3 + 1
            answer += 1
        else:
            break
            
        if answer == 500:
            return -1
    return answer

# if num != 1: 이 부분에 대하여 모든 경우에 따라서 answer은 +1 이 되므로 모두 answer += 1 을 넣어줄 이유가 없음

# 평균 구하기
def solution(arr):
    return sum(arr)/len(arr)

# 하샤드 수 구하기
# 나의 풀이
def solution(x):
    x = str(x)
    total_x = 0
    for w in x:
        total_x += int(w)
    
    if int(x) %total_x == 0:
        answer = True
    else:
        answer = False
        
    return answer

# 수정된 나의 풀이
def solution(x):
    x = str(x)
    s = 0
    for w in x:
        s += int(w)
        
    return True if int(x) %s == 0 else False

# 기존 풀이에서 if/else문을 바로 return 옆으로 이동시킴
# 이때 :는 들어가지 않는다.

# 핸드폰 번호 가리기
# 나의 풀이
def solution(ph_numbers):
    ph_numbers = str(ph_numbers)
    list_num = []
    for i in ph_numbers[:-4]:
        list_num.append('*')
    for j in ph_numbers[-4:]:
        list_num.append(j)
    answer = ''.join(list_num)
    return answer

# 다른 사람 풀이
def solution(ph_numbers):
    return '*'*(len(ph_numbers[:-4]))+ph_numbers[-4:]

# source : https://programmers.co.kr/learn/challenges
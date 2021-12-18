# 체육복
# 나의 풀이

# 요일 계산기
# 나의 풀이
def solution(a, b):
    import datetime
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    return days[datetime.date(2016,a,b).weekday()]

# 다른 사람 풀이
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

# 두 개 뽑아서 더하기
# 나의 풀이
def solution(numbers):
    from itertools import combinations as cb
    new_list = []
    
    for i in cb(numbers,2):
        sum_cb = sum(i)
        if sum_cb not in new_list:
            new_list.append(sum_cb)
    new_list.sort()
    return new_list

# 다른 사람 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
# 나의 풀이의 경우, 조합 함수를 사용해준 뒤, 이들의 합을 구하고 
# 새로운 리스트에 append() 함수를 사용하여 넣어준다.
# 그러나 이미 존재할 경우, 넣지 않는다.
# 다른 사람의 경우, 조합을 생각하지 않고 i와 j(i+1)를 더해준 뒤
# set 함수를 사용함으로 중복제거를 해준다.
# test 7 의 경우 나의 풀이는 4.64ms 다른 사람의 풀이는 0.46ms 
# 내 풀이가 매우 느리다.

# 부족한 금액 계산하기
# 나의 풀이
def solution(price, money, count):
    result_price = 0
    
    for i in range(1,count+1):
        result_price += (price*i)
    
    if money >= result_price:
        answer = 0
    else:
        answer = result_price - money        
    return answer

# 예산
# 나의 풀이
def solution(d, budget):
    from itertools import combinations as cb
    all_cb = []
    for a in range(2,len(d)+1):
        com = list(cb(d,a))
        all_cb.extend(com)
    
    all_cb_sum = []
    
    for b in all_cb:
        sum_cb = sum(b)
        all_cb_sum.append(sum_cb)
    # print(all_cb)
    # print(all_cb_sum)
    # answer = 0
    max_cb = all_cb_sum[0]
    for k in range(1,len(all_cb_sum)+1):
        if all_cb_sum[k] <= budget:
            if all_cb_sum[k] >= max_cb:
                max_cb = all_cb_sum[k]
                max_cb_index = all_cb_sum.index(max_cb)
        else:
            pass
    answer = len(all_cb[max_cb_index])
    return answer
# 현재 max_cb 인덱싱에서 막힘.
# 해결 못함.

# 같은 숫자는 싫어
# 나의 풀이
def solution(arr):
    answer = []
    norm_num = arr[0]
    answer.append(norm_num)

    for num in arr[1:]:
        if num == norm_num:
            pass
        else:
            answer.append(num)
            norm_num = num
    return answer

# 수정된 나의 풀이
def solution(arr):
    answer = []

    for num in arr:
        if (len(answer)==0) or (answer[-1] != num):
            answer.append(num)
        else:
            pass
    return answer

# 다른 사람 풀이
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue 
        a.append(i)
    return a
# 리스트에서 슬라이싱을 활용하면 벗어나도 문제가 없다.
# if a[-1:] == [i]: continue 여기서 [i]는 일반 문자열에서 해당 i 를 리스트에 넣어줌으로
# a[-1:] == [i] 즉 리스트 a의 마지막과 비교하는 것.

# 다른 사람 풀이
def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c): # 처음 시작을 넣어주고, result 마지막 값과 c가 다르면 추가.
            result.append(c)
    return result

# 문자열 내 p와 y의 개수
# 나의 풀이
def solution(s):
    p = 0
    y = 0
    for char in s:
        if (char == 'p') or (char == 'P'):
            p += 1
        elif (char == 'y') or (char == 'Y'):
            y += 1
    
    if p == y:
        answer = True
    elif p != y:
        answer = False
    elif (p == 0) and (y == 0):
        answer = True

    return answer

# 수정된 나의 풀이
def solution(s):
    p = 0
    y = 0
    for char in s:
        if (char == 'p') or (char == 'P'):
            p += 1
        elif (char == 'y') or (char == 'Y'):
            y += 1
    
    return p == y
# 다른 사람의 풀이
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')

# 모든 문자를 소문자로 변경 뒤, count()함수로 개수 비교
# 이 둘이 같을 경우에만 True 가 나오고, 이 외에는 모두 False 출력

# source : https://programmers.co.kr/learn/challenges
# 나누어 떨어지는 숫자 배열
# 나의 풀이
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i %divisor == 0:
            answer.append(i)
            answer.sort()
    
    if len(answer) == 0:
        answer.append(-1)
    return answer

# 다른 사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

# or의 경우, or의 앞부분이 True = 앞부분으로 출력
# or의 앞부분이 Falese = 뒷부분 출력
# comprehension이 사용된 듯 함.
# comprehension이란
# iterable한 오브젝트를 생성하기 위한 방법중 하나로 파이썬에서 사용할 수 있는 유용한 기능중 하나이다.

# 문자열 다루기
# 나의 풀이
def solution(s):
    if (len(s)==4) or (len(s)==6):
        if s.isdigit():
            return True
    else:
        return False

# 다른 사람 풀이 
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)

# 체육복
# 나의 풀이
def solution(n, lost, reserve):
    answer = n - len(lost)
    
    for i in range(len(reserve)):
        if (reserve[i]-1) in lost:
            answer += 1
            lost.remove(reserve[i]-1)
        elif (reserve[i]+1) in lost:
            answer += 1
            lost.remove(reserve[i]+1)

    return answer
# 현재 65점

# 수정된 나의 풀이 1
# 여벌의 옷을 가진 학생이 도둑맞은 경우 추가.
def solution(n, lost, reserve):
    for i in reserve:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    for i in range(len(reserve)):
        if (reserve[i]-1) in lost:
            lost.remove(reserve[i]-1)
            continue
        elif (reserve[i]+1) in lost:
            lost.remove(reserve[i]+1)

    return n - len(lost)
# 현재 75점
# 질문하기 속 많은 데이터케이스를 추가해도 다 통과인데 1, 3, 5, 18, 20번만 통과를 못함.
# 빡치네 ;;

# 수정된 나의 풀이 2
def solution(n, lost, reserve):
    res_unq = set(reserve) - set(lost)
    los_unq = set(lost) - set(reserve)
    
    for i in res_unq:
        if i-1 in los_unq:
            los_unq.remove(i-1)
        elif i+1 in los_unq:
            los_unq.remove(i+1)

    return n - len(los_unq)

# 중복되지 않는다. = 고유하다.(unique)
# set으로 각각 리스트를 중복 제거한 뒤, -(차집합)으로 빼준다.
# list의 경우 '-' 을 지원하지 않기 때문에 set으로 해줌.
# 이후 동일 
# set을 떠올리는 것이 문제였음.


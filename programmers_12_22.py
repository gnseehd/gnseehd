# x만큼 간격이 있는 n개의 숫자
# 나의 풀이
def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

# 이상한 문자 만들기
# 나의 풀이
def solution(s):
    s = s.upper()
    answer = []
    idx = 0
    
    for w in s:
        if w == ' ': # 단어의 공백을 기준으로 인덱스를 판단해야함.
            answer.append(w) 
            idx = 0
        elif (idx == 0) or (idx %2 == 0):
            answer.append(w)
            idx += 1
        else:
            answer.append(w.lower())
            idx += 1
    answer = ''.join(answer)
    
    return answer

# 다른 사람 풀이
def solution(s):
    answer = ''
    for word in s.split(" "):
        n = ''
        for i in range(len(word)):
            if i%2 == 0 :
                n += word[i].upper()
            else :
                n += word[i].lower()
        answer += (n + " ")
    return answer[0:-1]

# 나의 풀이는 인덱스를 += 1을 해줌으로 홀수와 짝수를 구별함.
# 이때 공백일 경우, 인덱스값을 0으로 초기화 해줌.
# 다른 사람 풀이의 경우 split으로 분리를 한 뒤,
# 단어 하나를 완성시킨 후, ' '공백을 붙여주고 마지막에 
# 슬라이싱을 통해서 제일 뒤에 붙은  ' '를 삭제해줌.

# 숫자 문자열과 영단어
# 나의 풀이
def solution(s):
    s = list(s)
    print(s)
    answer = []
    numbers = {'one':1, 'two':2, 'three':3, 'four':4, 
               'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for w in s:
        word = ''
        if type(w) is str:
            word += w
            if word in numbers:
                answer.append(numbers[word])
            else:
                pass
        else:
            answer.append(w)
    answer = ''.join(answer)    
    return answer
# answer 값이 빈칸으로 나옴
# 조금 더 수정해 봐야 할 것 같음
# 제한시간은 10초 이내로 출력값이 나와야 함

# 완주하지 못한 선수
# 나의 풀이
def solution(participant, completion):
    for name in completion:
        if name in participant:
            participant.remove(name)
    return participant[0]

# 정확성 테스트는 모두 통과했지만 효율성 테스트는 통과하지 못함
# in함수가 두 번 이상 사용될 경우, 시간은 두 배가 아닌, 제곱배로 늘어남.
# 따라서 효율성 테스트를 통과하기 위해서 in함수를 빼는 방향으로 고쳐 나가야 함.

# 수정된 나의 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(' ')
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            return participant[i]
# 이름을 알파벳 순으로 정렬한 뒤 한명 씩 비교
# 처음 뜬 에러는 인덱스가 다르다 => participant의 길이가 completion의 길이보다 +1 이므로 
# ' '을 append 해줌.

# 다른 사람 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]

# 이 사람은 추가를 하지 않고 for문이 돌아가는 동안 return값이 나오지 않는다면 
# participant에서 제일 마지막 사람이 완주하지 못한 선수가 되므로
# return participant[len(participant)-1]

# 또 다른 사람 풀이
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 12/23 공부
# source : https://programmers.co.kr/learn/challenges
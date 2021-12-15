# 로또의 최고 순위와 최저 순위
# 나의 풀이
def solution(lottos, win_nums):
    list_same = []
    
    for num in lottos:
        if num in win_nums:
            list_same.append(num)
    zero_nums = lottos.count(0)
    same_nums = len(list_same)
    
    max_v = 7 - (zero_nums + same_nums) # 최대
    min_v = 7 - same_nums # 최소
    
    if same_nums == 6:
        max_v = 1
        min_v = 1
    elif same_nums == 0:
        max_v = 1
        min_v = 6
        if zero_nums == 0: # 0은 없고 6개의 번호가 모두 다른 경우
            max_v = 6
    
    answer = [max_v, min_v]
        
    return answer

# 다른 사람의 풀이
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # rank 리스트를 선언한 뒤, index를 통해서 리턴

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]

# 신규 아이디 추천
# 나의 풀이
def solution(new_id):
    # 1단계
    new_id1 = list(new_id.lower()) 
    
    # 2단계
    new_id2 = [] 
    for word in new_id1:
        if word.isalnum():
            new_id2.append(word)
        elif '-' in word:
            new_id2.append(word)
        elif '_' in word:
            new_id2.append(word)
        elif '.' in word:
            new_id2.append(word)    
    
    # 3단계
    for word1 in new_id2:
        if word1 != '.':
            pass
        elif word1 == '.':
            
    # 4단계
    if new_id2[0] == '.': 
        del new_id2[0]
    elif new_id2[-1] == '.':
        del new_id2[-1]
    
    # 5단계
    new_id3 = []
    for word2 in new_id2:
        if word2 == ' ':
            word2 = 'a'
        new_id3.append(word2)
        
    # 6단계
    if len(new_id3) > 15:
        new_id3 = new_id3[:14]
        if new_id3[-1] == '.':
            new_id3 = new_id3[:13]
    # 7단계
    while len(new_id3) == 3:
        new_id3.append(new_id3[-1])
    
    answer = ''.join(new_id3)
    return answer

    # 해결 x

# k번째 수
def solution(array, commands):
    answer = []
    
    for command in commands:
        arr = array[command[0]-1:command[1]]
        arr.sort()
        ans = arr[command[2]-1]
        answer.append(ans)
            
    return answer

# 없는 숫자 더하기
# 나의 풀이
def solution(numbers):
    all_numbers = [0,1,2,3,4,5,6,7,8,9]
    none_numbers = []
    total = 0
    for num in all_numbers:
        if num not in numbers:
            total += num

    return total

# 다른 사람의 풀이
def solution(numbers):
    total = 45 - sum(numbers)
    return total

# 내적
#나의 풀이
def solution(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i]*b[i]
        
    return total

# 최소 직사각형
# 나의 풀이
def solution(sizes):
    if sizes[0][0] > sizes[0][1]:
        max_w = sizes[0][0]
        max_h = sizes[0][1]
    else:
        max_w = sizes[0][1]
        max_h = sizes[0][0]
    # 큰값을 가로로 가져간다.
    
    for size in sizes[1:]:
        if size[0] >= size[1]:
            w = size[0]
            h = size[1]
        else:
            w = size[1]
            h = size[0]
        
        if w >= max_w:
            max_w = w
        else:
            pass
        
        if h >= max_h:
            max_h = h
        else: 
            pass
    
    answer = max_w * max_h
    return answer

# 다른 사람의 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes) # 뭔 개소리야;;



# source : https://programmers.co.kr/learn/challenges
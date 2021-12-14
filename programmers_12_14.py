# Quiz 1) 같은 숫자는 싫어!
# 11222311 => 1231 

def sol_1(words):
    words = str(words)
    words_list = list(words)
    norm_word = words_list[0]

    new_words = []
    new_words.append(norm_word)
    
    for word in words_list[1:]:
        if word == new_words[-1]:
            pass
        else:
            new_words.append(word)
    
    answer = ''.join(new_words)
    answer = int(answer)

    return answer
        
# words = 1228788897701
# print(solution(words)) 

# Quiz 2) 나누어 떨어지는 숫자 배열 
# [5,9,7,10], 5 => [5,10]

def sol_2(list, x):
    new_list = []
    for i in list:
        if i %x == 0 :
            new_list.append(i)
    return new_list

# list = [12, 3124, 123, 12322, 33, 23]
# print(solution1(list,3))

# Quiz 3) 두 정수 사이의 합
# 3, 5를 입력받을 경우 3+4+5 = 12를 리턴

def sol_3(x, y):
    x_1 = x
    y_1 = y
    
    if x > y:
        x = y_1
        y = x_1
    
    total = 0
    for i in range(x,y+1):
        total += i
    
    return total

# print(sol_3(5,3))

# Quiz 4) 가운데 글자 가져오기
# qwer => we, qwert => e

def sol_4(words):
    index = len(words) // 2

    if len(words) %2 == 0:
        answer = words[index-1:index+1]
    else:
        answer = words[index]
    
    return answer

# words ='computer'
# print(sol_4(words))

# source : https://programmers.co.kr/learn/challenges
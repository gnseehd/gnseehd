# Quiz 4) 단어를 맞추는 hackman 프로그램을 작성하시오. 

# ['apple', 'banana', 'orange', 'strawberry', 'melon'] 과일 이름이 들어가 있는 리스트 작성.
# 리스트 내에서 랜덤으로 하나의 과일을 뽑음. example) apple 
# 과일 이름의 길이만큼 _를 출력. example) _ _ _ _ _
# 한 글자씩 입력을 받고 맞을 경우 Correct, 틀릴 경우 Wrong 를 출력.
# 정답이 맞을 경우, _ 위에 단어를 작성함. 
# 기회는 무제한으로 설정.

import random

fruit_list = ['apple', 'banana', 'orange', 'strawberry', 'melon']
target = random.choice(fruit_list)
target_blank = '_' * len(target)

target_list = list(target)
copy_list = list(target)
target_blank_list = list(target_blank)

print(f'answer : {target}')
print(target_blank)

for i in range(1,11):
    alp = input('알파벳을 입력해주세요:')
    target_answer = ''.join(target_blank_list)

    if alp in target_list:
        counts = target_list.count(alp)

        for count in range(counts):
            index = copy_list.index(alp)
            copy_list[index] = 'X'
            target_blank_list[index] = alp
        
        target_answer = ''.join(target_blank_list)

        print('\n')
        print('CORRECT!')
        print(target_answer)
        print('\n')

    else:
        print('\n')
        print('WRONG!')
        print(target_answer)

    
    if target_answer == target:
        print(f'정답은 {target}으로 맞추셨습니다!')
        break


#--------------------------------------------------------------------------------------------------

# 기존 target_list의 복사본 copy_list를 만들었음.
# 입력 받은 alp가 target_list에 존재하는 만큼 반복문을 다시 실행.
# 해당 alp가 존재하는 위치의 index를 확인한 뒤, copy_list에서 index에 해당하는 값을 X로 변경하는 방향으로 진행.
# example) ['a', 'p', 'p', 'l', 'e'], alp = p, counts = 2
# 첫번째 반복문이 실행되면 ['a', 'p', 'p', 'l', 'e'] => ['a', 'X', 'p', 'l', 'e']로 변경됨.
# 두번째 반복문이 실행되면 ['a', 'X', 'p', 'l', 'e'] => ['a', 'X', 'X', 'l', 'e']로 변경됨.
# 그리고 그 결과 target_answer = _pp___로 변경됨.

from random import *
words = ['apple', 'banana', 'orange', 'strawberry', 'melon']
word = choice(words)
print(f'answer : {word}')
letters = '' # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True
    
    print()
    for w in word:
        if w in letters:
            print(w, end=' ')
        else:
            print('_', end = ' ')
            succeed = False
    print()

    if succeed:
        print('success')
        break


    letter = input('알파벳을 입력해주세요: ')
    if letter not in letters:
        letters += letter

    if letter in word:
        print('correct')
    else:
        print('wrong')

# 12/13
# source : https://www.youtube.com/watch?v=487mr-e_Z74&list=PLMsa_0kAjjrftcNd6xLyY7KUyoc2FBqTP&index=2
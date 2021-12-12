# Quiz 4) 단어를 맞추는 hackman 프로그램을 작성하시오. 

# ['apple', 'banana', 'orange',...] 과일 이름이 들어가 있는 리스트 작성.
# 리스트 내에서 랜덤으로 하나의 과일을 뽑음. example) apple 
# 과일 이름의 길이만큼 _를 출력. example) _ _ _ _ _
# 한 글자씩 입력을 받고 맞을 경우 Correct, 틀릴 경우 Wrong 를 출력.
# 정답이 맞을 경우, _ 위에 단어를 작성함. 
# 기회는 무제한으로 설정.

import random

fruit = ['apple', 'banana', 'orange', 'strawberry', 'melon']
target = random.choice(fruit) # target 설정.
blank_answer = '_' * len(target) 

# target, blank_answer list로 변경.
target_list = list(target)
blank_answer_list = list(blank_answer)

print(f'answer : {target}') 
print(blank_answer)

for i in range(1,11): # 우선은 횟수를 10회로 설정.
    alp = input('알파벳을 입력해주세요: ')
   
    if alp in target_list:
        for j in target_list:
            if j == alp:
                index = target_list.index(j) # target_list 내 j 인덱스를 저장
                blank_answer_list[index] = alp # blank_answer_list에서 저장한 인데스에 해당하는 값을 alp로 변경

        blank_answer = ''.join(blank_answer_list) # 이후 리스트를 문자열로 변경하여 blank_answer을 교체
        
        print('CORRECT !')
        print(blank_answer)

    else:
        print('WRONG !')
        print(blank_answer)

        if blank_answer == target:
            break



# 문자열은 인덱스를 지정하여 문자를 가져올 수 있지만, = 로 문자를 할당할 수 없다.
# 따라서 리스트로 변환한 뒤 값을 변경하고 나서, join함수를 통해 다시 문자열로 변환.
# 현재 중복된 값은 출력되지 않는다.
# 아마도 이중 for문에서 문제가 발생한 듯 하다.

# 12/12
# source : https://www.youtube.com/watch?v=487mr-e_Z74&list=PLMsa_0kAjjrftcNd6xLyY7KUyoc2FBqTP&index=2
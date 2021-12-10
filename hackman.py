# Quiz 4) 단어를 맞추는 hackman 프로그램을 작성하시오. 

# ['apple', 'banana', 'orange',...] 과일 이름이 들어가 있는 리스트 작성.
# 리스트 내에서 랜덤으로 하나의 과일을 뽑음. example) apple 
# 과일 이름의 길이만큼 _를 출력. example) _ _ _ _ _
# 한 글자씩 입력을 받고 맞을 경우 Correct, 틀릴 경우 Wrong 를 출력.
# 정답이 맞을 경우, _ 위에 단어를 작성함. 
# 기회는 무제한으로 설정.
import random

fruit = ['apple', 'banana', 'orange', 'strawberry', 'melon']
random_fruit = random.choice(fruit) # random_fruit 설정
random_fruit_list = list(random_fruit) # random_fruit 알파벳을 모두 분해하여 리스트로 변환

for i in random_fruit_list: # random_fruit_list 각 단어에 인덱싱을 부여함.
    word_index = random_fruit_list.index(i)

game_word = '_ ' * len(random_fruit) # random_fruit의 단어 길이 만큼 _ 생성

print(f'answer : {random_fruit}') 
print(game_word)

for i in range(1,22): # 알파벳의 개수만큼 for문 작동
    alp = input('알파벳을 입력해주세요: ') # 앞파벳을 매 반복문마다 입력받음.
    if alp in random_fruit:

# 12/10 
# source : https://www.youtube.com/watch?v=487mr-e_Z74&list=PLMsa_0kAjjrftcNd6xLyY7KUyoc2FBqTP&index=2
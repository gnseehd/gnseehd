# tuple
# list = [], tuple = () 이때, tuple 의 경우 ()를 생략 가능하다.
# list_1 = [1,2,3,4]
# tuple_1 = (1,2,3,4)
# print(list_1)
# print(tuple_1)
# print(type(list_1), type(tuple_1))

# tuple_2 = 1,2,3,4
# print(tuple_2, type(tuple_2))

# tuple_3 = 'one',
# print(tuple_3, type(tuple_3)) # tuple의 경우 한 개의 아이템을 가지고 있을 경우, 반드시 ','를 넣어줘야함.

# tuple과 list의 공통점
# 1. 순서가 있는 시퀀스 타입이다.
# 2. 인덱스가 가능하다.
# 3. 슬라이싱이 가능하다.
# 4. 이터레이터 오브젝트이기에, for문에 사용 가능하다. 

# tuple과 list의 차이점
# list의 경우 정의된 값을 변경할 수 있지만, tuple의 경우 한 번 정의되면 변경이 불가능 하다.
# tuple의 경우 append, remove와 같은 추가 변경 삭제가 불가능하다.
# index, count의 함수는 사용 가능하다.
# tuple은 list보다 메모리를 적게 사용하며, 오브젝트 생성속도가 더 빠르다.


# class
# class (class_name): # class 선언
#     def __init__(self): # class 실행시 __init__함수가 바로 실행된다.
# self = class를 할당하는 자신을 의미함.

# class JSS:
#     def __init__(self): # __init__ 함수는 클래스가 실행됨에 따라 곧바로 실행이 됨.
#         print('JSS 클래스 실행') 
#     def show(self): # show 함수는 직접 실행을 시켜줘야 실행이 된다.
#         print('show 실행')


# a = JSS() # a = self 가 된다.

# class JSS():
#     def __init__(self):
#         self.name = input('이름: ')
#         self.age = int(input('나이: '))
#     def show(self):
#         print(f'이름은 {self.name}이며, 나이는 {self.age}입니다. ')

# # 기존 JSS class에 새로운 class를 만들어 덮어주기
# class JSS2(JSS):
#     def __init__(self):
#         super().__init__() # 기존 JSS의 init함수를 가져온다.
#         self.gender = input('성별: ')
#     def show(self):
#         print(f'이름은 {self.name}, 성별은 {self.gender}이며 나이는 {self.age}입니다.'

# Quiz 3) 신조어 퀴즈 클래스를 만드시오.
# class Word():
#     def __init__(self, word1, word2, word3, answer):
#         self.word1 = word1
#         self.word2 = word2
#         self.word3 = word3
#         self.answer = answer

#     def show_question(self):
#         print(f'{self.word1}의 뜻은 ?\n1:{self.word2}\n2:{self.word3}')

#     def check_answer(self):
#         ans = input('=> ')
#         if ans == 1:
#             print('정답입니다.')
#         elif ans == 2:
#             print('틀렸습니다.')

# word = Word('얼죽아', '얼어 죽어도 아이스 아메리카노', '얼굴만은 죽어도 아기피부', 1)
# print(word.show_question())
# print(word.check_answer())

class Word():
    def __init__(self, word, ex1, ex2, answer):
        self.word = word
        self.ex1 = ex1
        self.ex2 = ex2
        self.answer = answer

    def show_question(self):
        print(f'\"{self.word}\"의 뜻은 ?')
        print(f'1. {self.ex1}')
        print(f'2. {self.ex2}')

    def check_answer(self, user_input):
        if user_input == self.answer:
            print('정답입니다.')
        else:
            print('틀렸습니다.')

word = Word('얼죽아', '얼어 죽어도 아이스 아메리카노', '얼굴만은 죽어도 아기피부', 1)
print(word.show_question())
print(word.check_answer(int(input('=> '))))

# source https://www.youtube.com/watch?v=btpZOB_TvQ4&list=PLMsa_0kAjjrftcNd6xLyY7KUyoc2FBqTP&index=4
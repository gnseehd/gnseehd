# # 최대공약수 구하기
# def solution1(x, y):
#     new_x = x
#     new_y = y
#     if x > y: # x 가 y보다 더 크다.
#         x = new_y
#         y = new_x
#     else:
#         pass
    
#     for i in range(1, x+1):
#         if (x % i == 0) and (y % i == 0):
#             gcd = i
#     return gcd

# # 최대공배수 구하기
# def solution2(x,y):
#     data_x = []
#     data_y = []
#     sign = 0
#     for i in range(1,101):
#         mul_x = x * i
#         mul_y = y * i
#         data_x.append(mul_x)
#         data_y.append(mul_y)
#         for j in data_x:
#             if i in data_y:
#                 mcl = i
#                 sign = 1
#                 break
#         if sign:
#             break
#     return mcl
# x = 10 
# y = 30 
# print(solution2(x,y))

# 001
# print('hello world')

# 002
# print("Mary's cosmetics")
# 문자열에 ' or "을 집어넣을 경우 문자열을 반대되는 것으로 작성

# 003
# print('신씨가 소리질렀다. "도둑이야."')

# 004
# print('"C:\Windows"')

# 005
# print('안녕하세요.\n만나서\t\t반갑습니다.')
# \n = enter \t = tab

# 006
# print('오늘은','일요일')

# 007 
# print('naver;kakao;sk;samsung')

# 008
# print('naver\kakao\sk\samsung')

# 009
# print('first', end='');print('second')
# print()와 print()사이에 ; 를 넣어주면 줄바꿈 없이 사용 가능하다.

#010
# print(5/3)

# 011
# samsung = 50000
# print(f'삼성전자의 주식 10주를 보유한다면, 총 평가금액은 {samsung * 10}원 입니다.')

# 012
# Mc = 29800000000000
# pv = 50000
# per = 15.79
# print(Mc, type(int))
# type(int)를 작성할 시 class가 나온다.

# 013
# s = 'hello'
# t = 'python'
# print(f'{s}! {t}')

# 014
# print(2+2*3)

# 015
# a = 128
# print(type(a))

# 016 문자열 정수로 변환
# num_str = '720'
# num_str = int(num_str)
# print(type(num_str))

# 017 정수를 문자열로 변환
# num = 100
# num = str(num)
# print(type(num))

# 018 문자열을 실수로 변환
# str_num = '15.79'
# str_num = float(str_num)
# print(type(str_num))

# 019 문자열을 정수로 변환
# year = '2020'
# year = int(year)
# print(year, year+1, year+2)
# for i in range(3):
#     print(year+i)

# 020
# ac = 48584
# print(f'에어컨의 총 금액은 {ac*36}원 입니다.')

# 021
# letters = 'python'
# print(letters[0:3:2])
# print(letters[0],letters[2])

# 022
# license_plate = '24가 2210'
# print(license_plate[-4:])
 
# 023
# str = '홀짝홀짝홀짝'
# print(str[0::2])

# 024
# str = 'PYTHON'
# print(str[-1::-1])

# 025
# phone_number = '010-1111-2222'
# phone_number = phone_number.replace('-',' ')
# print(phone_number)

# 026
# phone_number = phone_number.replace('-','')
# print(phone_number)

# 027
# url = 'http://sharebook.kr'
# print(url.split('.')[1])

# 028
# lang = 'python'
# lang[0] = 'p'
# print(lang)
# 문자열은 수정이 불가능하다. 할당 메서드를 지원하지 않는다.

# 029
# str = 'sajnfekndsjanfeaaw'
# print(str.replace('a','A'))

# 30
# str = 'abcd'
# print(str.replace('b','B'))

import os
os.getcwd()
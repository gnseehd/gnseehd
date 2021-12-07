# Quiz1) 사회적 거루두기에 따른 영화 예매 시스템을 만드시오 
# 각 열은 1 ~ 20번까지 총 20개의 좌석으로 구성되어 있습니다.
# A1 A2 A3 ... A20
# B1 B2 B3 ... B20
# C1 C2 C3 ... C20
# 이때, A 열에 대하여 홀수로 끝나는 좌석에 대해서만 출력(각 좌석은 ""으로 구분)

# my answer
# layer = ['A', 'B', 'C']
# for i in layer:
#     for num in range(1,21):
#         if num %2 == 0:
#             pass
#         else:
#             print(f'{i}{num}', end=' ')
#     print('\n')

# 1
# for i in range(1,21)[::2]: # range 함수에서 [start : end : step] 지정 가능함.
#     print(f'A{i}', end=" ")

# 나는 한번에 모든 ABC열을 만들어야 하는 줄 알았음.
# range 함수에서도 silcing처럼 지정이 가능하다.

low = ['A', 'B', 'C']
for layer in low:
    for number in range(1,21)[::2]:
        print(f'{layer}{number}', end=' ')
    print()
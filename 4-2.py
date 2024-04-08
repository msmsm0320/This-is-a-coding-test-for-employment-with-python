"""정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도
포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
입력 예시 
5
출력 예시
11475"""
N = int(input())
count = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count+=1

print(count)




# 시,분,초가 나오면 60씩 끊어서 생각하자
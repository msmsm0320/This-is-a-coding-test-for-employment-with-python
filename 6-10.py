'''하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다.
수열을 내림차순으로 정렬하는 프로그램을 만드시오.

입력 조건
- 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
- 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의 자연수이다.

출력 조건
- 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.'''

n = int(input())

d = []
for i in range(n):
    d.append(int(input()))

d.sort(reverse=True)

for i in d:
    print(i, end=' ')
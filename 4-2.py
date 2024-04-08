#4-1

move_type = ['L','R','U','D']
x,y = 1, 1
n = int(input())
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for plan in plans:
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        
    if 1<=nx<=n and 1<=ny<=n:
        x,y = nx, ny
print(x, y)





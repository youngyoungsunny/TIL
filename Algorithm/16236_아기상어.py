import sys
from collections import deque

#https://11001.tistory.com/96 아주 참고하기 좋음.

n = int(input())

siteArr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0] #상어가 움직일 수 있는 곳
dy = [0,0,-1,1]

sx, sy = 0,0 #상어 위치 표시

for i in range(n):
    for j in range(n):
        if siteArr[i][j] == 9: #아기상어가 위치한 곳이라면?
            siteArr[i][j] = 0 #그 위치를 0으로 바꿔줘야 함 !!!!!!!!!!!!!!( 중요!!!!!!!)
            #안그러면 나중에 9라서 아기상어가 못 지나갈 수 있음.
            sx, sy = i, j #상어 위치를 이곳으로 바꾸기
            break

babySharkSize = 2 #맨 처음 아기상어 크기 2
move_num = 0 #상어가 움직인 횟수
eat = 0 #상어가 물고기 먹은 횟수

while True:
    q = deque()
    q.append((sx, sy, 0)) #상어 위치인 x,y, 먹은 물고기
    visited = [[False] * n for _ in range(n)]
    flag = 1e9 #1에 10의 9제곱을 곱한 값 즉, 1e9 = 1*109 = 1000000000,
    fish = []

    while q:
        x, y, count = q.popleft()

        if count > flag:
            break
            
        for i in range(4): #갈수있는 곳이 4군데 이기 때문에
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny >= n: #사이즈를 넘어가는 곳은 넘어감
                continue
            if siteArr[nx][ny] > babySharkSize or visited[nx][ny]: #size보다 크거나 혹시 방문을 했던 곳이면 넘어감
                continue

            #그 위치에 아무도 없지 않고(즉, 물고기가 있고), 물고기의 크기가 아기상어보다 작으면
            if siteArr[nx][ny] != 0 and siteArr[nx][ny] < babySharkSize:
                fish.append((nx, ny, count+1)) #fish의 위치, 아기상어가 움직인 크기 더해주기
                flag = count #flag에 count값을 넣어줌.

            visited[nx][ny] = True #방문했음
            q.append((nx,ny,count+1)) #현재 아기 상어 상태를 이렇게 바꿔주기

    if len(fish) > 0: #아기 상어가 먹을 수 있는 물고기가 있다면
        fish.sort() #다 모은 fish들을 sort한다.

        #그리고 제일 앞에 있는, 즉, 가장 작은 것의 sort를 쓴다. -->  fish[0]
        x, y, move = fish[0][0], fish[0][1], fish[0][2] #x,y위치, 그리고 움직인 수를 받아옴
        move_num += move #움직인 거리에 move값을 더 해주고
        eat += 1 #먹은 물고기 수를 추가해줌.
        siteArr[x][y] = 0 #그 자리 물고기가 사라지는 것이므로 0으로 바꿔줌.

        if eat == babySharkSize: #먹은거랑 사이즈가 똑같으면
            babySharkSize += 1 #아기상어 현재 크기만큼 물고기 (개수) 먹으면 아기상어 크기+1
            eat = 0

        sx, sy = x, y #아기상어 위치 갱신
    
    else:
        break

print(move_num)

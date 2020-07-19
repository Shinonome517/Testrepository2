#幅優先探索による最短経路
"""
----------------------------------------------------------------------------------------------------
ステージ情報：通路；"."　床及び壁；"#"　プレイヤーの位置；座標　敵の位置；座標

欲しい変数:

    stage_inf:上記のステージの情報
    sy,sx:敵キャラクターの位置情報
    gy,gx:プレイヤーの位置情報
----------------------------------------------------------------------------------------------------
"""

#存在する座標を列挙したリスト
stage_grid = []
for i in range(len(stage_inf)): #iは列（ｙ座標）
    for j in range(len(stage_inf[i])): #ｊは行（ｘ座標）
        stage_grid.append([i,j])

#未探索の通路をエンキューする関数
"""
gridの範囲内か否かを判定
道か否か判定
探索済みか否かを判定
どちらとも満たせばエンキュー
    →visitedに（親の距離＋１）を追加
"""


def enque(y,x,plus_y,plus_x):  
    global que
    global visited
    pa_depth = visited[y][x]
    #pa_grid_ num = [y,x]
    y = y + plus_y
    x = x + plus_x
    if [y,x] in stage_grid:
    #if y < 0 or R-1 < y or x < 0 or C-1 < x:
        return #print(1)
    elif visited[y][x] == "#":
        return #print(2)
    elif type(visited[y][x]) is int:
        return #print(3)
    else:
        que.append([y,x])
        visited[y][x] = pa_depth + 1
        return #print(4)

#初期化
from collections import deque

que = deque()
visited = stage_inf.copy()
goal = [gy,gx]

#手順１
"""最初の座標をエンキューする"""

que.append([sy,sx])
visited[sy][sx] = 0

#手順２
"""
queが空になるまでくりかえす（今回は目的のノードがあるのでそれを探索したら終了する）
    デキューをする
        →それが gy gx ならば探索終了
        →そうでなければ
            →探索済みなら無視
            →探索済みでなければ周囲の座標をエンキュー
"""

while que:
    #print(que)
    grid_num = que.popleft()
    if grid_num == goal:
        break
    else:
        enque(grid_num[0],grid_num[1],1,0)
        enque(grid_num[0],grid_num[1],0,1)
        enque(grid_num[0],grid_num[1],-1,0)
        enque(grid_num[0],grid_num[1],0,-1)

#情報の表示
"""
for i in range(R):
    print("  ".join(map(str,visited[i])))
"""

#print("最短距離は" + str(visited[gy][gx]))
print(visited[gy][gx])
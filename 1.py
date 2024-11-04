
# 創建一個 10x10 的二維陣列，所有元素初始化為 0
map = [[0 for _ in range(10)] for _ in range(10)]

# 輸出結果以確認
for row in map:
    print(row)
    
    # 創建一個大小為 10 的一維陣列，所有元素初始化為 0
rowMap = [0 for _ in range(10)]

# 輸出結果以確認
print(rowMap)

# 創建一個大小為 10 的一維陣列
rowMap = [0] * 10

# 將 rowMap 賦值
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 輸出結果以確認
print(rowMap)

# 創建一個 10x10 的二維陣列，所有元素初始化為 0
map = [[0 for _ in range(10)] for _ in range(10)]

# 將 rowMap 賦值
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 將炸彈標記為 '*'
for value in rowMap:
    row = value // 10  # 計算行索引
    col = value % 10   # 計算列索引
    map[row][col] = '*'  # 在對應位置標記炸彈

# 輸出二維陣列
for row in map:
    print(' '.join(str(elem) for elem in row))


# 創建一個 10x10 的二維陣列，所有元素初始化為 0
map = [[0 for _ in range(10)] for _ in range(10)]

# 將 rowMap 賦值
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 將炸彈標記為 '*'
for value in rowMap:
    row = value // 10  # 計算行索引
    col = value % 10   # 計算列索引
    map[row][col] = '*'  # 在對應位置標記炸彈

# 創建一個結果陣列以存儲炸彈周圍的數量
result_map = [[0 for _ in range(10)] for _ in range(10)]

# 定義八個相鄰格子的相對位置
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

# 計算每個格子周圍的炸彈數量
for row in range(10):
    for col in range(10):
        if map[row][col] == '*':
            # 炸彈格子，將周圍的格子數量加一
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < 10 and 0 <= c < 10:
                    if result_map[r][c] != '*':
                        result_map[r][c] += 1

# 將炸彈位置設置為 '*'
for value in rowMap:
    row = value // 10
    col = value % 10
    result_map[row][col] = '*'

# 輸出結果陣列
for row in result_map:
    print(' '.join(str(elem) if elem != 0 else ' ' for elem in row))


# 期中考
>
>學號：112111206
><br />
>姓名：李儲亮
><br />
>作業撰寫時間：180 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2024/11/04
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)

a. 小題

Ans
```py
# 創建一個 10x10 的二維陣列，所有元素初始化為 0
map = [[0 for _ in range(10)] for _ in range(10)]

# 輸出結果以確認
for row in map:
    print(row)
```

b. 小題

Ans
```py
# 創建一個大小為 10 的一維陣列，所有元素初始化為 0
rowMap = [0 for _ in range(10)]

# 輸出結果以確認
print(rowMap)
```

c. 小題

Ans
```py
# 創建一個大小為 10 的一維陣列
rowMap = [0] * 10

# 將 rowMap 賦值
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 輸出結果以確認
print(rowMap)
```

d. 小題

Ans
```py
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
```


e. 小題

Ans
```py
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
```
```py
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
```
# Python备忘录

## 循环

### level1： 遍历每个元素
```python
colors = ["red", "green", "blue", "purple"]

for i in range(len(colors)):
    print(colors[i])
```

output:
```python
red
green
blue
purple
```

<br>

### 遍历每个元素+位置（range）

```python
colors = ["red", "green", "blue", "purple"]

for i in range(len(colors)):
    print(f"{i+1}: {colors[i]}")
```

output:
```python
1: red
2: green
3: blue
4: purple
```

<br>


### 遍历每个元素+位置（枚举）

```python
colors = ["red", "green", "blue", "purple"]

for i, name in enumerate(colors, start=1):
    print(f"{i}: {name}")
```

output:
```python
1: red
2: green
3: blue
4: purple
```

<br>


### 遍历每个元素+位置（枚举）+ 格式化输出

```python
colors = ["red", "green", "blue", "purple"]

for i, name in enumerate(colors, start=1):
    print(f"{'%02d'%i}: {name}")
```

output:
```python
01: red
02: green
03: blue
04: purple
```

<br>


### 列表表达式

```python
colors = ["red", "green", "blue", "purple"]

print([c for c in colors])
```

output:
```python
['red', 'green', 'blue', 'purple']
```

### 列表表达式+过滤

```python
colors = ["Pink", "Dark red", "Light red", "Tomato"]

print([c for c in colors if 'red' in c])
```

output:
```python
['Dark red', 'Light red']
```

### 列表表达式+判断

```python
colors = ["Pink", "Dark red", "Light red", "Tomato"]

print(['red' in c for c in colors])
```

output:
```python
[False, True, True, False]
```

### 列表表达式+格式化输出

```python
colors = ["red", "green", "blue", "purple"]

print([f"({c})" for c in colors])
```

output:
```python
['(red)', '(green)', '(blue)', '(purple)']
```

### 列表表达式+字符串拼接

```python
colors = ["red", "green", "blue", "purple"]

print(["_".join(c) for c in colors])
```

output:
```python
['r_e_d', 'g_r_e_e_n', 'b_l_u_e', 'p_u_r_p_l_e']
```

<br>


### 组合2个list(zip)

```python
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for color, ratio in zip(colors, ratios):
    print(f"{ratio * 100}% {color}")
```

output:
```python
20.0% red
30.0% green
10.0% blue
40.0% purple
```

<br>


### 组合2个list(列表表达式)

```python
number = [1, 2, 3, 4]
colors = ["red", "green", "blue", "purple"]

print([(i, c) for i in number for c in colors])
```

output:
```python
[
    (1, 'red'), (1, 'green'), (1, 'blue'), (1, 'purple'), 
    (2, 'red'), (2, 'green'), (2, 'blue'), (2, 'purple'), 
    (3, 'red'), (3, 'green'), (3, 'blue'), (3, 'purple'), 
    (4, 'red'), (4, 'green'), (4, 'blue'), (4, 'purple')
]
```

Case 2: 条件过滤

```python
number = [1, 2, 3, 4]
colors = ["red", "green", "pink", "purple"]

print([(i, c) for i in number for c in colors if c[0] == "p"])
```

output:
```python
[   
    (1, 'pink'), (1, 'purple'), 
    (2, 'pink'), (2, 'purple'), 
    (3, 'pink'), (3, 'purple'), 
    (4, 'pink'), (4, 'purple')
 ]
```

Case 3: 多个条件

```python
number = [1, 2, 3, 4]
colors = ["red", "green", "pink", "purple"]

print([(i, c) for i in number for c in colors if c[0] == "p" if i>3])
```

output:
```python
[
    (4, 'pink'), (4, 'purple')
]
```

Case 4: 多个条件

```python
number = [1, 2, 3, 4]
colors = ["red", "green", "pink", "purple"]

print([i for i in zip(number, colors) if i[0]>3])
```

output:
```python
[
    [(2, 'green'), (4, 'purple')
]
```


### 合并多个list到dict

```python
a = ["red", "green", "blue", "purple"]
b = ["A", "B", "C", "D"]
c = [1, 2, 3, 4]

[
    {'name': name, 'color': color, 'number': number}
    for name, color, number in zip(a, b, c)
]
```

ouput:
```python
[
    {'name': 1, 'color': 'a', 'number': '一'},
    {'name': 2, 'color': 'b', 'number': '二'}, 
    {'name': 3, 'color': 'c', 'number': '三'}
]
```

<br>


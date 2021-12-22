# Python备忘录


## for..in


### Case 1
```python
colors = ["red", "green", "blue", "purple"]

for i in range(len(colors)):
    print(colors[i])
```

output:
```
red
green
blue
purple
```

### Case 2

```python
colors = ["red", "green", "blue", "purple"]

for i in range(len(colors)):
    print(f"{i+1}: {colors[i]}")
```

output:
```
1: red
2: green
3: blue
4: purple
```

### Case 3

```python
colors = ["red", "green", "blue", "purple"]

for i, name in enumerate(colors, start=1):
    print(f"{i}: {name}")
```

output:
```
1: red
2: green
3: blue
4: purple
```

### Case 4

```python
colors = ["red", "green", "blue", "purple"]

for i, name in enumerate(colors, start=1):
    print(f"{'%02d'%i}: {name}")
```

output:
```
01: red
02: green
03: blue
04: purple
```

### Case 5

```python
colors = ["red", "green", "blue", "purple"]
ratios = [0.2, 0.3, 0.1, 0.4]

for color, ratio in zip(colors, ratios):
    print(f"{ratio * 100}% {color}")
```

output:
```
20.0% red
30.0% green
10.0% blue
40.0% purple
```


### Case 6

```python
colors = ["red", "green", "blue", "purple"]

print(["_".join(c) for c in colors])
```

output:
```
['r_e_d', 'g_r_e_e_n', 'b_l_u_e', 'p_u_r_p_l_e']
```


### Case 7

```python
colors = ["red", "green", "blue", "purple"]

print([f"({c})" for c in colors])
```

output:
```
['(red)', '(green)', '(blue)', '(purple)']
```




# 正则表达式备忘录

## key=
```
\w+=
```

case:
```
abc=helloworld
```

---

## style="" 
```
style="[\s\S]*?"
```

## <img ...>
``` 
<img (.*?)>
```

## <div ...></div> 
```
<div[^>]*>(.*?)<\/div>$
```

case:
```
<div>I would like <b>all</b> the text!</div>
<div class="behavior" src="https://www.behavior/image.svg"><div class="text"><p>Bullet<p></div></div>
<div><p>Hello</p></div>
<div><div>Hello<div></div>
<div class="behavior" src="https://www.behavior/image.svg">Hello</div>
```

---

# <>
```
<([^><]+)>
```

## {} 
```
\{.+?\}
```

case(javascript):
```javascript
'{aaaa} {bbb} {50}'.match(/\{.+?\}/g).map(e=>e.slice(1,-1))
```

```javascript
'{aaaa} {bbb} {50}'.match(/\{[\w\d<>=]+\}/g).map(e=>e.slice(1,-1))
```

---

## #
```
\#[^\n]*
```

## //
```
//[\s\S]*?\n
```

## // (without: http://)
```
//(?!.*\..*\.).*\n
```
 
## /* ... */
```
/\*(.|\r\n|\n)*?\*/
```

## // & /*  */
```
/\*(.|\r\n|\n)*?\*/
```

## <-- ... -->
```
<!--(.*?)-->
```

## <-- /n --> (包含换行)
```
<!--([\s\S|\r]*?)-->
```

---

# newline
```
^\s*\n
```

case2:
```
str.split(/[\s\n]/)
```

case2: 
```
function heredoc(fn) {
    return fn.toString().split('\n').slice(1,-1).join('\n') + '\n'
}

var str = heredoc(function(){/*

这年头

居然还存在这种

奇怪的空格
*/});


// (7) ["", "这年头", "", "居然还存在这种", "", "奇怪的空格", ""]
```

---

## 手机号 
```
r'(\d{3})(-)?(\d{4})(-)?(\d{4})'
```

```
^1[3|4|5|7|8][0-9]{9}$
```

```
r'1\d{10}'
```


## 家庭住址
```
(?<省>[^省]+自治区|.*?省|.*?行政区|.*?市)
(?<市>[^市]+自治州|.*?地区|.*?行政单位|.+盟|市辖区|.*?市|.*?县)
(?<区>[^县]+县|.+区|.+市|.+旗|.+海域|.+岛)?
(?<街道>[^区]+区|.+镇|.+街道办事处|.+街道)?
(?<详细地址>.*)
```

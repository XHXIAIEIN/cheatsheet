# 正则表达式备忘录


## (...)

```
(?<=\()\S+(?=\))
```

- `(?<=exp)` 以 exp 开头的字符串, 但不包含 exp。  
- `(?=exp)` 以 exp 结尾的字符串, 但不包含 exp。  
- `(?<=\()` 以 `(` 开头, 但不包含 `(` 。  
- `(?=\))` 以 `(` 结尾, 但不包含 `)`。  
- `\S` 匹配任何非空白字符，等价于 `[\^\f\n\r\t\v]`。
- `\S+` 表示至少有一个字符。

`(?<=\()\S+(?=\))` 就是匹配以 `(` 开头，以 `)` 结尾，里面最少有一个非空白的字符串, 但不包含首尾的括号。

  
## {if condition ? True : False}

区分 `variable`, `"String"`, `123` 不同的类型
```
\{if?\s+?(?<condition>(\w+)\s*?([<>!=]+)?\s*?(\d+|\w+|[?<="].*?[?="]))\s*?\?[\s]*?(?<True>\d+|\w+|[?<="].*?[?="])[\s*]?[\:]?[\s*]?(?<False>\d+|\w+|[\"].*?[\"])?
```

```
Hi, {if gold >= 0 ?  "Rich   Man" : "Guy"}. You have {gold} coin. Do you want to buy some {fruit}?

Hi, {if gold >= "12312 32112" ?  nam1 : name2}. You have {gold} coin. Do you want to buy some {fruit}?

Hi, {if gold >= coin ?  nam1 : name2}. You have {gold} coin. Do you want to buy some {fruit}?

Hi, {if gold >= coin ?  nam1}. You have {gold} coin. Do you want to buy some {fruit}?

Hi, {if gold >= 0 ?"Rich   Man"}. You have {gold} coin. Do you want to buy some {fruit}?

Hi, {if gold>=0?1}. You have {gold} coin. Do you want to buy some {fruit}?

Hi, {if gold >= 2 ? 123 : 0}. You have {gold} coin. Do you want to buy some {fruit}?
```


## key=
```
\w+=
```

case:
```
abc=helloworld
```

---

## [tag]
```
/\[([^\]]*)\]/
```

case:
```
const line = [tag]
const tag = line.match(/\[([^\]]*)\]/)[1].trim();
```


## [This is a choice.](#text)

```
/\(#(.+?)\)/
```

```
/\(\#(.*)\)/
```

```
/\[([^\]]+)\]\(#([^)]+)\)/
```

```
const str = '[continue](#next)'
const re = /\(#(.+?)\)/

str.match(re)
```

case:
```
const line = [tag]
const tag = line.match(/\[([^\]]*)\]/)[1].trim();
```

---

## (str)
```
/\(\#([^\)]*)\)/
```

```
const line = (tag)
const str = line.match(/\(\#([^\)]*)\)/).trim();
```

---


## name:str
```
/^([^\:]+)\:(.*)/
```

case:
```
const line = "name : Hello World !"
const regex = /^([^\:]+)\:(.*)/
const speaker = line.match(regex)[1].trim();
const dialogue = line.match(regex)[2].trim();
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

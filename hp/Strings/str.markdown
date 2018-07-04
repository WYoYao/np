# class str

[参考链接](https://segmentfault.com/a/1190000004598007)
[参考链接](http://www.runoob.com/python/att-string-strip.html)

> class str(object)
>    str(object='') -> str
>    传入空值直接返回长度为0的字符串

```
str(bytes_or_buffer[, encoding[, errors]]) -> str
```

>  从给定对象创建一个新的字符串对象。 如果编码或
>  错误被指定，那么对象必须公开一个数据缓冲区
>  将使用给定的编码和错误处理程序进行解码。
>  否则，返回对象.__ str __（）的结果（如果已定义）
>  或repr（对象）。
>  编码默认为sys.getdefaultencoding（）。
>  错误默认为“严格”。
>  print(str("测试".encode("utf8"), "utf8"))

>  capitalize(...)
>      S.capitalize() -> str
>  首字母大写

>  casefold(...)
>      S.casefold() -> str
>  转换成为小写
>  lower() 只对 ASCII 也就是 'A-Z'有效，但是其它一些语言里面存在小写的情况就没办法了。文档里面举得例子是德语中'ß'的小写是'ss'：
>  s = 'ß'
>  print(s.lower())  # 'ß'
>  print(s.casefold())  # 'ss'

>  center(...)
>      S.center(width[, fillchar]) -> str
>  通过向 str 的前后填充 fillchar 到指定 width 长度
>  使用指定的填充字符完成（默认为空格）
>  print("1234".center(1, "5"))  # 长度小于当前长度时不做处理
>  print("1234".center(5, "5"))  # 如果目标长度与原有长度的差值为奇数,左侧比右侧多分配一个填充char
>  print("1234".center(6, "5"))  # 如果目标长度与原有长度的差值为偶数,左侧比右侧多分配相同数量的char

>
>  count(...)
>      S.count(sub[, start[, end]]) -> int
>      count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
>  print("123123a1b23c123123".count("123", 3, -1))
>

>  encode(...)
>      S.encode(encoding='utf-8', errors='strict') -> bytes
>      Python decode() 方法以 encoding 指定的编码格式解码字符串。默认编码为字符串编码。
>  errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个            UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace',        'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
>  print("测试".encode('utf8','ignore').decode('utf8'))

>  endswith(...)
>      S.endswith(suffix[, start[, end]]) -> bool
>      Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。
>  可选参数"start"与"end"为检索字符串的开始与结束位置。

```
print("123456789".endswith("789"))
# True
print("123456789".endswith(("123", "789")))
# True
```


>
>  expandtabs(...)
>      S.expandtabs(tabsize=8) -> str
>      Python expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。

```
# str.expandtabs(n) 跟踪每行上的当前光标位置，并将其找到的每个制表符字符替换为当前光标位置到下一个制表位的空格数。
# str.expandtabs(n) 不等于 str.replace("\t", " " * n)

def expandtabs(string, n=8):
    result = ""
    pos = 0
    for char in string:
        if char == "\t":
            # instead of the tab character, append the
            # number of spaces to the next tab stop
            char = " " * (n - pos % n)
        if char == "\n":
            pos = 0
        else:
            pos += len(char)
        result += char
    return result
```

>  find(...)
>      S.find(sub[, start[, end]]) -> int
>      Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
>
>      Return - 1 on failure.


>  format(...)
>      S.format(*args, **kwargs) -> str
>  格式化函数

```
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
```

>  format_map(...)
>      S.format_map(mapping) -> str
>      类似 str.format(*args, **kwargs) ，不同的是 mapping 是一个字典对象。

```
People = {'name': 'john', 'age': 56}

print('My name is {name},i am {age} old'.format_map(People))
# 'My name is john,i am 56 old'
```

>  index(...)
>      S.index(sub[, start[, end]]) -> int
>  与 find() rfind() 类似，不同的是如果找不到，就会引发 ValueError。

```
print("123456789".find("345"))
# 2
print("123456789".find("543"))
# -1
print("123456789".index("345"))
# 2
print("123456789".index("543"))
# ValueError
```

>  isalnum(...)
>      S.isalnum() -> bool
>
>      字符串和数字的任意组合，即为真，简而言之：
>      只要 c.isalpha(), c.isdecimal(), c.isdigit(), c.isnumeric() 中任意一个为真，则 c.isalnum() 为真。

```
print('dobi'.isalnum())
# True

print('dobi123'.isalnum())
# True

print('123'.isalnum())
# True

print('徐'.isalnum())
# True

print('dobi_123'.isalnum())
# False

print('dobi 123'.isalnum())
# False

print('%'.isalnum())
# False

```

>  isalpha(...)
>      S.isalpha() -> bool
>
>      Return True if all characters in S are alphabetic
> and there is at least one character in S, False otherwise.
>
>  isdecimal(...)
>      S.isdecimal() -> bool
>
>      Return True if there are only decimal characters in S,
>      False otherwise.
>
>  isdigit(...)
>      S.isdigit() -> bool
>
>      Return True if all characters in S are digits
> and there is at least one character in S, False otherwise.
>
>  isidentifier(...)
>      S.isidentifier() -> bool
>
>      判断字符串是否可为合法的标识符。

```
print('def'.isidentifier())
# True

print('with'.isidentifier())
# True

print('false'.isidentifier())
# True

print('dobi_123'.isidentifier())
# True

print('dobi 123'.isidentifier())
# False

print('123'.isidentifier())
# False
```

>  islower(...)
>      S.islower() -> bool
>      判断字符串中的字母是否全部是小写
>
>  isnumeric(...)
>      S.isnumeric() -> bool
>
>      Return True if there are only numeric characters in S,
>      False otherwise.
>
>  isprintable(...)
>      S.isprintable() -> bool
>
>      Return True if all characters in S are considered
>      printable in repr() or S is empty, False otherwise.
>
>  isspace(...)
>      S.isspace() -> bool
>
>      判断字符串中是否至少有一个字符，并且所有字符都是空白字符。

```
print('\r\n\t'.isspace())
# True
print(''.isspace())
# False
print(' '.isspace())
# True
```

>  istitle(...)
>      S.istitle() -> bool
>
>      判断字符串中的字符是否是首字母大写，其会忽视非字母字符。(字母中的每个字符的单词)

```
print('How Python Works'.istitle())
# True

print('How Python WORKS'.istitle())
# False

print('how python works'.istitle())
# False

print('How Python  Works'.istitle())
# True

print(' '.istitle())
# False

print(''.istitle())
# False

print('A'.istitle())
# True

print('a'.istitle())
# False

print('甩甩Abc Def 123'.istitle())
# True
```

>  isupper(...)
>      S.isupper() -> bool
>
>      字符串中所有的字符都是大写

```
'徐'.isupper()
# False

'DOBI'.isupper()
# True

'Dobi'.isupper()
# False

'DOBI123'.isupper()
# True

'DOBI 123'.isupper()
# True

'DOBI\t 123'.isupper()
# True

'DOBI_123'.isupper()
# True

'_123'.isupper()
# False
```

>  join(...)
>      S.join(iterable) -> str
>
>       join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

```
```


>
>  ljust(...)
>      S.ljust(width[, fillchar]) -> str
>
>      返回指定长度的字符串，字符串内容居左（右）如果长度小于字符串长度，则返回原始字符串，默认填充为 ASCII 空格，可指定填充的字符串。

```
print('dobi'.ljust(10))
# 'dobi      '

print('dobi'.ljust(10, '~'))
# 'dobi~~~~~~'

print('dobi'.ljust(3, '~'))
# 'dobi'

print('dobi'.ljust(3))
# 'dobi'

print('dobi'.rjust(10))
# 'dobi      '

print('dobi'.rjust(10, '~'))
# 'dobi~~~~~~'

print('dobi'.rjust(3, '~'))
# 'dobi'

print('dobi'.rjust(3))
# 'dobi'

```

>
>  lower(...)
>      S.lower() -> str
>
>      将字符串转换成小写，其仅对 ASCII 编码的字母有效。

```
print('DOBI'.lower())
# 'dobi'

print('ß'.lower())   # 'ß' 为德语小写字母，其有另一种小写 'ss'， lower 方法无法转换
# 'ß'

print('徐 ABCD'.lower())
# '徐 abcd'

```


>  lstrip(...)
>      S.lstrip([chars]) -> str
>
>      返回删除前导空白字符串S的副本。
>      如果给出了chars而不是None，则删除chars中的字符。

```
print('  dobi'.lstrip())
# 'dobi'
print('db.kun.ac.cn'.lstrip('dbk'))
# '.kun.ac.cn'
print(' dobi   '.rstrip())
# ' dobi'
print('db.kun.ac.cn'.rstrip('acn'))
# 'db.kun.ac.'
print('   dobi   '.strip())
# 'dobi'
print('db.kun.ac.cn'.strip('db.c'))
# 'kun.ac.cn'
print('db.kun.ac.cn'.strip('cbd.un'))
# 'kun.a'
```

>  partition(...)>  partition(...)
>      S.partition(sep) -> (head, sep, tail)
>
>      partition() 方法用来根据指定的分隔符将字符串进行分割。
>      如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

```
print("hello World Everyone".partition("World"))
# ('hello ', 'World', ' Everyone')
print("hello World World Everyone".partition("World"))
# ('hello ', 'World', ' World Everyone')
```

>  replace(...)
>      S.replace(old, new[, count]) -> str
>
>      Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

```
print("123123123".replace("3", "34"))
# 123412341234

print("123123123".replace("3", "34", 2))
# 12341234123

print("123123123".replace("3", "34", 10))
# 123412341234
```

>  rfind(...)
>      S.rfind(sub[, start[, end]]) -> int
>
>      Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。

>  rindex(...)
>      S.rindex(sub[, start[, end]]) -> int
>
>      Python rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。

>  rjust(...)
>      S.rjust(width[, fillchar]) -> str
>
>      Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。

>  rpartition(...)
>      S.rpartition(sep) -> (head, sep, tail)
>
>      rpartition() 方法类似于 partition() 方法，只是该方法是从目标字符串的末尾也就是右边开始搜索分割符。。

如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

>  rsplit(...)
>      S.rsplit(sep=None, maxsplit=-1) -> list of strings
>
>      Return a list of the words in S, using sep as the
>      delimiter string, starting at the end of the string and
>      working to the front.  If maxsplit is given, at most maxsplit
>      splits are done. If sep is not specified, any whitespace string
> is a separator.
>
>  rstrip(...)
>      S.rstrip([chars]) -> str
>
>      Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.

```
s = "     this is string example....wow!!!     "
print(s.rstrip())
#     this is string example....wow!!!
s = "88888888this is string example....wow!!!8888888"
print(s.rstrip('8'))
# 88888888this is string example....wow!!!
```

>
>  split(...)
>      S.split(sep=None, maxsplit=-1) -> list of strings
>
>      Python split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串

```
s = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(s.split())
print(s.split(' ', 1))
```

>
>  splitlines(...)
>      S.splitlines([keepends]) -> list of strings
>
>      Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

```
s1 = 'ab c\n\nde fg\rkl\r\n'
print(s1.splitlines())

s2 = 'ab c\n\nde fg\rkl\r\n'
print(s2.splitlines(True))

```

>
>  startswith(...)
>      S.startswith(prefix[, start[, end]]) -> bool
>
>      Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

```
s = "Hello World"

print(s.startswith("Hello", 0, len(s)))
# True
```

>
>  strip(...)
>      S.strip([chars]) -> str
>
>      Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

```
s = "00000003210Runoob01230000000"
print(s.strip('0'))  # 去除首尾字符 0
# 3210Runoob0123

s2 = "   Runoob      "   # 去除首尾空格
print(s2.strip())
# Runoob
```

>  swapcase(...)
>      S.swapcase() -> str
>   Python swapcase() 方法用于对字符串的大小写字母进行转换。

```
s = "hello WORLD"

print(s.swapcase())
# HELLO world
```

>  title(...)
>      S.title() -> str
>
>      Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。

```
s = "this is string example....wow!!!"
print(s.title())
# This Is String Example....Wow!!!
```

>  translate(...)
>      S.translate(table) -> str
>
>       Python maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式， 
第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 
注：两个字符串的长度必须相同，为一一对应的关系。 

```
intab = "abcde"
outtab = "12345"
# a=>1 b=>2 c=>3 d=>4 e=>5
trantab = str.maketrans(intab, outtab)

s = "edcbaabcde"
print(s.translate(trantab))
```

>  upper(...)
>      S.upper() -> str
>
>      返回小写字母转为大写字母的字符串。

```
str = "this is string example....wow!!!"

print(str.upper())
```

>  zfill(...)
>      S.zfill(width) -> str
>
>      指定字符串的长度。原字符串右对齐，前面填充0。

```
str = "this is string example....wow!!!"

print(str.zfill(40))
# 00000000this is string example....wow!!!
print(str.zfill(50))
# 000000000000000000this is string example....wow!!!
```


> ----------------------------------------------------------------------
>  Static methods defined here:
>
>  maketrans(x, y=None, z=None, /)
>      Return a translation table usable for str.translate().
>
>      If there is only one argument, it must be a dictionary mapping Unicode
>      ordinals(integers) or characters to Unicode ordinals, strings or None.
>      Character keys will be then converted to ordinals.
>      If there are two arguments, they must be strings of equal length, and
> in the resulting dictionary, each character in x will be mapped to the
>      character at the same position in y. If there is a third argument, it
>      must be a string, whose characters will be mapped to None in the result.

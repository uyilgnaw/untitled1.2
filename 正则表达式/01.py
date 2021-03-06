# 如使用r在字符串前缀，就不需要进行转义。

import re

# Python的字符串
s = 'ABC\\-001'
print(s)
s = r'ABC\001'
print(s)

r = re.match(r'\.\d{3}-\d{3,8}$','.010-123456')
print(r)
'''
match() 方法判断是否匹配，如果匹配成功，返回一个match对象，否则返回None。
常见的判断方法为：
    test = '用户输入的字符串'
    if re.match(r'正则表达式',test):
        print('ok')
    else:
        print('failed')
        
'''
# 使用正则表达式切分字符串比用固定的字符串更加灵活，例如：
s = 'a b  c'

print(s.split(' '))
# 无法识别连续的空格，以及会返回空格
print(re.split(r'\s+',s))
# 使用re.split方法，无论多少个空格都可以正常分割。

print(re.split(r'[\s,;]+',r'a,b c;;de'))
# []表示范围，括号中的都包括在内如果出现至少一次的话就会进行匹配
# 如果用户输入了一组不规范的标签，就可以用上面的正则表达式来进行处理


'''
分组：
    - 除了简单的是否匹配外，正则表达式提取子串的功能，用（）表示的就是要提取的分组（Group）。例如：
        - ^(\d{3})-(\d{3-8})$ 分别定义了两个组，可以直接从匹配的字符串中提取出括号中的两端字符串
                
'''

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)
# 返回的代表匹配成功
print(m.group(0))
# group(0) 代表将匹配到的所有字符串打印出来
print(m.group(1))
# group(1) 代表将表达式的第一个括号中的字符串打印出来
print(m.group(2))
# group(2) 同理
'''
如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
注意到group(0) 永远是原始字符串

'''
t = '19:04:32'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# 这个正则表达式可以直接识别合法的时间。
print(m.groups())
'''
贪婪匹配
    - 正则匹配默认是进行贪婪匹配，也就是匹配尽可能多的字符。
    - 下面的例子由于前面\d+采用了贪婪匹配，直接将后面的0全部都匹配了进去，结果0*只有匹配空字符串了
    - 所以要将\d+采用非贪婪匹配，加？
'''
# 贪婪匹配
print(re.match(r'^(\d+)(0*)$','1023000').groups())
# 非贪婪匹配
print(re.match(r'^(\d+?)(0*)$','102000').groups())



# -*- coding: utf-8 -*-

#1
dss='  hello pyqt5,,'
print('\n#1,去除空格及特殊符號')
s1=dss.strip().lstrip().rstrip(',')
print('s1,',s1)

#2
print('\n#2,字串連接')
s2=dss.join(['a','.','c'])
print('s2,',s2)
s3='s3'
s3+='xx'
print('s3,',s3)

#3
print('\n#3,查找字元')
css='abc1c2c3'
pi=css.find('c')
print('pi,',pi)

#4,字串比較
print('\n#4,字串比較')
print( s1 > s2 )  
print( s1 == s2 )  
print( s1 < s2 )  

#5
print('\n#5,字串長度')
s1,s2='abc','c123'
print('len(s1),',len(s1))
print('len(s2),',len(s2))

#6
print('\n#6,大小寫轉換')
s1,s2='abc','ABC123efg'
print('大寫，s1.upper(),',s1.upper())
print('小寫，s2.lower(),',s2.lower())
print('大小寫互換 ,s2.swapcase(),',s2.swapcase())
print('首字母大寫 ,s1.capitalize(),',s1.capitalize())

#7
print('\n#7,分割字串')
s2='  hello, ziwang,com,,'
print('s2.split,',s2.split(','))


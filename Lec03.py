# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第三讲：循环一般样式
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

###求某完全平方数的平方根
##x = 16
##ans = 0
##while ans*ans < x:
##    ans = ans + 1
##print ans


##if (x/2)*2 == x:
##    print '偶'
##else :
##    print '奇'


##x = 1515361
##ans = 0
##if x >= 0:
##    while ans*ans < x:
##        ans = ans +1
##        #print 'ans = ',ans
##    if ans*ans != x:
##        print x,' 不是完全平方数'
##    else: print ans
##else: print x,' 是负数'


##x = 10
##i = 1
##while i<x:
##    if x%i == 0:
##        print '约数',i
##    i= i+1
##

##x = 10
##for i in range(1,x):
##    if x%i == 0:
##        print '约数',i

##x = 1515361
##if x>= 0:
##    for ans in range(1,x):
##        if ans*ans == x:
##            print ans
##            break

##
##x = 100
##divisors = ( )
### 这里讲义上误作[ ]，此更正（圆括号表示元组tuple、方括号表示列表list）
### divisors：约数
##for i in range(1, x):
##    if x%i == 0:
##        divisors = divisors + (i, )
##print divisors

        
s1 = 'abcdefg'
s2 = 'hijklmn'

print s1 + s2
##
##print s1
##print s1[0]
##print s1[3]
##print s1[-1]
##
##print s1[2:4]
##print s1[:3]
##print s1[3:]


print s1.find('cde')

print s1 == s1
print s1 == s2
print s1 < s2
print s1 > s2

##
##sumDigits = 0
##for c in str(1952):
##    sumDigits += int(c)
##print sumDigits

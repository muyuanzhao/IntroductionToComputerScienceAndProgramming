# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第二讲：分支、条件和循环
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

##x = 3 # 创建变量x，并赋值为3
##x=x*x # 赋值9给x
##print x
##n = raw_input('输入一个数字：')
##print n
### print n/n
##
##x = input('输入一个数字：')
##if not x%2:
####    print '偶数'
##else: print '奇数'

##x = 15
##if (x/2)*2 == x: print '偶数'
##else: print '奇数'
##
##z = 'b'
####if 'x'<z:
####    print 'Hello'
####    print 'Mom'
##if 'x'<z:
##    print 'Hello'
##print 'Mom'
##
##x = 15
##y = 13
##z = 11
##print x,y,z
### 这里正确吗？
####if x < y:
####    if x < z: print 'x最小'
####    else: print 'z最小'
####else: print 'y最小'
##
##if x<y and x<z: print 'x最小'
##elif y<z: print 'y最小'
##else: print 'z最小'

##y = 0
##x = 3
##itersLeft = x
##while(itersLeft>0):
##    y = y + x
##    itersLeft = itersLeft - 1
##    print 'y=',y,',itersLeft',itersLeft
##print y

##x = 10
##i = 1
##while(i<x):
##    if x%i == 0:
##        print '约数',i
##    i = i+1

x = 10
for i in range(1,x):
    if x%i == 0:
        print '约数',i
    

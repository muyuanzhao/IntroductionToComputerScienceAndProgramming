# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第十二讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def fib(n):
    global numCalls
    numCalls +=1
    print 'fib调用', n
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
numCalls = 0
##fib(5)

n = 10
print 'fib_', n, '=', fib(n)
print '调用次数为', numCalls
    
            

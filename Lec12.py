# MIT600���������ѧ����̵��ۡ���2008���＾������
# ��ʮ����
# ����������ocourse.org
# �γ����۰棺http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def fib(n):
    global numCalls
    numCalls +=1
    print 'fib����', n
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
numCalls = 0
##fib(5)

n = 10
print 'fib_', n, '=', fib(n)
print '���ô���Ϊ', numCalls
    
            

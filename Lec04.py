# MIT600���������ѧ����̵��ۡ���2008���＾������
# ���Ľ����������󼰵ݹ����
# ����������ocourse.org
# �γ����۰棺http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

##x = 16
##ans = 0
##if x >= 0:
##    while ans*ans < x:
##        ans = ans +1
##        #print 'ans = ',ans
##    if ans*ans != x:
##        print x,' ������ȫƽ����'
##    else: print ans
##else: print x,' �Ǹ���'

def sqrt(x):
    """Returns the square root of x, if x is a perfect square.
        Prints an error message and returns None otherwise"""
    #hello���x����ȫƽ����������x��ƽ�����������ӡ������Ϣ�����޷���ֵ
    ans = 0  
    if x>= 0:
        while ans*ans < x: ans = ans + 1
        if ans*ans != x:
            print x, ' ������ȫƽ����'
            return None  
        else: return ans
    else:
        print x, ' �Ǹ���'
        return None


def f(x):
    x = x + 1
    return x

##x = 3
##z = f(x)
##print x
##print z

##ans = 15
##sqrt(25)
##ans

def solve(numLegs, numHeads):
    #solve�⣬num��ʾnumber����Ŀ����tot��ʾtotal����������leg�š�headͷ��pig��chick��
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs:
            return (numPigs, numChicks)
    return None

def barnYard():
    #barnyardũ��
    heads = int(raw_input('����ͷ�ĸ�����'))
    legs = int(raw_input('����ŵĸ�����'))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print '�޽�'
    else:
        print '�����Ŀ�ǣ�', pigs
        print '������Ŀ�ǣ�', chickens

def solve1(numLegs, numHeads):
    #spider֩��
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs =4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                return [numPigs, numChicks, numSpiders]
    return [None, None, None]

def barnYard1():
    heads = int(raw_input('����ͷ�ĸ�����'))
    legs = int(raw_input('����ŵĸ�����'))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs == None:
        print '�޽�'
    else:
        print '�����Ŀ�ǣ�', pigs
        print '������Ŀ�ǣ�', chickens
        print '֩�����Ŀ�ǣ�', spiders

def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs =4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                print '�����Ŀ�ǣ�' + str(numPigs) + ',',
                print '������Ŀ�ǣ�' + str(numChicks) + ',',
                print '֩�����Ŀ�ǣ�', numSpiders
                solutionFound = True
    if not solutionFound: print '�޽�'

###test function barnYard2 for solve2 added by ocourse.org
###ͷ��Ŀ10������Ŀ30���Եõ�������
def barnYard2():
    heads = int(raw_input('����ͷ�ĸ�����'))
    legs = int(raw_input('����ŵĸ�����'))
    solve2(legs, heads)

def isPalindrome(s):
    """Return True if s is a palindrome and False otherwise"""
    #����ǻ��ģ�palindrome��������True�����򷵻�False
    if len(s) <=1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])
   
def isPalindrome1(s, indent):
    """Return True if s is a palindrome and False otherwise"""
    #indent ����
    print indent*' ', 'isPalindrome1����', s
    if len(s) <= 1:
        print indent*' ', '׼���ӻ����������True'
        return True
    else:
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent + indent)
        print indent*' ', '׼������ ', ans
        return ans

def fib(x):
    """Return Fibonacci of x, where x is a non-negative int"""
    #����xʱ��쳲�������������x�ǷǸ�����
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)
    #�˷�Ч�ʺܵͣ���fib(36)�͹��ˣ�Ϊʲô���Ƿ���ʲô��ЧһЩ���㷨�أ�



# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第四讲：函数抽象及递归介绍
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

##x = 16
##ans = 0
##if x >= 0:
##    while ans*ans < x:
##        ans = ans +1
##        #print 'ans = ',ans
##    if ans*ans != x:
##        print x,' 不是完全平方数'
##    else: print ans
##else: print x,' 是负数'

def sqrt(x):
    """Returns the square root of x, if x is a perfect square.
        Prints an error message and returns None otherwise"""
    #hello如果x是完全平方数，返回x的平方根；否则打印错误信息，并无返回值
    ans = 0  
    if x>= 0:
        while ans*ans < x: ans = ans + 1
        if ans*ans != x:
            print x, ' 不是完全平方数'
            return None  
        else: return ans
    else:
        print x, ' 是负数'
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
    #solve解，num表示number（数目），tot表示total（总数），leg脚、head头、pig猪、chick鸡
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs:
            return (numPigs, numChicks)
    return None

def barnYard():
    #barnyard农场
    heads = int(raw_input('输入头的个数：'))
    legs = int(raw_input('输入脚的个数：'))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print '无解'
    else:
        print '猪的数目是：', pigs
        print '鸡的数目是：', chickens

def solve1(numLegs, numHeads):
    #spider蜘蛛
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs =4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                return [numPigs, numChicks, numSpiders]
    return [None, None, None]

def barnYard1():
    heads = int(raw_input('输入头的个数：'))
    legs = int(raw_input('输入脚的个数：'))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs == None:
        print '无解'
    else:
        print '猪的数目是：', pigs
        print '鸡的数目是：', chickens
        print '蜘蛛的数目是：', spiders

def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs =4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                print '猪的数目是：' + str(numPigs) + ',',
                print '鸡的数目是：' + str(numChicks) + ',',
                print '蜘蛛的数目是：', numSpiders
                solutionFound = True
    if not solutionFound: print '无解'

###test function barnYard2 for solve2 added by ocourse.org
###头数目10，腿数目30可以得到两个解
def barnYard2():
    heads = int(raw_input('输入头的个数：'))
    legs = int(raw_input('输入脚的个数：'))
    solve2(legs, heads)

def isPalindrome(s):
    """Return True if s is a palindrome and False otherwise"""
    #如果是回文（palindrome），返回True；否则返回False
    if len(s) <=1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])
   
def isPalindrome1(s, indent):
    """Return True if s is a palindrome and False otherwise"""
    #indent 缩进
    print indent*' ', 'isPalindrome1调用', s
    if len(s) <= 1:
        print indent*' ', '准备从基础情况返回True'
        return True
    else:
        ans = s[0] == s[-1] and isPalindrome1(s[1:-1], indent + indent)
        print indent*' ', '准备返回 ', ans
        return ans

def fib(x):
    """Return Fibonacci of x, where x is a non-negative int"""
    #返回x时的斐波那契数，其中x是非负整数
    if x == 0 or x == 1: return 1
    else: return fib(x-1) + fib(x-2)
    #此法效率很低，算fib(36)就挂了，为什么？是否有什么高效一些的算法呢？



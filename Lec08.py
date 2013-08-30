# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第八讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def exp1(a,b):
    ans = 1
    while (b>0):
        ans *= a
        b -= 1
    return ans

def exp2(a,b):
    if b == 1:
        return a
    else: return a*exp2(a,b-1)  

def exp3(a,b):
    if b == 1:
        return a
    if (b/2)*2 == b:
        return exp3(a*a, b/2)
    else: return a*exp3(a,b-1)
    

def g(n,m):
    x = 0
    for i in range(n):
        for j in range(m):
            x += 1
    return x

def Towers(size,fromStack,toStack,spareStack):
    if size == 1:
        print 'Move disk from ', fromStack, 'to ', toStack
    else:
        Towers(size-1,fromStack,spareStack,toStack)
        Towers(1,fromStack,toStack,spareStack)
        Towers(size-1,spareStack,toStack,fromStack)

def search(s, e):
    answer = None
    i = 0
    numCompares = 0
    while i < len(s) and answer == None:
        numCompares += 1
        if e == s[i]:
            answer = True
        elif e < s[i]:
            answer = False
        i += 1
    print answer, numCompares

def bsearch(s, e, first, last):
    print first, last
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1)
    return bsearch(s, e, mid + 1, last)

def search1(s,e):
    print bsearch(s, e, 0, len(s) -1)
    print '搜索完毕'

def testSearch():
    s = range(0,1000000)
    raw_input('基本搜索, -1')
    print search(s,-1)
    raw_input('折半搜索, -1')
    print search1(s,-1)
    raw_input('基本搜索, 末尾')
    print search(s,1000000)
    raw_input('折半搜索, 末尾')
    print search1(s,1000000)
    s = range(0,10000000)
    raw_input('基本搜索, 中途')
    print search(s,1000000)
    raw_input('基本搜索, 更大的末尾')
    print search(s,10000000)
    raw_input('折半搜索, 中途')
    print search1(s,1000000)
    raw_input('折半搜索, 更大的尾部')
    print search1(s,10000000)

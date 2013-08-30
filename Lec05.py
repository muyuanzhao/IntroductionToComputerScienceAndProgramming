# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第五讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def squareRootB1(x, epsilon):
    """Assume x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    #假设x>=0且ε>0，返回y，使得y*y在x的ε内
    assert x >= 0, 'x必须为非负数，而不是' + str(x)
    assert epsilon > 0, 'ε必须为正数，而不是' + str(epsilon)
    low = 0
    high = x
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        print 'low:', low, 'high:', high, 'guess:', guess
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <=100, '循环计数次数超出范围'
    print 'Bl方法，循环数', ctr, '估值', guess
    return guess


# MIT600���������ѧ����̵��ۡ���2008���＾������
# ���彲
# ����������ocourse.org
# �γ����۰棺http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def squareRootB1(x, epsilon):
    """Assume x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    #����x>=0�Ҧ�>0������y��ʹ��y*y��x�Ħ���
    assert x >= 0, 'x����Ϊ�Ǹ�����������' + str(x)
    assert epsilon > 0, '�ű���Ϊ������������' + str(epsilon)
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
    assert ctr <=100, 'ѭ����������������Χ'
    print 'Bl������ѭ����', ctr, '��ֵ', guess
    return guess


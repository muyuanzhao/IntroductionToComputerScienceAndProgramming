# MIT600���������ѧ����̵��ۡ���2008���＾������
# ��ʮһ��
# ����������ocourse.org
# �γ����۰棺http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def silly():
    res = []
    done = False
    while not done:
        elem = raw_input('Enter element. Return when done.')
        if elem == '':
            done = True
        else:
            res.append(elem)
    print 'res',res
    tmp = res[:]
    print 'tmp',tmp,'res',res
    tmp.reverse()
    isPal = (res == tmp)
    print 'tmp',tmp,'res',res
    if isPal:
        print 'is a palindrome'
    else:
        print 'is NOT a palindrome'
    
            

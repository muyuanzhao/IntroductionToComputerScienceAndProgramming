# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第十一讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
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
    
            

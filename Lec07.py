# MIT600���������ѧ����̵��ۡ���2008���＾������
# ���߽�
# ����������ocourse.org
# �γ����۰棺http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def showDicts():
    EtoF = {'one': 'un', 'soccer': 'football', 'never': 'janais'}
    print EtoF['soccer']
    raw_input()
    #print EtoF[0]
    print EtoF
    raw_input()
    NtoS = {1: 'one', 2: 'two', 'one': 1, 'two': 2}
    print NtoS
    print NtoS.keys()
    raw_input()
    print NtoS.keys
    raw_input()
    del NtoS['one']
    print NtoS
    raw_input()


### ����ڣ��ṹʽ��������
##import math
##
### ȡ��
##inputOK = False
##while not inputOK:
##    base = input('����ף�')
##    if type(base) == type(1.0): inputOK = True
##    else: print('���󣬵ױ���Ϊ������')
##
### ȡ��
##inputOK = False
##while not inputOK:
##    height = input('����ߣ�')
##    if type(height) == type(1.0): inputOK = True
##    else: print('���󣬸߱���Ϊ������')
##
##hyp = math.sqrt(base*base + height*height)
##
##print '��' + str(base) + '����' + str(height) + '��б��' + str(hyp)


import math

def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = input(requestMsg)
        if type(val) == type(1.0): inputOK = True
        else: print(errorMsg)
    return val

base = getFloat('����ף�','���󣬵ױ���Ϊ������')
height = getFloat('����ߣ�','���󣬸߱���Ϊ������')

hyp = math.sqrt(base*base + height*height)

print '��' + str(base) + '����' + str(height) + '��б��' + str(hyp)

  


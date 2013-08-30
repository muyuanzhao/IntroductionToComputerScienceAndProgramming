# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第七讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
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


### 格教授：结构式代码样例
##import math
##
### 取底
##inputOK = False
##while not inputOK:
##    base = input('输入底：')
##    if type(base) == type(1.0): inputOK = True
##    else: print('错误，底必须为浮点数')
##
### 取高
##inputOK = False
##while not inputOK:
##    height = input('输入高：')
##    if type(height) == type(1.0): inputOK = True
##    else: print('错误，高必须为浮点数')
##
##hyp = math.sqrt(base*base + height*height)
##
##print '底' + str(base) + '，高' + str(height) + '，斜边' + str(hyp)


import math

def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = input(requestMsg)
        if type(val) == type(1.0): inputOK = True
        else: print(errorMsg)
    return val

base = getFloat('输入底：','错误，底必须为浮点数')
height = getFloat('输入高：','错误，高必须为浮点数')

hyp = math.sqrt(base*base + height*height)

print '底' + str(base) + '，高' + str(height) + '，斜边' + str(hyp)

  


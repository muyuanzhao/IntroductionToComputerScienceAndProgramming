# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第九讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def bsearch(s, e, first, last, calls):
    print first, last, calls
    if (last - first) < 2: return s[first] == e or s[last] == e
    mid = first + (last - first)/2
    if s[mid] == e: return True
    if s[mid] > e: return bsearch(s, e, first, mid - 1, calls + 1)
    return bsearch(s, e, mid + 1, last, calls + 1)

def search1(s,e):
    print bsearch(s, e, 0, len(s) -1,0)

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j = j + 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
        print L

def testSelSort():
    test1 = [1,6,3,4,5,2]
    raw_input('运行选择排序测试1')
    selSort(test1)
    test2 = [6,1,2,3,4,5]
    raw_input('运行选择排序测试2')
    selSort(test2)
    test3 = [6,5,4,3,2,1]
    raw_input('运行选择排序测试3')
    selSort(test3)
    test4 = [1,2,3,4,5,6]
    raw_input('运行选择排序测试4')
    selSort(test4)

##def bubbleSort(L):
##    for j in range(len(L)):
##        for i in range(len(L) - 1):
##            if L[i] > L[i+1]:
##                temp = L[i]
##                L[i] = L[i+1]
##                L[i+1] = temp
##        print L

def bubbleSort(L):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp
                swapped = True
        print L


def testBubbleSort():
    test1 = [1,6,3,4,5,2]
    raw_input('运行冒泡排序测试1')
    bubbleSort(test1)
    test2 = [6,1,2,3,4,5]
    raw_input('运行冒泡排序测试2')
    bubbleSort(test2)
    test3 = [6,5,4,3,2,1]
    raw_input('运行冒泡排序测试3')
    bubbleSort(test3)
    test4 = [1,2,3,4,5,6]
    raw_input('运行冒泡排序测试4')
    bubbleSort(test4)

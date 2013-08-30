# MIT600《计算机科学及编程导论》（2008年秋季）样码
# 第十讲
# 翻译制作：ocourse.org
# 课程讨论版：http://ocourse.org/bbs/forum.php?mod=forumdisplay&fid=29
# by yoeo24

def merge(left,right):
    """Assum left and right are sorted lists,
return a new sorted list containing the same elements
as (left + right) would contain."""
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while (i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return result


def mergesort(L):
    """Return a new sort list containing the same elements as L"""
    print L
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)/2
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        together = merge(left,right)
        print 'merged', together
        return together

def create(smallest, largest):
    intSet = []
    for i in range(smallest, largest+1): intSet.append(None)
    return intSet

def insert(intSet, e):
    intSet[e] = 1

def member(intSet, e):
    return intSet[e] == 1

def hashChar(c):
    # c is a char
    # function returns a different integer in the range 0-255
    # for each possible value of c
    return ord(c)

def cSetCreate():
    cSet = []
    for i in range(0, 255): cSet.append(None)
    return cSet

def cSetInsert(cSet, e):
    cSet[hashChar(e)] = 1

def cSetMember(eSet, e):
    return cSet[hashChar(e)] == 1

def readFloat(requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg)
        try:
            val = float(val)
            return val
        except:
            print(errorMsg)

#print readFloat('Enter float: ', 'Not a float.')

def readVal(valType, requestMsg, errorMsg):
    while True:
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except:
            print(errorMsg)

#print readVal(int, 'Enter int: ', 'Not an int.')

def getGrades(fname):
    try:
        gradesFile = open(fname, 'r')
    except IOError:
        print 'Could not open', fnmae
        raise 'GetGradesError'
    grades = []
    for line in gradesFile: grades.append(float(line))
    return grades

    try:
        grades = getGrades('q1grades.txt')
        grades.sort()
        median = grades[len(grades)/2]
        print 'Median grade is', median
    except 'GetGradesError':
        print 'Whoops'
            

import math

# points as lists

def addPoints(p1,p2):
    r=[]
    r.append(p1[0]+p2[0])
    r.append(p1[1]+p2[1])
    return r

##p=[1,2]
##q=[3,1]
##r=addPoints(p,q)
##print r

# points as classes

class cartesianPoint:
    pass

cp1=cartesianPoint()
cp2=cartesianPoint()
cp1.x=1.0
cp1.y=2.0
cp2.x=1.0
cp2.y=3.0

def samePoint(p1,p2):
    return (p1.x==p2.x)and(p1.y==p2.y)

def printPoint(p):
    print '('+str(p.x)+','+str(p.y)+')'

class polarPoint:
    pass

pp1=polarPoint()
pp2=polarPoint()
pp1.radius=1.0
pp1.angle=0
pp2.radius=2.0
pp2.angle=math.pi/4.0

class cPoint:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.radius=math.sqrt(self.x*self.x+self.y*self.y)
        self.angle=math.atan2(self.y,self.x)
    def cartesian(self):
        return (self.x,self.y)
    def polar(self):
        return (self.radius,self.angle)
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'
    def __cmp__(self,other):
        return (self.x>other.x)and(self.y>other.y)
    def __eq__(self,other):
        return (self.x==other.x)and(self.y==other.y)

class Segment:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def length(self):
        return math.sqrt((self.start.x-self.end.x)**2+(self.start.y-self.end.y)**2)

        

from pylab import *
import random,math

def flipTrial(numFlips):
    heads,tails=0,0
    for i in xrange(0,numFlips):
        coin=random.randint(0,1)
        if coin==0: heads+=1
        else: tails+=1
    return heads,tails

def simFlips(numFlips,numTrials):
    diffs=[]
    for i in xrange(0,numTrials):
        heads,tails=flipTrial(numFlips)
        diffs.append(abs(heads-tails))
    diffs=array(diffs)
    diffMean=sum(diffs)/len(diffs)
    diffPercent=(diffs/float(numFlips))*100
    percentMean=sum(diffPercent)/len(diffPercent)
    hist(diffs)
    #axvline(diffMean,lable='Mean')
    legend()
    titleString=str(numFlips)+' Flips, '+str(numTrials)+' Trials'
    title(titleString)
    xlabel('Differnce between heads and tails')
    ylabel('Number of Trials')
    figure()
    plot(diffPercent)
    #axhline(percentMean,lable='Mean')
    legend()
    title(titleString)
    xlabel('Trial Number')
    ylabel('Percent Differnce between heads and tails')

##simFlips(100,100)
##figure()
##simFlips(5000,100)
##simFlips(3,4000)
##show()

def throwDarts(numDarts,shouldPlot):
    inCircle=0
    estimates=[]
    for darts in xrange(1,numDarts+1,1):
        x=random.random()
        y=random.random()
        if math.sqrt(x*x+y*y)<=1.0:
            inCircle+=1
        if shouldPlot:
            piGuess=4*(inCircle/float(darts))
            estimates.append(piGuess)
        if darts%1000000==0:
            piGuess=4*(inCircle/float(darts))
            print 'Number of darts ',darts,', piGuess ',piGuess
    if shouldPlot:
        xAxis = xrange(1,len(estimates)+1)
        semilogx(xAxis,estimates)
        title('Estimate of pi')
        xlabel('Number of darts')
        ylabel('Estimate of pi')
        show()
    return 4*(inCircle/float(numDarts))

def findPi(numDarts,shouldPlot=False):
    piGuess=throwDarts(numDarts,shouldPlot)
    print 'Number of darts ',numDarts,', piGuess ',piGuess

#findPi(10000000)
#findPi(100000,True)

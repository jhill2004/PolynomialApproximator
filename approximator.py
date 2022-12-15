
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp
import array as arr
from scipy.optimize import curve_fit



def getXCoordList(coordList):
    xlist = []
    for item in coordList:
        xlist.append(float(item[0]))
    return xlist

def getYCoordList(coordList):
    ylist = []
    for item in coordList:
        ylist.append(float(item[1]))
    return ylist

def optfunc(x,a,b,c,d,e,f):
    return (a*x**5 + b*x**4 + c*x**3 + d*x**2 + e*x + f)

eqnBool = bool(int(input("Are you inputting an equation (1) or coord points (0): ")))

if (eqnBool):
    #eqn = input("Input the equation: ")
    pi = np.pi
    a = float(input("Input the beginning point of the interval you want to evaluate: "))
    b = float(input("Input the end point of the interval you want to evaluate: "))
    x = np.linspace(a,b,int((b-a)*10), endpoint = True)
    

    eqn = eval(input("Input the expression (use x as variable) (exp() for e^(), pi for pi): "))

    popt, pcov = curve_fit(optfunc, x, eqn)

  
    plt.plot(x,eqn)
    plt.plot(x,optfunc(x,*popt), 'g--')
    plt.show()

else:
    print("Enter your coord points. To stop enter 'stop' (for this patch you must enter a minimum of 6 coord points)")
    x = 0
    y = 0
    coordlist = []

    while (x != "stop" and y != "stop"):
        x = input("X coordinate: ")
        y = input("Y coordinate: ")
        if (x != "stop" and y != "stop"):
            coordlist.append([float(x),float(y)])
    
    xCoordList = getXCoordList(coordlist)
    yCoordList = getYCoordList(coordlist)
    popt, pcov = curve_fit(optfunc, xCoordList, yCoordList)
 



    x = np.array(xCoordList)
    y = np.array(yCoordList)
    x_interp = np.linspace(min(x), max(x), 100, endpoint = True)
    y_interp = optfunc(x_interp,*popt)

    
    
    
    plt.plot(getXCoordList(coordlist),getYCoordList(coordlist))
    plt.plot(x_interp, y_interp,'g--')
  
    plt.show()

    ''' old code
        startPoint = xCoordList[0]
    endPoint = xCoordList[0]
    for key in xCoordList:
        if key > endPoint:
            endpoint = key
        if key < startPoint:
            startPoint = key
    
    domain = np.linspace(startPoint,endPoint,int((endPoint-startPoint)*10), endpoint = True)
    plt.plot(domain, optfunc(domain, *popt))
    '''
    
    
    


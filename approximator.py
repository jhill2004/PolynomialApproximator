import matplotlib.pyplot as plt
import numpy as np
import array as arr



def getXCoordList(coordList):
    xlist = []
    for item in coordList:
        xlist.append(item[0])
    return xlist

def getYCoordList(coordList):
    ylist = []
    for item in coordList:
        ylist.append(item[1])
    return ylist

eqnBool = bool(int(input("Are you inputting an equation (1) or coord points (0): ")))

if (eqnBool):
    #eqn = input("Input the equation: ")
    pi = np.pi
    a = float(input("Input the beginning point of the interval you want to evaluate: "))
    b = float(input("Input the end point of the interval you want to evaluate: "))
    x = np.linspace(a,b,int((b-a)*10), endpoint = True)
    

    eqn = eval(input("Input the expression (use x as variable) (exp() for e^(), pi for pi): "))

    print("eqn")
    plt.plot(x,eqn)
    plt.show()
    exit()
else:
    print("Enter your coord points. To stop enter 'stop'")
    x = 0
    y = 0
    coordlist = []

    while (x != "stop" and y != "stop"):
        x = input("X coordinate: ")
        y = input("Y coordinate: ")
        if (x != "stop" and y != "stop"):
            coordlist.append([float(x),float(y)])
    
    plt.plot(getXCoordList(coordlist),getYCoordList(coordlist))
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Approximator")
    plt.show()
    
    
    


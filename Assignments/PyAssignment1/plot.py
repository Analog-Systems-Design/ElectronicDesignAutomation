import matplotlib.pyplot as plt 
import numpy as np
from Equation import Expression

def checkeqninput(inputtext):
    try:
        dummy = Expression(inputtext,["x"])
        dummytest=dummy(0)
        flag=0
    except:
        print("Please Enter a Valid Equation")
        flag=1
    return flag
def checkeqnlimits(inputtext):
    try:
        float(inputtext)
        flag=0
    except ValueError:
        print("You didnot enter a number please enter a number")
        flag=1
    return flag
def ploteqn(eqn,lowerlimit,upperlimit):
    #Validation for limits
    flag1=checkeqnlimits(lowerlimit)
    if flag1==1:
        print("error in UpperLimit\n")
        
    flag2=checkeqnlimits(upperlimit)
    if flag2==1:
        print("error in LowerLimit\n")
    #Validation for equation
    flag3=checkeqninput(eqn)
    #return flag
    
    # Accuracy of Sampler
    accuracy=10000
    # Generate Stream
    if flag1==0 and flag2==0 and flag3==0:
        # Extract Equation from Text
        fn = Expression(eqn,["x"])
        x = np.linspace(float(lowerlimit),float(upperlimit), accuracy)
        y = fn(x)
        flag=0
    else:
        x=0
        y=0
        flag=1
    return flag,x, y

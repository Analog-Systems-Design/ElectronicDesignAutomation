import pytest
from plot import checkeqninput, checkeqnlimits

#Validation
def testcheckeqnlimits():
    assert(checkeqnlimits("a12")==1)
    assert(checkeqnlimits("12")==0)
    assert(checkeqnlimits("a1.22")==1)
    assert(checkeqnlimits("a12b")==1)
    assert(checkeqnlimits("-1.22")==0)
    
def testcheckinputeqn():
    assert(checkeqninput("a12")==1)
    assert(checkeqninput("sin(x)")==0)
    assert(checkeqninput("ax")==1)
    assert(checkeqninput("a5s")==1)
    assert(checkeqninput("cos(x)")==0)
    






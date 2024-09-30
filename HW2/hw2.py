import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        

        
def rhs(LS,p):
    x1=LS.A.x
    y1=LS.A.y
    x2=LS.B.x
    y2=LS.B.y
    x3=p.x
    y3=p.y
    
    a1=x2-x1  #define two lines x and y. a1,b1 are line1 x,y. a2,b2 are line2 x,y
    b1=y2-y1
    a2=x3-x1
    b2=y3-y1
    ans=a1*b2-b1*a2
    
    if ans>0:
        return -1
    elif ans<0:
        return 1
    else:
        return 0

def cross(LS1,LS2):
    x1=LS1.A
    y1=LS1.B
    x2=LS2.A
    y2=LS2.B
    ans1=rhs(LS1,x2)
    ans2=rhs(LS1,y2)
    ans3=rhs(LS1,x1)
    ans4=rhs(LS1,y1)
    
    if (ans1*ans2==-1 and ans3*ans4==-1):
        return 1        
    else:
        return 0

def diffside(q1,q2,p1,p2):
    LS1=Line(q1,q2)
    LS2=Line(p1,p2)
    ans1=rhs(LS1,p1)
    ans2=rhs(LS1,p2)
    ans3=rhs(LS2,q1)
    ans4=rhs(LS2,q2)
    
    if (ans1*ans2==-1 and ans3*ans4==-1):
        return 1    
    elif(ans1==0 or ans2==0 or ans3==0 or ans4==0):
        return 0
    else:
        return -1

def PiP_1(p,P): #Assignment 2-1
    
    ans=1
    for i in range(n):
        a=P[i]
        b=P[(i+1)%n]
        LS=Line(a,b)
        if(rhs(LS,p)!=-1):
            ans=0
    if(ans==1):
        return 1
    else:
        return 0
    
def PiP_2(p,P): #Assignment 2-2
    numCount=0
    max_r=0
    for i in range(n):
        max_r=max(max_r,P[i].x)
    
    p1=Point(max_r+10,p.y)
    for i in range(n):
        LS1=Line(P[i],P[(i+1)%n])
        LS2=Line(p,p1)
        if(cross(LS1,LS2)):
            numCount+=1
    if(numCount%2==1):
        return 1
    else:
        return 0
    
def PiP_3(p,P): #Assignment 2-3
    numCount=0
    max_r=0
    for i in range(n):
        max_r=max(max_r,P[i].x)

    p1=Point(max_r+10,p.y)
    i=0
    while i<n:
        LS1=Line(P[i],P[(i+1)%n])
        LS2=Line(p,p1)
        if(cross(LS1,LS2)):
            numCount+=1
        elif(diffside(p,p1,P[i],P[(i+1)%n])==0 and diffside(p,p1,P[(i-1+n)%n],P[i])==0):    
            x=(i-1+n)%n
            y=(i+1)%n
            while(diffside(p,p1,P[x],P[y])==0 and i<n):
                y=(y+1)%n
                i+=1
            if(diffside(p,p1,P[x],P[y])==1 and i<n):
                numCount+=1
            P[(y-1+n)%n]=P[x]
        i+=1
    print(numCount)
    if(numCount%2==1):
        return 1
    else:
        return 0 
    
if __name__ == '__main__':
    
    n=int(input())
    P=list([])
    for i in range(n):
        x=int(input("coordinate x:"))
        y=int(input("coordinate y:"))
        p=Point(x,y)
        P.append(p)
    x=int(input("coordinate x:"))
    y=int(input("coordinate y:"))
    p=Point(x,y)
    if(PiP_3(p,P)==1): #you can choose three functions at here and just change number
        print("p is located inside P")
    else:
        print("p is not located inside P")
    
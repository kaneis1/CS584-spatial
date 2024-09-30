import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    
def area(p1,p2,p3):
    x1=p2.x-p1.x
    y1=p2.y-p1.y
    x2=p3.x-p1.x
    y2=p3.y-p1.y
        
    ans=(x1*y2)-(x2*y1)
    ans=abs(ans)
    return ans/2    

       
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
    
    
if __name__ == '__main__':
    p1=Point(2,5)
    p2=Point(2,6)
    p3=Point(0,2)
    p4=Point(0,13)
    p5=Point(3,7)
    p6=Point(-1,9)
    
    ans_a1=area(p1,p2,p3)
    
    ans_a2=area(p4,p5,p6)
    
    L1=Line(p1,p2)
    if rhs(L1,p3)==1:
        ans_b1='p3 is right to the p1->p2'
    else:
        ans_b1='p3 is left to the p1->p2'
    L2=Line(p5,p6)
    if rhs(L2,p4)==1:
        ans_b2='p4 is right to the p5->p6'
    else:
        ans_b2='p4 is left to the p5->p6'
    L3=Line(p4,p5)
    if cross(L1,L3)==1:
        ans_c='do cross'
    else:
        ans_c='no cross'
        
    L4=Line(p4,p1)
    L5=Line(p2,p3)
    if cross(L4,L5)==1:
        ans_d='do cross'
    else:
        ans_d='no cross'
        
    print('the ans of q1_a',ans_a1,' ',ans_a2)
    print('the ans of q1_b',ans_b1,' ',ans_b2)
    print('the ans of q1_c',ans_c)
    print('the ans of q1_d',ans_d)


'''
the ans of q1_a 1.0   9.0
the ans of q1_b p3 is left to the p1->p2   p4 is right to the p5->p6
the ans of q1_c do cross
the ans of q1_d do cross
'''
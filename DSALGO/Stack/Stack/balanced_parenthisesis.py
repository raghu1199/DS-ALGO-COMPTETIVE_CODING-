open=["[","{","("]
close=["]","}",")"]

def check(mystr):
    stack=[]
    for exp in mystr:
        if exp in open:
            stack.append(exp)
        elif exp in close:
            pos=close.index(exp) # returns index of this exp from close list
            if stack[len(stack)-1]==open[pos]:   # compare two equal parenthiss in stack it will be open and we chekcing in open
                stack.pop() # remove that open parenthis which is balanced
            else:
                return "unbalanced"
    return ("balanced")

mystr="{1+2(3*5)+[8/4)}"
myexp="{1+2*(4+5)}"
print(check(myexp))
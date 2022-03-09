
open=['[','{','(']
close=[']','}',')']


#only append open paranthesis ,on ancountering close get it index compare with lastly appended paranthesi
def check(mystr):
    stack=[]
    for i in mystr:
        if i in open:
            stack.append(i)
        elif i in close:
            pos=close.index(i)
            if len(stack)>0 and stack[len(stack)-1] ==open[pos]:
                stack.pop()
            else:
                return "Unbalanced"
    
    return "balanced"

print(check("[({})]"))


def validPalindrom(str):
    text=""
    for c in str:
        if c.isalpha():
            text+=c
        elif c.isdigit():
            text+=c
    
    l,r=0,len(text)-1
    while l<=r:
        if text[l]==text[r]:
            l+=1
            r-=1
        else:
            return False
    return True

str="race5 a 5ecar"
print(validPalindrom(str))


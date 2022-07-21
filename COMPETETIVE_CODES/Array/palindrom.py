

def ispalindrom(s):
    text=""
    for c in s:
        if c.isalpha():
            text+=c
        elif c.isdigit():
            text+=c
    text=text.lower()
    #s="".join(s.split(" "))

    print(text)
    l,r=0,len(text)-1
    while l<=r:
        if text[l]==text[r]:
            l+=1
            r-=1
        else:
            return False

    return True

print(ispalindrom(" Race : a 9eCar "))

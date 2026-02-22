

def getBondPrice(y, face, couponRate, m, ppy=1):
    r=y/ppy
    n=int(m*ppy)
    c=couponRate/ppy
    x=0.0
    for t in range(1, n+1):
        x += c/((1+r)**t)
    x += face/(1+r)**n) 
    return(x)

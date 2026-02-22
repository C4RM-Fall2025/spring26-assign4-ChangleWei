def getBondDuration(y, face, couponRate, m, ppy = 1):
    r = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    price = 0.0
    weightSum = 0.0

for t in range (1, n + 1):
    cf = c
    if t == n:
        cf = c + face
    pvcf = cf / ((1+r)**t)
    
    price += pvcf
    weightsum += t * pvcf

duration_periods = weightsum / price
duration_years = duration_periods / ppy

return durtion_years

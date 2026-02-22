def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy
    n = int(m * ppy)
    c = face * couponRate / ppy

    price = 0.0
    weighted_sum = 0.0

    for t in range(1, n + 1):
        cf = c
        if t == n:
            cf = c + face

        pvcf = cf / ((1 + r) ** t)
        price += pvcf
        weighted_sum += t * pvcf

    duration_periods = weighted_sum / price
    duration_years = duration_periods / ppy
    return duration_years

def getBondPrice_E(face, couponRate, yc):
    coupon = face * couponRate
    bondPrice = 0.0
    m = len(yc)

    for t, y in enumerate(yc, start=1):
        cf = coupon
        if t == m:
            cf = coupon + face

        pv = 1 / ((1 + y) ** t)
        bondPrice += cf * pv

    return bondPrice

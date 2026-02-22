def getBondPrice_E(face, couponRate, m, yc):
    coupon = face * couponRate
    bondPrice = 0.0

    m = min(m, len(yc))

    for t, y in enumerate(yc[:m], start=1):
        cf = coupon
        if t == m:
            cf = coupon + face

        pv = 1 / ((1 + y) ** t)
        bondPrice += cf * pv

    return bondPrice

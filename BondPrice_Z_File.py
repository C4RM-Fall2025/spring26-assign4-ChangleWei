def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0.0

    last_i = len(times) - 1

    for i, (t, y) in enumerate(zip(times, yc)):
        cf = coupon
        if i == last_i:
            cf = coupon + face
        pv = 1 / ((1 + y) ** t)
        bondPrice += cf * pv
    return bondPrice

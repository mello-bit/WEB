def count_delta(lowerPos, upperPos):
    delta = float(upperPos.split(' ')[0]) - \
        float(lowerPos.split(' ')[0])

    delta2 = float(upperPos.split(' ')[1]) - \
        float(lowerPos.split(' ')[1])

    return [str(round(delta, 3)), str(round(delta2, 3))]

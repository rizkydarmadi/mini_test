def bukan_bilangan_prima():
    prima = []

    for i in range(1, 100 + 1):
        if i == 1:
            prima.append(i)
        elif i == 2:
            continue
        elif i == 3:
            continue
        elif i == 5:
            continue
        elif i == 7:
            continue
        elif (i % 2) == 0:
            prima.append(i)
        elif (i % 3) == 0:
            prima.append(i)
        elif (i % 5) == 0:
            prima.append(i)
        elif (i % 7) == 0:
            prima.append(i)
        else:
            continue

    return prima


def change():
    result = []
    for i in bukan_bilangan_prima():
        if (i % 3) == 0:
            result.append("Foo")
        elif (i % 5) == 0:
            result.append("Bar")
        elif ((i % 3) and (i % 5)) == 0:
            result.append("FooBar")
        else:
            result.append(i)

    print(result[::-1])


change()

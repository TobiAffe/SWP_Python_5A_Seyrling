import random
def lottoziehung(length, how_many):
    lotto = []
    for i in range(1, length + 1):
        lotto.append(i)

    list_range = range(0, len(lotto))
    for i in list_range:
        ran = random.randint(list_range[0], list_range[-1])
        lotto[ran], lotto[-i] = lotto[-i], lotto[ran]
    return lotto[-how_many:]

def lotto_statistik(length, how_many, count):
    statistik = {}
    for key in range(1, length + 1):
        statistik[key] = 0

    for i in range(count):
        for j in lottoziehung(length, how_many):
            statistik[j] += 1
    return statistik

statistik = lotto_statistik(45, 6, 10000)
print(statistik)

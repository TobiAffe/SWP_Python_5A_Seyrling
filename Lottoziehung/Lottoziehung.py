import random
def lottoziehung(length, how_many):
    lotto = []
    for i in range(1, length + 1):
        lotto.append(i)

    for i in range(len(lotto)):
        ran = random.randint(0, length-i-1)
        val_ran = lotto[ran]
        lotto[ran] = lotto[-i]
        lotto[-i] = val_ran
    return lotto[:how_many]

def lotto_statistik(length, how_many, count):
    statistik = {}
    for key in range(1, length + 1):
        statistik[key] = 0

    for i in range(count):
        for j in lottoziehung(length, how_many):
            statistik[j] += 1

    return statistik

statistik = lotto_statistik(1000, 45, 6)
print(statistik)

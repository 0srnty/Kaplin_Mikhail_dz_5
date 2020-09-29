import collections

pred = collections.defaultdict()
n = int(input("Введите количество предприятий для расчета прибыли: "))
s = 0
for i in range(n):
    pname = input("Введите название предприятия " + str(i + 1) + ": ")
    numbers = input("через пробел введите прибыль данного предприятия за каждый квартал: ")
    psum = sum(map(int, numbers.split(' ')))
    pred[pname] = psum
    s += psum

avrg = s / n
print("\nСредняя годовая прибыль всех предприятий: %.0f. Предприятия, с прибылью выше среднего значения:" % avrg)
for i in pred:
    if pred[i] > avrg:
        print(i)
print("Предприятия, с прибылью ниже среднего значения:")
for i in pred:
    if pred[i] < avrg:
        print(i)
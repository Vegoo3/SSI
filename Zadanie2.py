import ReadFile
import matplotlib.pyplot as plt
import chart

list = []
listofatrybut = []
iris = ReadFile.wczytajPlik("iris.txt")
irisnazwa = ReadFile.wczytajPlik('iris-type.txt')




for i in range(len(iris)):
    a = iris[i][len(iris[0]) - 1]
    if float(a) in list:
        continue
    list.append(float(a))


for i in range(len(list)):
    listofatrybut.append([list[i]])


for i in range(len(iris)):
    a = iris[i][len(iris[0]) - 1]
    for j in range(len(listofatrybut)):
        if int(a) == int(listofatrybut[j][0]):
            listofatrybut[j].append(iris[i])
            break


for i in range(len(listofatrybut)):
    listofatrybut[i].pop(0)
nazwyKwiatkow = ["Virginica", "Versicolour", "Setosa"]
plt.subplot(2, 2, 1)
x = chart.wezWspolrzedna(3, listofatrybut)
y = chart.wezWspolrzedna(4, listofatrybut)
chart.stworzWykres(x, y, nazwyKwiatkow, 'atrybut 3', 'atrybut 4')


plt.subplot(2, 2, 2)
x = chart.wezWspolrzedna(2, listofatrybut)
y = chart.wezWspolrzedna(4, listofatrybut)
chart.stworzWykres(x, y, nazwyKwiatkow, 'atrybut 2', 'atrybut 4')

plt.subplot(2, 2, 3)
x = chart.wezWspolrzedna(1, listofatrybut)
y = chart.wezWspolrzedna(4, listofatrybut)
chart.stworzWykres(x, y, nazwyKwiatkow, 'atrybut 1', 'atrybut 4')


plt.subplot(2, 2, 4)
x = chart.wezWspolrzedna(2, listofatrybut)
y = chart.wezWspolrzedna(3, listofatrybut)
chart.stworzWykres(x, y, nazwyKwiatkow, 'atrybut 2', 'atrybut 3')


plt.show()



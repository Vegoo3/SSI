import ReadFile
import math
import matplotlib.pyplot as plt
import random

m = 4
spiralka = ReadFile.wczytajPlik('spiralka.txt')
obecneSrodkiIndex = random.sample(range(0, len(spiralka)), m)
#obecneSrodkiIndex = [10, 15, 20, 25]
obecneSrodki = []

for i in range(m):
    obecneSrodki.append(spiralka[obecneSrodkiIndex[i]])

for y in range(20):
    plt.figure(y)
    podzialNaGrupy = []

    for i in range(len(obecneSrodkiIndex)):

        podzialNaGrupy.append([obecneSrodki[i]])

    for i in range(len(spiralka)):
        najmniejszaOdleglosc = 9999999
        for j in range(len(obecneSrodkiIndex)):
            odleglosc = 0
            for k in range(len(spiralka[0])):
                odleglosc = odleglosc + (math.pow(((float(podzialNaGrupy[j][0][k])) - float(spiralka[i][k])), 2))
            odleglosc = math.sqrt(odleglosc)
            if odleglosc < najmniejszaOdleglosc:
                najmniejszaOdleglosc = odleglosc
                zapamietajGrupa = j
        podzialNaGrupy[zapamietajGrupa].append(spiralka[i])

    if int(y) > 0:
        for i in range(m):
            podzialNaGrupy[i].pop(0)

    for i in range(len(podzialNaGrupy)):
        x = []
        y = []
        for j in range(len(podzialNaGrupy[i])):
             x.append(float(podzialNaGrupy[i][j][0]))
             y.append(float(podzialNaGrupy[i][j][1]))
        plt.scatter(x, y, label='grupa ' + str(i+1), marker='s')
    x = []
    y = []
    for i in range(len(obecneSrodki)):
        x.append(float(obecneSrodki[i][0]))
        y.append(float(obecneSrodki[i][1]))
    plt.scatter(x, y, label='srodki', marker='*')


    obecneSrodki = []
    sredniaX = 0
    sredniaY = 0
    for i in range(m):
        sredniaX = 0
        sredniaY = 0
        for j in range(len(podzialNaGrupy[i])):
            sredniaX = sredniaX + float(podzialNaGrupy[i][j][0])
            sredniaY = sredniaY + float(podzialNaGrupy[i][j][1])
        sredniaX = sredniaX / len(podzialNaGrupy[i])
        sredniaY = sredniaY / len(podzialNaGrupy[i])
        obecneSrodki.append([sredniaX, sredniaY])
    plt.legend()

plt.show()



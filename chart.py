import matplotlib.pyplot as plt
import random


def wezWspolrzedna(pozycja, nazwaListy):
    pozycja = pozycja - 1
    wynik = []
    for i in range(len(nazwaListy)):
        a = []
        for j in range(len(nazwaListy[0])):
            a.append(float(nazwaListy[i][j][pozycja]))
        wynik.append(a)
    return wynik


def stworzWykres(a, b, lista, xlabel, ylabel):
    for i in range(len(a)):
        plt.scatter(a[i], b[i], label=lista[i],
                     marker='o')
    plt.legend()
    #plt.axis([0, 7.1, 0, 2.6])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()


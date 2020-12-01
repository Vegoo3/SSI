import ReadFile

listaWartosci = ReadFile.wczytajPlik("australian.txt")
listaAtrybutow = ReadFile.wczytajPlik("australian-type.txt")



for i in range(len(listaAtrybutow)):
    for j in range(len(listaWartosci)):
        listaAtrybutow[i].append(listaWartosci[j][i])



for i in range(len(listaAtrybutow)):
    print(listaAtrybutow[i][0] + ": ", listaAtrybutow[i][1], listaAtrybutow[i][2:3])

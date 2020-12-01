def wczytajPlik(nazwaPliku):
    lista = []
    i = 1
    a_file = open(nazwaPliku, "r")
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        if len(line_list) == 0:
            continue
        if int(i) == 1:
            dl = len(line_list)
            i = 0
        if len(line_list) != dl:
            print("rozna dlugosc")
            return 0
        lista.append(line_list)
    a_file.close()
    return lista


def sprawdzAtrybut(x, y, list1, list2):
    print("wartość atrybutu: " + str(list1[x][y]))
    print("nazwa atrybutu: " + list2[y][0])
    if list2[y][1] == "s":
        print("czy atrybut symboliczny: false")
    else:
        print("czy atrybut symboliczny: true")

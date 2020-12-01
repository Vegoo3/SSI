def potega(n):
    if int(n)==0:
        return 1
    else:
        return n*potega(n-1)

XD = potega(4)
print(XD)
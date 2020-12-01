import random
import math
import matplotlib.pyplot as plt


rozrzut = 10
wsp_przyrostu = 1.1
l = 10
x = random.randint(0, 100)
y = ((math.sin(x / 10))) * (math.sin(x / 200))


labelX = []
labelY = []
for i in range(100):
    labelX.append(float(i))
    labelY.append(((math.sin(i / 10))) * (math.sin(i / 200)))



for i in range(l):
    plt.figure(i)
    plt.plot(labelX, labelY)
    xpot = x + random.randint(-10, 10)
    if float(xpot) > 100.0 and float(xpot) < 0.0:
        xpot = random.randint(0, 100)
    ypot = ((math.sin(xpot / 10))) * (math.sin(xpot / 200))
    if float(ypot) >= float(y):
        x = xpot
        y = ypot
        rozrzut = rozrzut * wsp_przyrostu
    else:
        rozrzut = rozrzut / wsp_przyrostu
    plt.scatter(x,y,label='punkt', marker='*',color='r')
    print(i)
    print("x = " + str(x))
    print("xpot = " + str(xpot))
    print("y = " + str(y))
    print("ypot = " + str(ypot))
    print("rozrzut = " + str(rozrzut))
    print("=====")
    plt.show()




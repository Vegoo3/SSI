import matplotlib.pyplot as plt
import numpy as np

oczyNosX = [-1, 0, 1]
oczyNosY = [1, 0, 1]

ustaX = np.linspace(0, np.pi, 100)
ustaY = np.sin(ustaX)

glowyX = [-2, -1.8, -1.4, -0.8, 0.0, 0.8, 1.4, 1.8, 2]
goraglowyY = [0, 0.8, 1.4, 1.8, 2, 1.8, 1.4, 0.8, 0]
dolglowyY = [0, -0.8, -1.4, -1.8, -2, -1.8, -1.4, -0.8, 0]

plt.plot(glowyX, goraglowyY, label='lamane',color='r')
plt.plot(glowyX, dolglowyY, color='r')
plt.plot((ustaX - 1.58)*0.64, ustaY*-1, label='sin', color='y')
plt.scatter(oczyNosX, oczyNosY, label='punkty', marker='D')
plt.axis([-2, 2, -3, 3])
plt.grid(True)
plt.legend()
plt.show()
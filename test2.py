import matplotlib.pyplot as plt
import numpy as np

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(np.random.randn(100))
plt.subplot(2, 2, 2)
plt.plot(np.random.random(size=100), "+")
plt.plot(2, 2, 3)
plt.plot(np.random.randn(), "r.")
plt.plot(2, 2, 4)
plt.plot(np.random.randn(100), "g--")
plt.savefig("mes_graphiques.jpg")
plt.show()

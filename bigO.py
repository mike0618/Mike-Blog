import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

plt.style.use('dark_background')

# set up runtime comparisons
n = np.linspace(1, 10)
labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponencial', 'Factorial']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n, gamma(n + 1)]

# plot setup
plt.figure(figsize=(12, 10))
plt.ylim(0, 1000)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label=labels[i])

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.show()

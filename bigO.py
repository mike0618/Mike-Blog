import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

plt.style.use('dark_background')

# set up runtime comparisons
n = np.linspace(1, 100)
big_o = {'Constant': np.ones(n.shape),
         'Logarithmic': np.log(n),
         'Linear': n,
         'Log Linear': n * np.log(n),
         'Quadratic': n ** 2,
         'Cubic': n ** 3,
         'Exponential': 2 ** n,
         'Factorial': gamma(n + 1)}

# plot setup
plt.figure(figsize=(10, 6))
plt.ylim(0, 1000)

for k, v in big_o.items():
    plt.plot(n, v, label=k)

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

plt.style.use('dark_background')

# set up runtime comparisons
n = np.linspace(1, 50)
big_o = {'Constant': np.ones(n.shape),
         'Logarithmic': np.log(n),
         'Linear': n,
         'Log Linear': n * np.log(n),
         'Quadratic': n ** 2,
         'Cubic': n ** 3,
         'Exponential': 2 ** n,
         'Factorial': gamma(n + 1)}

# plot setup
fig = plt.figure(figsize=(20, 11))
plt.ylim(0, 1000)
plt.xlim(0, 50)

for k, v in big_o.items():
    plt.plot(n, v, label=k)

plt.legend(loc=0)
plt.ylabel('Relative Runtime')
plt.xlabel('n')
plt.tight_layout()
plt.get_current_fig_manager().set_window_title('Big O Notation')
plt.margins(x=0)
fig.subplots_adjust(
    top=0.99,
    bottom=0.05,
    left=0.04,
    right=0.99,
    hspace=0.2,
    wspace=0.2
)
plt.show()

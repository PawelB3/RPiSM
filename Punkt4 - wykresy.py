from matplotlib import pyplot as plt
from numpy import *
from scipy.stats import norm
import numpy as np


def count_possibilities(k):
    for i in range(1, 7):
        throws[k-1] = i
        if k > 1:
            count_possibilities(k-1)
        else:
            total.append(sum(throws))


total = []
k = 4
throws = [0 for _ in range(k)]
count_possibilities(k)

#print(total)

distribution = norm(mean(total), std(total))
values = np.unique(total)
probabilities = [distribution.pdf(value) for value in values]
cdf = np.cumsum(probabilities)


plt.plot(values, probabilities, label='gęstość')
plt.grid(True)
plt.plot(values, cdf, label='dystrybuanta', color='r')
plt.legend()
plt.savefig("wykres")
plt.show()

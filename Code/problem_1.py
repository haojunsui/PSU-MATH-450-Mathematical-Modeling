import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

x = np.matrix([74.4, 93.4, 110.4, 130.6, 148.9, 170.7, 191.1, 211.8, 231.7, 259.1]).transpose()
y = np.matrix([1.64, 2.03, 3.16, 3.96, 4.78, 6.21, 7.28, 8.91, 8.79, 8.63]).transpose()

x_log10 = np.log10(x)
A = np.concatenate((np.matrix(np.ones(x.shape[0])).transpose(), x_log10), axis=1)
b = np.log10(y)

betas = inv(A.transpose() * A) * A.transpose() * b

y_log_fit = A * betas

plt.figure(figsize=(10,8))
plt.plot(np.array(x_log10), np.array(b), "ro", markersize=8)
plt.plot(np.array(x_log10), np.array(y_log_fit), "b", linewidth=2)
plt.xlabel("$\log_{10}x$ (kg)", fontsize=24)
plt.ylabel("$\log_{10}y$ (kg)", fontsize=24)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(["Data", "Best fit, $\log_{10}y = %.3f + %.3f\log_{10}x$" % (betas.item((0, 0)), betas.item((1, 0)))], loc="upper left", fontsize=20)
plt.savefig("problem_1_log_fit.eps", format="eps", dpi=1000)
plt.show()

print betas.item((1, 0))

y_fit = np.power(10, betas.item((0, 0))) * np.power(x, betas.item((1, 0)))

plt.figure(figsize=(10,8))
plt.plot(np.array(x), np.array(y), "ro", markersize=8)
plt.plot(np.array(x), np.array(y_fit), "b", linewidth=2)
plt.xlabel("$x$ (kg)", fontsize=24)
plt.ylabel("$y$ (kg)", fontsize=24)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(["Data", "Best fit, $y = %.3f * x ^ {%.3f}$" % (np.power(10, betas.item((0, 0))), betas.item((1, 0)))], loc="upper left", fontsize=20)
plt.savefig("problem_1_fit.eps", format="eps", dpi=1000)
plt.show()

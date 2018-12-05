#%%
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#%%
truth_N    = [] # num of data
truth_mean = [] # mean
truth_var  = [] # variance

#%%
truth_N.append(100)
truth_mean.append(-18)
truth_var.append(2)

truth_N.append(600)
truth_mean.append(25)
truth_var.append(5)

truth_N.append(300)
truth_mean.append(0)
truth_var.append(6)

#%%
K = len(truth_N)
c_truth_N = np.cumsum(np.concatenate(([0,], truth_N)))
N = c_truth_N[-1]
truth_pi = np.array(truth_N) / N

#%% make data
datas = np.zeros(N)

for i in range(K):
    n = truth_N[i]
    m = truth_mean[i]
    v = truth_var[i]
    d = norm.rvs(loc=m, scale=v, size=n)

    l = c_truth_N[i]
    r = c_truth_N[i+1]
    datas[l:r] = d

#%%
plt.hist(datas, bins=100)
# plt.show()
plt.savefig("./data_histogram.png")

#%%
np.savetxt("./data.txt", datas)

#%%
print(f"N: {N}")
print(f"pi: {truth_pi}")
print(f"mean: {truth_mean}")
print(f"variance: {truth_var}")

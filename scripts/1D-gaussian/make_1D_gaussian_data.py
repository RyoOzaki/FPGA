#%%
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from pathlib import Path

#%%
file_name_temp = "1D-gaussian-{}.{}"
means = [1.5, -1.5, 0.0, 5.0, -5.0]
stds = [1.0, 4.0, 10.0, 0.5, 0.2]
Ns = [300, 300, 300, 300, 300]

for i in range(len(means)):
    alp = chr(i + 65)

    data = stats.norm.rvs(loc=means[i], scale=stds[i], size=Ns[i])

    plt.clf()
    plt.hist(data, bins=100)
    plt.title("Mean={}, Std={}, N={}".format(means[i], stds[i], Ns[i]))
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.savefig("/home/ema/FPGA/scripts/1D-gaussian/datas/" + file_name_temp.format(alp, "png"))

    np.savetxt("/home/ema/FPGA/scripts/1D-gaussian/datas/" + file_name_temp.format(alp, "txt"), data)

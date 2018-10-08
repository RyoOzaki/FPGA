#%%
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from pathlib import Path

#%%
file_name_temp = "1D-Gaussian-{}.{}"
means = [1.5, -1.5, 0.0, 5.0, -5.0]
stds = [1.0, 4.0, 10.0, 0.5, 0.2]
Ns = [300, 300, 300, 300, 300]

#%%
params_file = Path("/home/ema/FPGA/scripts/1D-Gaussian/datas/parameters.txt")
with params_file.open(mode="w") as f:
    f.write("This file shows the parameters of 1-D Gaussian datas.\n\n")

#%%
for i in range(len(means)):
    alp = chr(i + 65)

    data = stats.norm.rvs(loc=means[i], scale=stds[i], size=Ns[i])

    plt.clf()
    plt.hist(data, bins=100)
    plt.title("Mean={}, Std={}, N={}".format(means[i], stds[i], Ns[i]))
    plt.xlabel("$x_1$")
    plt.ylabel("$x_2$")
    plt.savefig("/home/ema/FPGA/scripts/1D-Gaussian/datas/" + file_name_temp.format(alp, "png"))

    np.savetxt("/home/ema/FPGA/scripts/1D-Gaussian/datas/" + file_name_temp.format(alp, "txt"), data)

    with params_file.open(mode="a") as f:
        f.write("=====   1D-Gaussian-{}   =====\n".format(alp))
        f.write("Mean: {}\n".format(means[i]))
        f.write("Std : {}\n".format(stds[i]))
        f.write("N   : {}\n\n".format(Ns[i]))

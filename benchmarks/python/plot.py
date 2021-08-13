import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot(x, labels, list_df, names):

    plt.figure(figsize=(80, 40), dpi=100)
    plt.subplot(1, 2, 1)
    x_indices = []
    width = 0.25
    rect = [0, 0, 0]
    _list = []
    for ind, list in enumerate(list_df):
        if ind < 3:
            _list.append(list)
    for ind, time_taken in enumerate(_list):
        rect[ind] = plt.bar(x + width * ind, time_taken, width, align = 'center', label = labels[ind])
        x_indices.append(
            x + width * ind
        )
        plt.bar_label(rect[ind], padding = 3, fontsize = 33)
    plt.xticks(x + width, names, fontsize = 40)
    plt.yticks(fontsize = 30)
    plt.legend(fontsize = 50)
    plt.ylabel(r'$\frac{Time}{nParticles^2}$', fontsize = 50)
    plt.xlabel(r"$Number\ of\ Particles\ Simulated(nParticles)$", fontsize = 50)
    plt.title(r"$Library\ used\ for\ Implementation$", fontsize = 60)

    plt.subplot(1, 2, 2)
    rect = [0, 0, 0]
    colors = ['lightcoral', 'navy', 'm']
    _list = []
    for ind, list in enumerate(list_df):
        if ind >= 3:
            _list.append(list)
    j = 3
    for ind, time_taken in enumerate(_list):
        rect[ind] = plt.bar(x + width * ind, time_taken, width, align = 'center', color = colors[ind % len(colors)], label = labels[j])
        x_indices.append(
            x + width * ind
        )
        j += 1
        plt.bar_label(rect[ind], padding = 3, fontsize = 33)
    plt.xticks(x + width, names, fontsize = 40)
    plt.yticks(fontsize = 30)
    plt.legend(fontsize = 50)
    plt.ylabel(r'$\frac{Time}{nParticles^2}$', fontsize = 50)
    plt.xlabel(r"$Number\ of\ Particles\ Simulated(nParticles)$", fontsize = 50)
    plt.title(r"$Accelerator\ used\ for\ Implementation$", fontsize = 60)
    
    plt.suptitle("Performance Comparision; Number of Iterations: 5", fontsize = 70)
    plt.savefig("subplot")

if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    df = df.drop(['Unnamed: 0'], axis = 1)
    df = df.T
    df.columns = ["Python-NumPy", "Pure-NumPy", "Pure-Python", "C++", "Numba", "Pythran: Transonic"]

    labels = df.columns
    names = ["16", "32", "64", "128"]

    df = df.T
    x = np.arange(len(df.columns))
    list_df = df[0:].to_numpy().tolist()

    plot(x, labels, list_df, names)
    

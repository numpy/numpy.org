import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot(x, labels, list_df, names):

    plt.figure(figsize=(350, 220), dpi=30)
    plt.subplot(2, 1, 1)

    width = 0.25
    rect = [0, 0, 0]

    list1 = []
    for ind, list in enumerate(list_df):
        if ind < 2:
            list1.append(list)

    for ind, time_taken in enumerate(list1):
        rect[ind] = plt.bar(x + width*ind, time_taken, width, align='center', label=labels[ind])
        plt.bar_label(rect[ind], padding=3, fontsize=250)
 
    plt.xticks(x + width/2, names, fontsize=300)
    plt.tick_params(axis='x', which='major', pad=50)
    plt.yticks(fontsize=300)
    plt.legend(fontsize=250)
    
    plt.ylabel(r'$\frac{Time}{nParticles^2}$', fontsize=350)
    plt.xlabel(r"$Number\ of\ Particles\ Simulated(nParticles)$", fontsize=270)
    plt.title(r"$Library\ based\ Implementation$", fontsize=300)

    plt.subplot(2, 1, 2)
    rect = [0, 0, 0]
    colors = ['lightcoral', 'navy', 'm']
    
    list2 = []
    for ind, list in enumerate(list_df):
        if ind >= 2:
            list2.append(list)

    j = 2
    for ind, time_taken in enumerate(list2):
        rect[ind] = plt.bar(x + width*ind, time_taken, width, align='center', color=colors[ind % len(colors)], label=labels[j])
        j += 1
        plt.bar_label(rect[ind], padding=3, fontsize=250)
 
    plt.xticks(x + width, names, fontsize=300)
    plt.yticks(fontsize=300)
    plt.legend(fontsize=250)

    plt.ylabel(r'$\frac{Time}{nParticles^2}$', fontsize=350)
    plt.tick_params(axis='x', which='major', pad=50)
    plt.xlabel(r"$Number\ of\ Particles\ Simulated(nParticles)$", fontsize=270)
    plt.title(r"$Compiler\ based\ Implementation$", fontsize=300)
    
    plt.tight_layout(pad=70.0)
    plt.savefig("performance_benchmarking")

if __name__ == "__main__":

    data_path = "data/table.csv"
    df = pd.read_csv(data_path)
    df = df.drop(['Unnamed: 0'], axis=1)
    df = df.T
    df.columns = ["NumPy", "Python", "C++", "Numba", "Pythran"]

    labels = df.columns
    names = ["16", "32", "64", "128"]

    df = df.T
    x = np.arange(len(df.columns))
    list_df = df[0:].to_numpy().tolist()

    plot(x, labels, list_df, names)

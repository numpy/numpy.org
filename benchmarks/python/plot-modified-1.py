import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def main(x, labels):

    fig, ax = plt.subplots()

    #figure(figsize=(20, 5), dpi=80)
    width = 0.17
    j = 0
    rect = [0, 0, 0, 0, 0]#, 0]

    for i in _list_df:
        rect[j] = plt.bar(x - width*j, i, width, align='center', label = labels[j])
        ax.bar_label(rect[j], padding=3)
        j += 1

    plt.title('Performance Comparision')
    plt.xlabel('Datasets')
    plt.ylabel('Time (s)')

    ax.set_xticks(x)
    ax.set_xticklabels(df.columns)

    plt.grid(True)
    plt.legend()

    fig.tight_layout()
    plt.savefig("output-modify-2-new.jpg")


if __name__ == "__main__":

    df = pd.read_csv("iter_6-b.csv")

    df = df.drop(['Unnamed: 0'], axis = 1)

    df = df.T

    df.columns = ["Pythran", "Numba", "Pythran Naive", "NumPy", "Pure NumPy"]#, "Pythran Opti"]

    labels = []
    for i in range(len(df.columns)):
        labels.append(df.columns[i])
    #print(labels)

    df = df.T
    x = np.arange(len(df.columns))
    _list_df = df[0:].to_numpy().tolist()

    main(x, labels)


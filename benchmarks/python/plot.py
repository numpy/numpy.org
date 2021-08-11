import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_graph(x, labels, list_df, names):
    
    plt.figure(figsize=(20, 10), dpi=500)
    width = 0.15
    rect = [0, 0, 0, 0, 0, 0]
    
    # Iterating through one type of implementation
    x_indices = []
    for ind, time_taken in enumerate(list_df):
        rect[ind] = plt.bar(x + width * ind, time_taken, width, align='center', label = labels[ind])
        x_indices.append(
            x + width * ind
        )
        plt.bar_label(rect[ind], padding=3)

    per_dataset = [np.array(list_df)[:, ind] for ind in range(len(list_df[0]))]
    per_indices = [np.array(x_indices)[:, ind] for ind in range(len(x_indices[0]))]
    new_x = np.array([0, 1, 2, 3, 4, 5])

    colors = np.random.rand(6)
    for ind, val in enumerate(per_dataset):
        indices = per_indices[ind]
        plt.scatter(
            indices, val, s = 20, c = colors
        )
        plt.plot(
            indices, val, c = 'black'
        )

    plt.title('Performance Comparision; Number of iterations: 5')
    plt.xlabel('Number of Particles Simulated(nParticles)')
    plt.ylabel('Time / (nParticles **2)')

    plt.xticks(x + width * 2, names)

    plt.legend()
    plt.show()
    plt.savefig("NumPy-Benchmarking.png")


if __name__ == "__main__":
    df = pd.read_csv("data.csv")
    df = df.drop(['Unnamed: 0'], axis = 1).T
    df.columns = ["Python-NumPy", "Pure-NumPy", "Pure-Python", "C++", "Numba", "Pythran-Naive: Transonic Jit"]

    labels = df.columns
    names = ["16", "32", "64", "128"]

    df = df.T
    x = np.arange(len(df.columns))
    list_df = df[0:].to_numpy().tolist()

    plot_graph(x, labels, list_df, names)

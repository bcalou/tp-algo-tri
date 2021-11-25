import matplotlib.pyplot as plt

# Use matplotlib to input and organize data in a graph
def plot_graph(entries, time_per_entry, file_name):
    plt.plot(entries, time_per_entry, 'ro')
    plt.xlabel("Nombre d'entrées")
    plt.ylabel("Temps d'exécution (en s)")
    plt.axis([1, max(entries), 0, max(time_per_entry)])
    plt.savefig(file_name)
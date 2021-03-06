import matplotlib.pyplot as plt
import nsgaNet
import pareto_front
import random_pareto

''' 'NSGA-Net-crossover-0.1', 'NSGA-Net-crossover-0.5', 'NSGA-Net-crossover-1.0',
              'NSGA-Net-mutation-0.1', 'NSGA-Net-mutation-0.5', 'NSGA-Net-mutation-1.0' '''


def main():
    acc = {}
    time = {}

    acc['NSGA-Net'], time['NSGA-Net'] = nsgaNet.nsgaII()
    acc['Total-data'], time['Total-data'], acc['Answer'], time['Answer'] = pareto_front.pareto_front()
    acc['Random'], time['Random'] = random_pareto.random_pareto_front(40)

    labels = ['NSGA-Net', 'Total-data', 'Answer', 'Random']
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    colors = ['green', 'violet', 'steelblue', 'yellow']
    markers = ['o', 'x', '*', '^']

    for i, label in enumerate(labels):
        ax.scatter(time[label], acc[label], marker=markers[i], color=colors[i], label=label)

    ax.legend(loc='best')

    plt.tight_layout()
    plt.show()

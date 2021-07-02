import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def plot_complex():
    col = ["nbits", "tbits", "sec1", "p", "q", "sec2", "g"]
    data = np.genfromtxt("safe_prime_complex", names = col)
    plt.scatter(data['nbits'], data['sec2'], marker = '.', alpha = 0.3, label = 'Generator', color = 'r')
    plt.scatter(data['nbits'], data['sec1'], marker = '.', alpha = 0.5, label = 'Prime')
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f s'))
    plt.legend(loc = "upper left")
    plt.show()


def plot_variance():
    col = ["second", "tbits", 'index']
    data = np.genfromtxt("safe_prime_variance", names = col)
    plt.scatter(data['tbits'], data['second'], marker = '.', alpha = 0.5, label = 'Prime')
    plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f s'))
    plt.show()

plot_variance()
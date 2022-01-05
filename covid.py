import numpy as np
import matplotlib.pyplot as plt
import math

NUCLEOTIDES = ['a','c','g','t']

def load_genome_string(genome_file):
    genome = ''
    with open(genome_file) as file:
        for line in file.readlines():
            for letter in line:
                if letter in NUCLEOTIDES:
                    genome += letter
    return genome

def print_info(genome):
    # There are 4 nucleotides = 2 bits. 4 nucleotides = 8 bits = 1 byte.
    size_bytes = len(genome) / 4
    size_kb = size_bytes / 1024
    print('Loaded genome is', len(genome), 'nucleotides long =',
        "{:.2f}".format(size_kb), 'KiB')

def to_numpy_array(genome_string):
    side = int(math.ceil(math.sqrt(len(genome_string))))
    genome_array = np.zeros((side, side))
    for i in range(side):
        for j in range(side):
            index = i*side + j
            if index >= len(genome_string):
                break # The remaining ones are zeros.
            genome_array[i,j] = NUCLEOTIDES.index(genome_string[index])
    return genome_array

def plot_numpy_array(title, array):
    fig = plt.figure(figsize=(8,6))
    plt.imshow(array)
    plt.title(title)
    plt.show()

if __name__ == '__main__':
    genome_string = load_genome_string('covid_genome.txt')
    print_info(genome_string)
    plot_numpy_array('Covid genome', to_numpy_array(genome_string))
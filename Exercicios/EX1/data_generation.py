import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Essa função usa sementes que sempre irão gerar a mesma sequencia randomica.

# Médias e desvios para cada classe
means = [(2, 3), (5, 6), (8, 1), (15, 4)]
stds = [(0.8, 2.5), (1.2, 1.9), (0.9, 0.9), (0.5, 2)]

data = []
labels = []

for i in range(len(means)):
    mean = means[i]
    std = stds[i]

    x = np.random.normal(loc=mean[0], scale=std[0], size=100)
    y = np.random.normal(loc=mean[1], scale=std[1], size=100)

    # Agrupando os pontos em pares (x, y)
    points = []
    for j in range(100):
        points.append([x[j], y[j]])

    # Adiciona os pontos da classe atual à lista geral
    data.extend(points)

    # Adiciona os rótulos correspondentes
    for j in range(100):
        labels.append(i)

# Convertendo para arrays do numpy
data = np.array(data)
labels = np.array(labels)

print("Dados gerados:")
print(data)
#print(data[0:10])  # Mostra os primeiros 10 pontos
print("Rótulos correspondentes:")
print(labels)
#print(labels[0:10])  # Mostra os primeiros 10 rótulos

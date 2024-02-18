import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(30000)
    rw.fill_walk()
    plt.figure(figsize=(12, 7))
    plt.scatter(rw.x_values, rw.y_values, c=list(range(rw.num_points)), cmap=plt.cm.Greens, s=1)
    plt.scatter(0, 0, c='green', edgecolors='none', s=10)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=10)
    plt.show()
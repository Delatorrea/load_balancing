from load.core import Input, Cluster
from functools import reduce


if __name__ == '__main__':

    data = Input()
    cluster = Cluster(data.ttask, data.umax)

    for line in data.users:
        cluster.dimension(line)


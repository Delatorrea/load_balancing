from core.models import Input, Cluster
from functools import reduce


if __name__ == '__main__':

    data = Input()
    cluster = Cluster(data.ttask, data.umax)

    for line in data.users:
        cluster.dimension(line)





    #a = Server()
    #a.sum_usercount()
    #servers.append(a)
    #a.sum_usercount()
    # produto = reduce(lambda x, y: x.usercount + y.usercount, servers)
    #print(servers[0].usercount)
    #print(servers[1].usercount)

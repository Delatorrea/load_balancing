class Input:

    def __init__(self):
        self.archive = open('input.txt', 'r')
        self.list = self.archive.readlines()
        self.archive.close()
        self.ttask = None
        self.umax = None
        self.users = []
        self.get_all()

    @property
    def ttask(self):
        return self.__ttask

    @ttask.setter
    def ttask(self, value):
        if value:
            try:
                self.__ttask = int(value.replace('\n', ''))
            except Exception as e:
                raise Exception("ttask invalid\n"
                                "Error: {}.".format(e))

    @property
    def umax(self):
        return self.__umax

    @umax.setter
    def umax(self, value):
        if value:
            try:
                self.__umax = int(value.replace('\n', ''))
            except Exception as e:
                raise Exception("umax invalid\n"
                                "Error: {}.".format(e))

    def add_user(self, user):
        self.users.append(user)

    def get_all(self):
        self.ttask = self.list[0]
        self.umax = self.list[1]

        __line = 0
        __listSize = len(self.list) - 2
        while __line < __listSize:
            self.add_user(int(self.list[__line + 2].replace('\n', '')))
            __line += 1


class Cluster:

    def __init__(self, ttask, umax):
        self.ttask = ttask
        self.umax = umax
        self.server = None
        self.servers = []

    def add_server(self):
        self.server = Server()
        self.servers.append(self.server)

    def remove_server(self, server):
        self.servers.remove(server)

    def count_servers(self):
        return len(self.servers)

    def dimension(self, qtd_user):
        self.add_server()
        self.server.sum_usercount()
        server_available = self.get_server_available()
        if server_available is not None:
            user = User()
            server_available.add_user(user)



    def get_server_available(self):
        self.servers.sort(key=lambda x: x.usercount, reverse=True)
        servers_activate = list(filter(lambda x: x.active, self.servers))
        for server in servers_activate:
            if server.usercount < self.ttask:
                return server

        return None


class Server:

    def __init__(self):
        self.usercount = 0
        self.users = []
        self.price = 0
        self.active = True

    def sum_usercount(self):
        self.usercount += 1

    def add_user(self, user):
        self.sum_usercount()
        self.users.append(user)

    def remove_user(self, user):
        if self.count_users() > 0:
            self.users.remove(user)
            return True

        return False

    def count_users(self):
        self.usercount = len(self.users)
        return self.usercount

    def set_active(self):
        self.active = True

    def set_inactive(self):
        self.active = False

    def is_activate(self):
        return self.active

    def status(self):
        return self.active


class User:

    def __init__(self):
        self.ttask = 0

    def add_ttask(self):
        self.ttask += 1

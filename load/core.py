import os


class Input:

    def __init__(self):
        self.archive = open('input.txt', 'r')  # Arquivo input.txt iniciado
        self.list = self.archive.readlines()  # Conteúdo do arquivo carregado em lista
        self.archive.close()  # Arquivo fechado
        self.ttask = None  # Tempo que servidor leva para executar uma tarefa
        self.umax = None  # Limite de usuários que servidor comporta simultaneamente
        self.users = []  # Lista de usuários por tick
        self.get_all()  # Carrega dados do arquivo em seus respectivos atributos da classe

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


class Output:
    def __init__(self):
        if os.path.exists("output.txt"):
            os.remove("output.txt")

        self.archive = open('output.txt', 'w')  # Arquivo output.txt iniciado
        self.text = ''

    def save_archive(self):
        self.archive.writelines(self.text)

    def add_line(self, line):
        self.text = line


class Cluster:

    def __init__(self, ttask, umax):
        self.ttask = ttask  # Tempo que servidor leva para executar uma tarefa
        self.umax = umax  # Limite de usuários que servidor comporta simultaneamente
        self.price = 0  # Valor acumulado gerado pelos serviços executados nos servidores
        self.server = None  # Atributo recebe instância de Servidor
        self.servers = []  # Lista de Servidores no Cluster
        self.output = Output()  # Arquivo que irá receber todos os registros de saída

    def add_server(self):
        self.server = Server()
        self.servers.append(self.server)
        return self.server

    def remove_server(self, server):
        self.servers.remove(server)

    def get_servers_used(self):
        used = ''
        for server in self.servers:
            used += str(server.count_users()) + ', '

        self.output.add_line('\n' + used[:-2])
        self.output.save_archive()

    def add_price(self):
        self.price += 1

    def dimension(self, qtd_user):
        count = 0

        # Libera recurso já consumido
        self.release_resource()

        # TODO Remover contagem de ttask de dentro do loop. Quando não há novos usuários o ttask não é incrementado.

        # Pra cada usuário necessário verifica se há um servidor disponível e o provisiona caso não haja.
        while count < qtd_user:
            # Retorna um servidor disponível
            server_available = self.get_server_available()

            # Adiciona um novo usuário ao servidor
            user = User()
            server_available.add_user(user)

            count += 1
        self.get_servers_used()

    def get_server_available(self):
        # Ordena Servidores de forma decrescente por quantidade de usuários
        self.servers.sort(key=lambda x: x.usercount, reverse=True)

        # Filtra servidores ativos e que estejam com vaga disponível
        servers_active = list(filter(lambda x: x.active is True and (x.usercount < self.umax), self.servers))

        for server in servers_active:
            #
            for user in server.users:
                user.add_ttask()

            # Retorna primeiro servidor disponível encontrado
            return server

        # Caso não encontre servidores ativos Filtra servidores inativos, reativando-os para uso.
        servers_disabled = list(filter(lambda x: x.active is False and (x.usercount < self.umax), self.servers))

        for server in servers_disabled:
            # Ativa servidor encontrado
            server.set_active()

            # Retorna servidor reativado
            return server

        # Caso não encontre servidores disponíveis instancia um novo.
        return self.add_server()

    def release_resource(self):
        # Filtra servidores ativos
        servers_active = list(filter(lambda x: x.active is True, self.servers))

        for server in servers_active:
            for user in server.users:
                if user.ttask >= self.ttask:
                    server.remove_user(user)
            if server.count_users() == 0:
                server.set_inactive()


class Server:

    def __init__(self):
        self.usercount = 0
        self.users = []
        self.active = True

    def add_usercount(self):
        self.usercount += 1

    def subtract_usercount(self):
        if self.usercount > 0:
            self.usercount -= 1

    def add_user(self, user):
        self.add_usercount()
        self.users.append(user)

    def remove_user(self, user):
        if self.count_users() > 0:
            self.subtract_usercount()
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

    def time_task(self):
        pass


class User:

    def __init__(self):
        self.ttask = 0

    def add_ttask(self):
        self.ttask += 1

from input import Input
from output import Output


class Cluster:

    def __init__(self):
        self.input = Input()  # Arquivo com parâmetros do Cluster e usuários
        self.ttask = self.input.ttask  # Tempo que servidor leva para executar uma tarefa
        self.umax = self.input.umax  # Limite de usuários que servidor comporta simultaneamente
        self.price = 0  # Valor acumulado gerado pelos serviços executados nos servidores
        self.server = None  # Atributo recebe instância de Servidor
        self.servers = []  # Lista de Servidores no Cluster
        self.output = Output()  # Arquivo que irá receber todos os registros de saída

    def start(self):
        index = 0
        self.add_server()

        # Enquanto houver Servidor ativo os Ticks são consumidos
        while list(filter(lambda x: x.active is True, self.servers)).__len__() > 0:

            # Se houver usuários na lista passa como parâmetro caso contrário envia 0 (zero usários)
            if index >= self.input.users.__len__():
                self.dimension(0)
            else:
                self.dimension(self.input.users[index])

            index += 1

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

        # Adiciona 1 ttask ao usuário
        self.set_ttask_users()

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

        # Retorna primeiro servidor disponível encontrado
        if servers_active.__len__() > 0:
            return servers_active[0]

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

    def set_ttask_users(self):
        # Filtra servidores ativos e que estejam com vaga disponível
        servers_active = list(filter(lambda x: x.active is True and x.usercount <= self.umax, self.servers))

        # Adiciona 1 ttask ao usuário
        for server in servers_active:
            for user in server.users:
                user.add_ttask()


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

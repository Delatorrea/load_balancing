class Input:

    def __init__(self):
        self.archive = open('input.txt', 'r')  # Arquivo input.txt iniciado
        self.list = self.archive.readlines()  # Conteúdo do arquivo carregado em lista
        self.archive.close()  # Arquivo fechado
        self.ttask = None  # Tempo que servidor leva para executar uma tarefa
        self.umax = None  # Limite de usuários que servidor comporta simultaneamente
        self.qtd_users = []  # Lista de quantidade de usuários por tick
        self.user_index = 0  # index atual da lista de quantidade de usuários
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

    def add_qtd_user(self, qtd_user: int):
        self.qtd_users.append(qtd_user)

    def get_qtd_user(self) -> int:
        return self.qtd_users[self.get_index()]

    def get_all(self):
        self.ttask = self.list[0]
        self.umax = self.list[1]

        __line = 0
        __listSize = len(self.list) - 2
        while __line < __listSize:
            self.add_qtd_user(int(self.list[__line + 2].replace('\n', '')))
            __line += 1

    def get_index(self) -> int:
        return self.user_index

    def add_index(self):
        self.user_index += 1

    def get_count_list_user(self) -> int:
        return self.qtd_users.__len__()

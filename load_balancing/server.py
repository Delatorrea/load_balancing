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

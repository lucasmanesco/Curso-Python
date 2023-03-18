# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classmethod
# @ staticmethod - método estático (no self, no cls)


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x, y):
        return x + y


# c1 = Connection()
c1 = Connection.create_with_auth('lucasmanesco', '123456')
# c1.set_user('lucasmanesco')
# c1.set_password('123456')
print(c1.user)
print(c1.password)

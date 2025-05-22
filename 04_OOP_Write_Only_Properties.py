class User():
    def __init__(self, password):
        self.password = password

    @property
    def password(self):
        raise AttributeError('Password is write-only')

    @password.setter
    def password(self, plaintext):
        self._user_password = plaintext


u1 = User('password')
# print(u1.password)
u1.password = 'new password'

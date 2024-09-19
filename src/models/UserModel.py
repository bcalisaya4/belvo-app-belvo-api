class User():

    def __init__(self, email, password) -> None:
        print("User model")
        self.id = None
        self.email = email
        self.password = password
        self.fullname = None
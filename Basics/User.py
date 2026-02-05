class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    def say_hi_to_user(self, user):
        print(f"Message from {self.username}: Hi {user.username}, it's {self.username}!")

user1 = User("Rania", "rania@gmail.com", 123)
user2 = User("Ahmed", "ahmed@gmail.com", 246)

user1.say_hi_to_user(user2)
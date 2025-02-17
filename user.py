from werkzeug.security import generate_password_hash, check_password_hash
from collections import defaultdict

users_db = defaultdict(dict)


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.hash_password = generate_password_hash(password)
        users_db[self.name] = self 

    def verify_password(self, password):
        return check_password_hash(self.hash_password, password)


def verify_login(name, password):
    user = users_db.get(name)

    if user and user.verify_password(password):
        return True
    else:
        return False




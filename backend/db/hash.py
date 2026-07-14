import bcrypt

class Hash():
    def bcrypt(password: str):
        return bcrypt.hashpw(password)
    def verify(hashed_password, plain_password):
        return bcrypt.checkpw(plain_password, hashed_password)
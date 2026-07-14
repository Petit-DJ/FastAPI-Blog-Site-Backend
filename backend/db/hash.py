# import bcrypt


# class Hash():
#     def bcrypt(password: str):
#         return bcrypt.hashpw(
#             password.encode("utf-8"),
#             bcrypt.gensalt()
#         )
#     def verify(hashed_password, plain_password):
#         return bcrypt.checkpw(
#             plain_password.encode("utf-8"),
#             hashed_password.encode("utf-8")
#             )

import bcrypt

class Hash:

    @staticmethod
    def bcrypt(password: str):
        return bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
    @staticmethod
    def verify(hashed_password, plain_password):
        if isinstance(hashed_password, str):
            hashed = hashed_password.encode("utf-8")
        else:
            hashed = hashed_password
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed)
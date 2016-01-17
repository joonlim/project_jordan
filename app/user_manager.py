

class UserManager:
    """
    Manages user data.
    """
    def fake_user(self):
        """
        Return a fake user used for testing purposes.
        The user has a name and a hash.
        """
        return {
            "name": "joonkid",
            "hash": "21fe34e3887efecbc3b1f7272d6bb838eea17b3b",
            "players": [
                201939,
                203110,
                202355,
                203952,
                202738,
                201942,
                1717,
                203468,
                201152,
                101162,
                101114,
                201149,
                204001
            ]
        }

user_manager = UserManager()

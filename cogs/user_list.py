class UserList:
    user_list = []
    
    @classmethod
    def get_user_list(cls):
        return cls.user_list
    
    @classmethod
    def append_user(cls, user):
        cls.user_list.append(user)
    
    @classmethod
    def is_user_in_user_list(cls, user):
        return user in cls.user_list

    @classmethod
    def clear_user_list(cls):
        cls.user_list = []

    @classmethod
    def remove_user_from_user_list(cls, user):
        cls.user_list.remove(user)

class UserList:
    user_list = []
    tickets_created = 0
    
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

    @classmethod
    def get_counter_value(cls):
        return cls.tickets_created
    
    @classmethod
    def increment_counter(cls):
        cls.tickets_created += 1
    
    @classmethod
    def decrement_counter(cls):
        cls.tickets_created -= 1
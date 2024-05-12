class User():
    def __init__(self, id, name, access):
        self.__id = id
        self.__name = name
        self.__access = access

    def get_info(self):
        return self.__id, self.__name, self.__access


user1 = User('1', 'John', 'user')
user2 = User('2', 'Tom', 'user')
print(user1.get_info())
print(user2.get_info())


class Admin(User):
    def __init__(self, id, name, access, add_access):
        super().__init__(id, name, access)
        self.__add_access = add_access
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)


    def remove_user(self, user_to_remove):
        for user in self.__users:
            user_name = user.get_info()[1]
            if user_name == user_to_remove:
                self.__users.remove(user)
                print(f"{user_name} удален из списка")



admin = Admin('3', 'Leonardo', 'user', 'admin')
print(admin.get_info())
admin.add_user(user1)
admin.add_user(user2)
admin.remove_user('Tom')
admin.remove_user('John')

class User:
    

    def __init__(self, service_provider, username, password):

        '''
        __init__ method that helps us define properties for our objects.

        '''
        
        self.service_provider = service_provider
        self.username = username
        self.password = password

    user_list = []  # Empty user list    
    # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)    

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_user_by_username(cls,username):
        '''
        Method that takes in a service provider and returns a user that matches that service provider.
        '''

        for user in cls.user_list:
            if user.username == username:
                return user
    @classmethod
    def display_user(cls):
        """
        method that returns the class array
        """
        return cls.user_list            
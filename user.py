class User:
    
    
    def __init__(self,service_provider,user_name,user_password):

        '''
        __init__ method that helps us define properties for our objects.

        '''
        
        self.service_provider = service_provider
        self.user_name = user_name
        self.user_password = user_password
 # Init method up here
    user_list = []  # Empty user list
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
    def find_by_service_provider(cls,service_provider):
        '''
        Method that takes in a service provider and returns a user that matches that service provider.
        '''

        for user in cls.user_list:
            if user.service_provider == service_provider:
                return user    
class Account:
    
    user_list = []  # Empty user list
    def __init__(self,service_provider,user_name,user_password):

        '''
        __init__ method that helps us define properties for our objects.

        '''
        
        self.service_provider = service_provider
        self.user_name = user_name
        self.user_password = user_password
 # Init method up here
    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Account.user_list.append(self)

    def delete_user(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Account.user_list.remove(self)

    @classmethod
    def find_by_service_provider(cls,service_provider):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for user in cls.user_list:
            if user.service_provider == service_provider:
                return user    
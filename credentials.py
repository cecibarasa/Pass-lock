class Credentials:

    '''
    The class that generates the credentials for the user
    '''

    credentials_list = []

    def __init__(self, service_provider, username, password):
        self.service_provider = service_provider
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        Save user credentials into the list
        '''
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        Returns the credential list
        '''    
        return cls.credentials_list
import unittest
from credentials import Credentials
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credentials("service_provider", "username", "password")

    def tearDown(self):
        '''
        Method that cleans up after each method is run
        '''
        Credentials.credentials_list = []

    def test_init(self):
        """
        test_init test case to test if the object is properly initialized
        """
        self.assertEqual(self.new_credential.service_provider, "service_provider")
        self.assertEqual(self.new_credential.username, "username")
        self.assertEqual(self.new_credential.password, "password")

    def save_credentials(self):
        """
        test_save_cred test case to test if the credential object is saved into
         the credentials list
        """
        self.new_credential.save_credentials()  # save the new credential
        self.assertEqual(len(Credentials.credentials_list), 1)

    def display_credentials(self):
        """
        method that returns a list of saved credentials
        """
        self.assertEqual(Credentials.display_credentials(), Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()                
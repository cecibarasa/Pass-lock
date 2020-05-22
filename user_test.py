import unittest  #Import unittest module
import random  # for pass generator
from user import Account


class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = Account("Instagram","James", "0875345") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.service_provider,"Instagram")
        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.user_password, "0875345")
        
    def save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(Account.user_list), 1)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.user_list = []

# other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_user()
            test_user = Account("Test","user","0712345678") # new contact
            test_user.save_user()
            self.assertEqual(len(Account.user_list), 2)
            
    def test_delete_user(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_user.save_user()
            test_user = Account("Test","user","0712345678") # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(Account.user_list),1)        

    def test_find_contact_by_service_provider(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = Account("Test","user","0711223344") # new contact
        test_user.save_user()

        found_user = Account.find_by_service_provider("Test")

        self.assertEqual(found_user.service_provider,test_user.service_provider)


if __name__ == '__main__':
    unittest.main()
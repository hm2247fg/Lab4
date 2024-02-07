import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError


class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [testPhone1, testPhone2]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order. (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)

    def test_create_and_add_phone_with_duplicate_id(self):
        # Modified PhoneAssignments.add_phone() to make this test pass

        # Create an instance of PhoneAssignments
        testAssignmentMgr = PhoneAssignments()

        # Add the first phone
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')

        # Attempt to add a second phone with the same ID (expecting a PhoneError)
        with self.assertRaises(PhoneError) as e:
            testPhone2 = Phone(1, 'Apple', 'iPhone 5')
            self.assertEqual(str(e.exception), "Phone with same id already exists")

        # Ensure that the first phone was successfully added
        self.assertIn(testPhone1, testAssignmentMgr.phones)

        # Ensure that the second phone was not added due to the PhoneError
        with self.assertRaises(AttributeError):
            self.assertNotIn(testPhone2, testAssignmentMgr.phones)


    def test_create_and_add_new_employee(self):
        # Create an instance of PhoneAssignments
        testAssignmentMgr = PhoneAssignments()

        # Create two employees
        testemployee1 = Employee(101, 'John Doe')
        testemployee2 = Employee(102, 'Jane Smith')

        # Create a list of expected employees
        testemployees = [testemployee1, testemployee2]

        # Add employees to testAssignmentMgr
        testAssignmentMgr.add_employee(testemployee1)
        testAssignmentMgr.add_employee(testemployee2)

        # Ensure that the employees were successfully added
        self.assertEqual(testemployees, testAssignmentMgr.employees)

        # remove the self.fail() statement
        # self.fail()

    def test_create_and_add_employee_with_duplicate_id(self):

        # Fixed the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id

        # Create an instance of PhoneAssignments
        testAssignmentMgr = PhoneAssignments()

        # Create the first employee
        testEmployee1 = Employee(101, 'John Doe')

        # Attempt to create a second employee with the same ID (expecting a PhoneError)
        with self.assertRaises(PhoneError) as e:
            testEmployee2 = Employee(101, 'Jane Smith')
            self.assertEqual(str(e.exception), "Employee with same id already exists")

        # Ensure that the first employee was successfully added
        self.assertIn(testEmployee1, testAssignmentMgr.employees)

        # Ensure that the second employee was not added due to the PhoneError
        with self.assertRaises(AttributeError):
            self.assertNotIn(testEmployee2, testAssignmentMgr.employees)

        # Removed the self.fail() statement
        # self.fail()

    def test_assign_phone_to_employee(self):
        # Fixed the assign method in PhoneAssignments
        testPhone = Phone(1, 'Apple', 'iPhone 6')
        testEmployee = Employee(101, 'John Doe')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)

        testAssignmentMgr.assign(testPhone, testEmployee)

        self.assertEqual(testAssignmentMgr.get_phone(testPhone.id), testPhone)

        # Removed the self.fail() statement
        # self.fail()

    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # Fixed the assign method in PhoneAssignments so it throws an exception if the phone is already assigned.
        testPhone = Phone(1, 'Apple', 'iPhone 6')
        testEmployee1 = Employee(101, 'John Doe')
        testEmployee2 = Employee(102, 'Jane Smith')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee1)
        testAssignmentMgr.add_employee(testEmployee2)

        testAssignmentMgr.assign(testPhone.id, testEmployee1)

        # If a phone is already assigned to an employee, PhoneError raised to assign it to a different employee.
        with self.assertRaises(PhoneError) as e:
            testAssignmentMgr.assign(testPhone.id, testEmployee2)
            self.assertEqual(str(e.exception), "Phone is already assigned to Employee")

        # Removed the self.fail() statement
        # self.fail()

    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Samsung', 'Galaxy S10')
        testEmployee = Employee(101, 'John Doe')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)
        testAssignmentMgr.add_employee(testEmployee)

        testAssignmentMgr.assign(testPhone1.id, testEmployee)

        # Fixed the assign method in PhoneAssignments, so it raises a PhoneError if the phone is already assigned.
        with self.assertRaises(PhoneError) as e:
            testAssignmentMgr.assign(testPhone2.id, testEmployee)
            self.assertEqual(str(e.exception), "Employee already has a phone")

        # Removed the self.fail() statement
        # self.fail()

    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        testPhone = Phone(1, 'Apple', 'iPhone 6')
        testEmployee = Employee(101, 'John Doe')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)

        # Assign the phone initially
        testAssignmentMgr.assign(testPhone.id, testEmployee)

        # Reassigning should not raise a PhoneError if a phone is assigned to the same user
        # it is currently assigned to and should not make any changes
        testAssignmentMgr.assign(testPhone.id, testEmployee)

        # Verify that the assignment is still the same
        self.assertEqual(testAssignmentMgr.get_phone(testPhone.id), testPhone)

        # Removed the self.fail() statement
        # self.fail()

    def test_un_assign_phone(self):
        testPhone = Phone(1, 'Apple', 'iPhone 6')
        testEmployee = Employee(101, 'John Doe')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)

        # Assign the phone initially
        testAssignmentMgr.assign(testPhone.id, testEmployee)

        # Unassign the phone
        testAssignmentMgr.un_assign(testPhone.id)

        # Verify that the employee_id is None after unassigning
        self.assertIsNone(testAssignmentMgr.get_phone(testPhone.id).employee_id)

        # Removed the self.fail() statement
        # self.fail()

    def test_get_phone_info_for_employee(self):
        testPhone = Phone(1, 'Apple', 'iPhone 6')
        testEmployee = Employee(101, 'John Doe')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone)
        testAssignmentMgr.add_employee(testEmployee)

        # Assign the phone initially
        testAssignmentMgr.assign(testPhone.id, testEmployee)

        # Get phone info for the assigned employee
        phone_info = testAssignmentMgr.phone_info(testEmployee)

        # Verify correct phone info is returned
        self.assertEqual(phone_info, testPhone)

        # Unassign the phone
        testAssignmentMgr.un_assign(testPhone.id)

        # Get phone info for the unassigned employee, should return None
        phone_info_unassigned = testAssignmentMgr.phone_info(testEmployee)

        # method returns None if the employee does not have a phone
        self.assertIsNone(phone_info_unassigned)

        # Method raises an PhoneError if the employee does not exist
        with self.assertRaises(PhoneError) as e:
            non_existent_employee = Employee(102, 'Jane Smith')
            testAssignmentMgr.phone_info(non_existent_employee)
            self.assertEqual(str(e.exception), "Employee does not exist")

        # Removed the self.fail() statement
        # self.fail()


if __name__ == '__main__':
    unittest.main()
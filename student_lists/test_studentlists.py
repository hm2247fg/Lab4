from studentlists import ClassList, StudentError
import unittest


class TestStudentLists(unittest.TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)

    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')

    # Test that adds and removes a student, and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)

    # Test that adds some example students, then removes a student not in the list,
    # and asserts a StudentError is raised
    def test_add_remove_student_not_in_list(self):
        # Arrange
        class_list = ClassList(3)
        class_list.add_student('Alice')
        class_list.add_student('Bob')
        class_list.add_student('Charlie')

        # Act and Assert
        with self.assertRaises(StudentError):
            class_list.remove_student('David')

    # Test that removes a student from an empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_list(self):
        # Arrange
        class_list = ClassList(5)

        # Act and Assert
        with self.assertRaises(StudentError):
            class_list.remove_student('Alice')

    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))

    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))

    # Test that adds some example students to a test class, then, call is_enrolled for a student who is not enrolled.
    # Use assertFalse to verify is_enrolled returns False.
    def test_is_enrolled_for_non_enrolled_student(self):
        # Arrange
        class_list = ClassList(3)
        class_list.add_student('Alice')
        class_list.add_student('Bob')
        class_list.add_student('Charlie')

        # Act
        result = class_list.is_enrolled('David')

        # Assert
        self.assertFalse(result)

    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))

    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))

    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))

    # Test for index_of_student when the class_list list is empty.
    # Assert index_of_student returns None for a student if the list is empty.
    # use assertIsNone.
    def test_index_of_student_empty_list(self):
        # Arrange
        class_list = ClassList(5)

        # Act
        result = class_list.index_of_student('Alice')

        # Assert
        self.assertIsNone(result)

    # Test for index_of_student. In the case when the class_list is not empty but has some students.
    # Assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_non_empty_list(self):
        # Arrange
        class_list = ClassList(5)
        class_list.add_student('Alice')
        class_list.add_student('Bob')
        class_list.add_student('Charlie')

        # Act
        result_alice = class_list.index_of_student('Alice')
        result_bob = class_list.index_of_student('Bob')
        result_charlie = class_list.index_of_student('Charlie')
        result_nonexistent = class_list.index_of_student('David')

        # Assert
        self.assertEqual(result_alice, 1)
        self.assertEqual(result_bob, 2)
        self.assertEqual(result_charlie, 3)
        self.assertIsNone(result_nonexistent)

    # Test for your new is_class_full method when the class is full.
    # use assertTrue.
    def test_is_class_full_full_class(self):
        # Arrange
        class_list = ClassList(3)
        class_list.add_student('Alice')
        class_list.add_student('Bob')
        class_list.add_student('Charlie')

        # Act
        result = class_list.is_class_full()

        # Assert
        self.assertTrue(result)

    # Test for your new is_class_full method for when is empty, and when it is not full.
    # Use assertFalse.
    def test_is_class_full_empty_class(self):
        # Arrange
        class_list = ClassList(5)

        # Act
        result = class_list.is_class_full()

        # Assert
        self.assertFalse(result)

    def test_is_class_full_not_full_class(self):
        # Arrange
        class_list = ClassList(3)
        class_list.add_student('Alice')
        class_list.add_student('Bob')

        # Act
        result = class_list.is_class_full()

        # Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
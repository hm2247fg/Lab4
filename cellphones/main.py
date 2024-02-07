from phone_manager import Phone, Employee, PhoneAssignments


def main():
    # Create an instance of PhoneAssignments
    assignments = PhoneAssignments()

    # Create three phones
    phone1 = Phone(1, 'Samsung', 'Galaxy Note 7')
    phone2 = Phone(2, 'Samsung', 'Galaxy S III')
    phone3 = Phone(3, 'Samsung', 'Galaxy A7')

    # Add phones to assignments
    assignments.add_phone(phone1)
    assignments.add_phone(phone2)
    assignments.add_phone(phone3)

    # Create three employees
    employee1 = Employee(1, 'Alice')
    employee2 = Employee(2, 'Bill')
    employee3 = Employee(3, 'Ted')

    # Add employees to assignments
    assignments.add_employee(employee1)
    assignments.add_employee(employee2)
    assignments.add_employee(employee3)

    # Assign phones to employees
    assignments.assign(phone1.id, employee2)  # Assign phone 1 to employee 2
    assignments.assign(phone2.id, employee3)  # Assign phone 2 to employee 3

    # Print phone information for employees
    print(assignments.phone_info(employee1))  # Employee 1, no phone. Prints None
    print(assignments.phone_info(employee2))  # Employee 2, has Phone 1
    print(assignments.phone_info(employee3))  # Employee 3 has Phone 2

    # Unassign phone 2 from employee 3
    assignments.un_assign(phone2.id)          # un-assign phone 2 (which belonged to employee 3)
    print(assignments.phone_info(employee3))  # None

    assignments.assign(phone3.id, employee3)   # Assign phone 3 to employee 3

    try:
        # Try to assign phone 2 to employee 3 again (should raise an exception)
        # employee3 should not be able to have two phones
        assignments.assign(phone2.id, employee3)
    except Exception as e:
        print(f"Assignment Error: {e}")


if __name__ == '__main__':
    main()

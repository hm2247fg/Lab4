"""Demonstration of a phone management system using classes that  simulates a basic phone management
system where phones can be assigned and unassigned to employees, and information about phone assignments
can be queried."""

# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones


class Phone:
    phone_registry = {}

    def __init__(self, id, make, model):
        if id in Phone.phone_registry:
            raise PhoneError("Phone with the same ID already exists")

        self.id = id
        self.make = make
        self.model = model
        self.employee_id = None
        Phone.phone_registry[id] = self

    def assign(self, employee_id):
        self.employee_id = employee_id

    def is_assigned(self):
        return self.employee_id is not None

    def __str__(self):
        return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model,
                                                                              self.employee_id)


class Employee:
    employee_registry = {}

    def __init__(self, id, name):
        if id in Employee.employee_registry:
            raise PhoneError("Employee with same id already exists")
        self.id = id
        self.name = name
        Employee.employee_registry[id] = self

    def __str__(self):
        return 'ID: {} Name {}'.format(self.id, self.name)


class PhoneAssignments():

    def __init__(self):
        self.phones = []
        self.employees = []

    def add_employee(self, employee):
        # Check if an employee with the same ID already exists
        # Raise exception if two employees with same ID are added
        if any(existing_employee.id == employee.id for existing_employee in self.employees):
            raise PhoneError("Employee with same ID already exists!")

        # If no duplicate ID is found, add the new employee
        self.employees.append(employee)

    def add_phone(self, phone):
        # Check if a phone with the same ID already exists
        # Raise exception if two phones with same ID are added
        if any(existing_phone.id == phone.id for existing_phone in self.phones):
            raise PhoneError("Phone with same ID already exists!")

        # If no duplicate ID is found, add the new phone
        self.phones.append(phone)

    def assign(self, phone_id, employee):
        # Find phone in phones list
        # If phone is already assigned to an employee, do not change list, raise exception
        for phone in self.phones:
            if phone.id == phone_id:
                if phone.employee_id is not None:
                    raise PhoneError("Phone is already assigned to Employee!")

        # If employee already has a phone, do not change list, and raise exception
        for phone in self.phones:
            if phone.employee_id == employee:
                raise PhoneError("Employee already has a phone!")

        # If employee already has this phone, don't make any changes. This should NOT raise an exception
        for phone in self.phones:
            if phone.id == phone_id:
                if phone.employee_id == employee:
                    pass

        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(employee.id)
                return

    def un_assign(self, phone_id):
        # Find phone in list, set employee_id to None
        for phone in self.phones:
            if phone.id == phone_id:
                phone.assign(None)  # Assign to None

    def phone_info(self, employee):
        # Find phone for employee in phones list
        # Should return None if the employee does not have a phone
        for phone in self.phones:
            if phone.employee_id != employee.id:
                return None

        # Method should raise an exception if the employee does not exist
        if employee not in self.employees:
            raise PhoneError("Employee does not exist")

        for phone in self.phones:
            if phone.employee_id == employee.id:
                return phone

        return None

    def get_phone(self, ph):
        for phone in self.phones:
            if phone.id == ph:
                return phone


class PhoneError(Exception):
    pass

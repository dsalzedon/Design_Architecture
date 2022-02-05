import copy


class Address:
    def __init__(self, street_address, city, suite) -> None:
        self.city = city
        self.street_address = street_address
        self.suite = suite

    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.suite}"


class Employee:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address("London Road 123", "London", 0))
    aux_office_employee = Employee("", Address("London Road 124B", "London", 0))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


john = EmployeeFactory.new_main_office_employee("John", 50)
dan = EmployeeFactory.new_main_office_employee("Dan", 101)
ivan = EmployeeFactory.new_aux_office_employee("Ivan", 33)

print(ivan)
print(john)
print(dan)

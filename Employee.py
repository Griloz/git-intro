
# create class
class Employee:

    # create class attribute/variable
    vacation_days = 10


# create an object/instance from the class
Mike = Employee()
Jane = Employee()


print(f'Vacation days of Mike is {Mike.vacation_days}')
print(f'Vacation days of Jane is {Jane.vacation_days}')

# change oblect sttribute value
Jane.vacation_days = 20
Jane.is_manager = True
print(Jane.is_manager)

# change class sttribute value
Employee.vacation_days = 12


print(f'Vacation days of Mike is {Mike.vacation_days}')
print(f'Vacation days of Jane is {Jane.vacation_days}')

print(id(Mike.vacation_days))
print(id(Jane.vacation_days))

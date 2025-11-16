class Employee:
    def __init__(self, f_name, l_name,):
        self.f_name = f_name
        self.l_name = l_name
class SalaryEmployee(Employee):
    def __init__(self, f_name, l_name, salary):
        super().__init__(f_name, l_name)
        self.salary = salary
    def calculate_salary(self):
        return self.salary/52
class HourlyEmployee(Employee):
    def __init__(self, f_name, l_name, hourly_income, hour_worked):
        super().__init__(f_name, l_name)
        self.hourly_income = hourly_income
        self.hour_worked = hour_worked
    def calculate_salary(self):
        return self.hourly_income * self.hour_worked
class Commission_Employee(SalaryEmployee):
    def __init__(self, f_name, l_name, commission_rate, commission_completed, salary):
        super().__init__(f_name, l_name, salary)
        self.c_rate = commission_rate
        self.c_c = commission_completed
    def calculate_salary(self):
        regular = super().calculate_salary()
        commission = self.c_rate * self.c_c
        return regular + commission
class Company:
    def __init__(self):
        self.employees = []
    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    def display_employee(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.f_name, i.l_name)
        print('----------------------------------------')
    def paycheck_salary(self):
        for i in self.employees:
            print('The paycheck of employee: ' + i.f_name + ' ' + i.l_name + ' is $' + str(i.calculate_salary()))
        print('----------------------------------------')

#Main Program
def main():
    try: 
        number = int(input('Please enter a number of new Employees!\n'))

        my_company = Company()
        for i in range(number): 
            fname = input('Enter employee first name:\n')
            lname = input('Enter employee last name:\n')
            salary_type = input('Pls enter the paycheck type: Monthly, Hourly, or Commission?\n')
            if salary_type == 'Monthly':
                salary = int(float(input("Please enter the employee's yearly salary:\n")))
                if salary <= 0:
                    raise ValueError('Pls enter a valid salary!')
                employee = SalaryEmployee(fname, lname, salary)
                my_company.add_employee(employee)
            
            elif salary_type == 'Hourly':
                hourly_income = int(float((input('Pls enter the hourly income:\n'))))
                if hourly_income <= 0:
                    raise ValueError('Pls enter a valid salary!')
                hour_worked = int(float((input('Pls enter the hour that the employee had worked in a year:\n'))))
                if hour_worked <= 0:
                    raise ValueError('Pls enter a valid hour!')
                employee = HourlyEmployee(fname, lname, hourly_income, hour_worked)
                my_company.add_employee(employee)
            
            elif salary_type == 'Commission':
                salary = int(float(input("Please enter the employee's yearly salary:\n")))
                commision_rate = int(float((input('Pls enter the commision rate:\n'))))
                if commision_rate <= 0:
                    raise ValueError('Pls enter a valid rate!')
                commision_completed = int(float((input('Pls enter the completed Commission!\n'))))
                if commision_completed <= 0:
                    raise ValueError('Pls enter a valid commision completed')
                employee = Commission_Employee(fname, lname, commision_rate, commision_completed, salary) # type: ignore
                my_company.add_employee(employee)
            
            else:
                print('Pls check again your spelling or input the right type of salary!')
            
        my_company.display_employee()
        my_company.paycheck_salary()
    except:
        print('Pls enter a valid number')

main()
#Autor: Long Vien 
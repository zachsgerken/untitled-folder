#Zach Gerken
#Chapter 11 Lab 1
#November 17 2022


def employee_salesperson_path():
    employee_type = 'go on'
    while employee_type != 'q' and employee_type != 'Q':
        employee_type = input('Do you wish to enter the data for an (E)mployee, a (S)alesperson or would you like to (Q)uit? ')
        if employee_type == ('e'):
            employee = employee('joe bob', 25, 20)
            name1 = input('Enter the name of the employee: ')
            employee.set_name(name1)
            print('Enter', name1, "'s hourly pay rate", sep='', end="")
            pay_rate1 = float(input(': '))
            employee.set_pay_rate(pay_rate1)
            print('Enter the number of hours worked by', name1, end="")
            hours1 = int(input(': '))
            employee.set_hours(hours1)

            print('\nEmployee data: ')
            print('Employee name: ', employee.get_name())
            print('Employee hourly pay rate: $', format(employee.get_pay_rate(), '.2f'))
            print('Hours worked: ', employee.get_hours())
            print('Pay: $', format(employee.calc_pay(), '.2f'))

        elif employee_type == 's':
            sales_employee = salesperson('joe bob',26, 21, 100, .5)
            name2 = input('Enter the name of the employee: ')
            sales_employee.set_name(name2)
            print('Enter', name2, "'s hourly pay rate", sep='', end="")
            pay_rate2 = float(input(': '))
            sales_employee.set_pay_rate(pay_rate2)
            print('Enter the number of hours worked by', name2, end="")
            hours2 = int(input(': '))
            employee.set_hours(hours2)
            print('Enter amount of sales made by', name2, end="")
            sales_amount = float(input(': '))
            sales_employee.set_amount(sales_amount)
            print('Enter the commission percentage that will be earned by', name2, end="")
            commission_percentage = float(input(': '))
            sales_employee.set_percentage(commission_percentage)

            print('\nEmployee data: ')
            print('Employee name: ', sales_employee.get_name())
            print('Employee hourly pay rate: $', format(sales_employee.get_pay_rate(), '.2f'))
            print('Hours worked: ', sales_employee.get_hours())
            print('Sales: $', format(sales_employee.get_amount(), '.2f'))
            print('Commission percentage: $', format(sales_employee.get_percentage(), '.2f'))
            print('Pay: $', format(sales_employee.calc_pay(), '.2f'))

employee_salesperson_path()














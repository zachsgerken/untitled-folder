#Zach Gerken
#Chapter 11 Lab 2
#November 17 2022

import employee

def employee_salesperson_path():
    employee_salesperson = input('Do you wish to enter the data for an (E)mployee, a (S)alesperson or would you like to (Q)uit? ')
    if employee_salesperson == ('e'):
        employee()
    elif employee_salesperson == ('s'):
        salesperson()
    elif employee_salesperson == ('q'):
        quit()
    else:
        print("Invalid Entry Try Again")
        employee_salesperson_path()

def employee():
    import employee

    name1 = input('Enter the name of the employee: ')

    pay_rate1 = float(input(f'Enter {name1}\'s hourly pay rate: '))

    hours1 = float(input(f'Enter the number of hours worked by {name1}: '))

    pay1 = employee.calc_pay()


    myEmployee = employee.Employee(name1, pay_rate1, hours1, pay1)

    myEmployee.set_name(name1)
    myEmployee.set_pay_rate(pay_rate1)
    myEmployee.set_hours(hours1)
    myEmployee.calc_pay(pay1)


    print()
    print(f'Employee data:\nEmployee name: {pay1}\nEmployee hourly pay rate: ${pay_rate1:.2f}\nHours worked: {hours1:.0f}')







def salesperson():
    import employee

    name1 = input('Enter the name of the employee: ')

    hours1 = float(input(f'Enter the number of hours worked by {name1}: '))

    pay_rate1 = float(input(f'Enter {name1}\'s hourly pay rate: '))

    sales1 = input(f'Enter the amount of sales made by {name1}: ')

    comm1 = float(input(f'Enter the commmission percentage that will be earned by {name1}: '))

    calc_sales1 = hours1 * pay_rate1


    myEmployee = employee.Employee(name1, hours1, pay_rate1, pays)
    mySalesperson = employee.Salesperson(name1, hours1, pay_rate1, calc_pay1, sales1, comm1, calc_sales1)

    myEmployee.set_name(name1)
    myEmployee.set_pay_rate(pay_rate1)
    myEmployee.set_hours(hours1)
    myEmployee.set_calc_pay(calc_pay1)
    mySalesperson.set_name(name1)
    mySalesperson.set_hours(hours1)
    mySalesperson.set_pay_rate(pay_rate1)
    mySalesperson.set_calc_pay(calc_pay1)
    mySalesperson.set_sales(sales1)
    mySalesperson.set_comm(comm1)
    mySalesperson.set_calc_sales(calc_sales1)

    print()
    print(f'Employee data:\nEmployee name: {name1}\nEmployee number: {number1}\nEmployee shift: {shift1}\nEmployee pay rate: ${pay_rate1:.2f}')



def quit():
    pass


def main():
    employee_salesperson_path()


if __name__ == '__main__':
    main()

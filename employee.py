#Zach Gerken
#Chapter 11 Lab 2
#November 17 2022
#name, hours worked and hourly rate
class Employee:

    def __init__(self, name, hours, pay_rate):
        self._name = name
        self._hours = hours
        self._pay_rate = pay_rate
        self._calc_pay = calc_pay

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_hours(self, hours):
        self._hours = hours

    def get_hours(self):
        return self._hours

    def set_pay_rate(self, pay_rate):
        self._pay_rate = pay_rate

    def get_pay_rate(self):
        return self._pay_rate

    def set_calc_pay(self):
        self._calc_pay = float(self.get_hours()) * float(self._get_pay_rate())

    def calc_pay(self):
        return self._calc_pay


class Salesperson(Employee):
    def __init__(self, name, hours, pay_rate, week, comm):
        Employee.__init__(self, name, hours, pay_rate)
        self._week = week
        self._comm = comm

    def set_week(self, week):
        self._week = week

    def get_week(self):
        return self._week

    def set_comm(self, comm):
        self._comm = comm

    def get_comm(self):
        return self._comm

    def calc_sales(self):
        employeepay = Employee.calc_pay(self)
        employeepay += float(self._week) * float(self._comm)
        return employeepay


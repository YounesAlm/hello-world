#!/usr/bin/python
# -*- coding: utf-8 -*-

class Employee:
    num_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'
        Employee.num_emp +=1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



print(Employee.num_emp)
emp1 = Employee( 'Youn', 'Bouchib', 50)
print(emp1.fullname())
print(Employee.num_emp)
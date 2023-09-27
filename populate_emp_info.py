import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','drf_curd_all_pagination_11.settings')
                      
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *


# Create an instance of Faker
fakegen=Faker()

def populate(n):
    for _ in range(n):
        feno = randint(1, 999)
        fname = fakegen.name()
        fsal = randint(10000, 250000)
        faddress = fakegen.address()
        employee, created = Employee.objects.get_or_create(
            eno=feno, ename=fname, esal=fsal, eaddr=faddress
        )
        if created:
            print(f'Created Employee: {employee}')


try:
    n = int(input('Enter total number of records you want to generate: '))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        populate(n)
        print(f'{n} number of records generated successfully.')
except ValueError:
    print("Invalid input. Please enter a positive integer.")

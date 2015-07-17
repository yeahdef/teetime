from django.contrib import admin
from teetime.models import Product, Category, Feature, Job, Client, State, Department, Employee
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(Job)
admin.site.register(Client)
admin.site.register(State)
admin.site.register(Department)
admin.site.register(Employee)
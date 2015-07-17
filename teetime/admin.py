from django.contrib import admin
from teetime.models import Product, Category, Feature, Job, Client, JobState, Department, Employee
# Register your models here.


class ProductInline(admin.TabularInline):
    model = Product


class JobInline(admin.TabularInline):
    model = Job


class EmployeeInline(admin.TabularInline):
    model = Employee


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'job', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductInline]

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'name']


class JobAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'open_date', 'client']


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'address', 'email']
    inlines = [JobInline]


class JobStateAdmin(admin.ModelAdmin):
    list_display = ['name']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [EmployeeInline]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'department']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(JobState, JobStateAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
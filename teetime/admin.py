from django.contrib import admin
from teetime.models import Product, Category, Feature, Job, Client, JobState, Department, Employee
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class FeatureAdmin(admin.ModelAdmin):
    pass


class JobAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


class JobStateAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(JobState, JobStateAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
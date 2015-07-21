from django.contrib import admin
from teetime.models import Product, Category, Feature, Job, Client, JobState, Department, Employee, Lot
# Register your models here.


class ProductInline(admin.TabularInline):
    model = Product


class LotInline(admin.TabularInline):
    model = Lot


class JobInline(admin.TabularInline):
    model = Job


class EmployeeInline(admin.TabularInline):
    model = Employee


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'lot', ]


class LotAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ProductInline]

class FeatureAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'name']


class JobAdmin(admin.ModelAdmin):
    list_display = ['pk', 'state', 'open_date', 'client']
    inlines = [LotInline]


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
    def user_first_name(obj):
        return obj.user.first_name

    def user_last_name(obj):
        return obj.user.last_name

    list_display = ['user', user_first_name, user_last_name, 'department']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Lot, LotAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(JobState, JobStateAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
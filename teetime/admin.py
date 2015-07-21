from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
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
    can_delete = False


class UserInline(admin.TabularInline):
    model = User


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


class UserAdmin(admin.ModelAdmin):
    inlines = [EmployeeInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Lot, LotAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
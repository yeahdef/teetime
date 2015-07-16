from django.contrib import admin
from teetime.models import Product, Category, Feature, Job, Client, State
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Feature)
admin.site.register(Job)
admin.site.register(Client)
admin.site.register(State)
from django.contrib import admin

# Register your models here.
from .models import Category, Classification, Activity, Methods

admin.site.register(Category)
admin.site.register(Classification)
admin.site.register(Activity)
admin.site.register(Methods)
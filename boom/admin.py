from django.contrib import admin

# Register your models here.
from .models import bloger
from .models import product


admin.site.register(bloger)
admin.site.register(product)
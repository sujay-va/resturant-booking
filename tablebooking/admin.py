from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Dishes)
admin.site.register(Resttab)
admin.site.register(OrdersDish)
admin.site.register(BookTable)

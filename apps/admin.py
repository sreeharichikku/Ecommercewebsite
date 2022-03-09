from django.contrib import admin
from .models import contacts
from .models import Productss
from .models import cart

# Register your models here.
admin.site.register(contacts)
admin.site.register(Productss)
admin.site.register(cart)

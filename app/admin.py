from django.contrib import admin

from .models import Employee
from .models import Person
from .models import Profile
from .models import Fueltype
from .models import Cartype

# Register your models here.
admin.site.register([Employee])
admin.site.register([Person])
admin.site.register([Profile])
admin.site.register([Fueltype])
admin.site.register([Cartype])

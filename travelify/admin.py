from django.contrib import admin
from .models import Testimony
from .models import Ifem
from .models import Place

# Register your models here.

admin.site.register(Testimony)
admin.site.register(Ifem)
admin.site.register(Place)
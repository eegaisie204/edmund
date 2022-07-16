from django.contrib import admin
from .models import Destination
from .models import Experience
from .models import Testimony

# Register your models here.
admin.site.register(Destination)
admin.site.register(Experience)
admin.site.register(Testimony)
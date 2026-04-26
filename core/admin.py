from django.contrib import admin

# Register your models here.
from .models import TeamMember, Department

admin.site.register(TeamMember)
admin.site.register(Department)
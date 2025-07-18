from django.contrib import admin
from .models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'joined_date')
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

admin.site.register(Members, MemberAdmin)

from django.contrib import admin

from app.models import  field_name

# Register your models here.
class appAdmin(admin.ModelAdmin):
        
    list_display=['name_field_value_x','name_field_value_y']

admin.site.register(field_name,appAdmin)
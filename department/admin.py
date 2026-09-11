from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'department_number',
        'short_name',
        'name',
    )

    search_fields = (
        'department_number',
        'short_name',
        'name',
    )
  

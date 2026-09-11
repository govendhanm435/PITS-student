from django.contrib import admin
from .models import Subject, Mark


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject_code',
        'subject_name',
        'semester',
    )

    search_fields = (
        'subject_code',
        'subject_name',
    )

    list_filter = (
        'semester',
    )


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'internal_mark',
        'external_mark',
        'total_mark',
        'grade',
        'result',
    )

    search_fields = (
        'student__register_number',
        'student__name',
        'subject__subject_code',
        'subject__subject_name',
    )

    list_filter = (
        'subject__semester',
        'result',
        'grade',
    )

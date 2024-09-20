from django.contrib.admin import ModelAdmin, register
from .models import *


@register(Teacher)
class TeacherAdmin(ModelAdmin):
    pass


@register(Student)
class StudentAdmin(ModelAdmin):
    pass

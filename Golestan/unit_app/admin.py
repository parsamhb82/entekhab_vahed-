from .models import *
from django.contrib.admin import ModelAdmin,register

@register(Lesson)
class LessonAdmin(ModelAdmin):
    pass


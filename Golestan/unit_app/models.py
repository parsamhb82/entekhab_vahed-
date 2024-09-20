from django.db import models


class Lesson(models.Model):
    unit = models.IntegerField()
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    class_day = models.IntegerField() # 0 to 4, From Saturday To Wednesday
    major = models.CharField(max_length=50)
    teacher = models.ForeignKey('user_app.Teacher', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

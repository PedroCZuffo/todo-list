import uuid
from django.db import models

class Task(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    finished = models.BooleanField(default=False)
    due_date = models.DateField()
    chart = models.ForeignKey('chart.Chart', related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    # subtask
    # tag
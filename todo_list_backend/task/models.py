import uuid
from django.db import models
from todo_list_backend.chart import Chart

class Task(models.Model):
    uuid = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=30)
    description = models.CharField()
    finished = models.BooleanField(default=False)
    expected_date = models.DateField()
    chart = models.ForeignKey(Chart, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    # subtask
    # tag
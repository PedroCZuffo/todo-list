from rest_framework import serializers
from .models import Chart
from task.serializers import TaskSerializer

class ChartSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Chart
        fields = '__all__'

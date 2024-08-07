from rest_framework import viewsets
from .models import Chart
from .serializers import ChartSerializer

class ChartViewSet(viewsets.ModelViewSet):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from tasks.models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getData(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
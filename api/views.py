from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TaskSerializer, RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .models import Task


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',

        'token': '/token/',
        'token refresh': '/token/refresh/',

        'create user': '/user/create/',
    }

    return Response(api_urls)


@api_view(['POST'])
def userCreate(request):
    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    user = User.objects.get(username=serializer.data['username'])
    refresh = RefreshToken.for_user(user)

    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskList(request):
    user = request.user
    tasks = user.task_set.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def taskDetail(request, pk):
    user = request.user
    try:
        tasks = user.task_set.get(id=pk)
    except Task.DoesNotExist:
        return Response('You are not authorized to view this task!')

    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def taskCreate(request):
    user = request.user
    request.data['user'] = user.id

    if request.data['priority'] not in ['low', 'medium', 'high']:
        return Response('Invalid priority!')

    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def taskUpdate(request, pk):
    user = request.user
    try:
        task = user.task_set.get(id=pk)
    except Task.DoesNotExist:
        return Response('You are not authorized to update this task!')
    request.data['user'] = user.id

    if request.data['priority'] not in ['low', 'medium', 'high']:
        return Response('Invalid priority!')

    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    user = request.user
    try:
        task = user.task_set.get(id=pk)
    except Task.DoesNotExist:
        return Response('You are not authorized to delete this task!')

    task.delete()

    return Response('Item successfully delete!')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

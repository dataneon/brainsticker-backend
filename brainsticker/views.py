from django.http import HttpResponse
from rest_framework import generics
from .models import CustomUser, Canvas, Note
from .serializers import UserSerializer, CanvasSerializer, NoteSerializer
from brainsticker import serializers


# Shows that the server is running
def main_view(request):
    return HttpResponse("Main route works!")

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# canvas list
class CanvasList(generics.ListCreateAPIView):
    queryset = Canvas.objects.all()
    serializer_class = CanvasSerializer


# canvas detail
class CanvasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Canvas.objects.all()
    serializer_class = CanvasSerializer


# note list
class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


# note detail
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

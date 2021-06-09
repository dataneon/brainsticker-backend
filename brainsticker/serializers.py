from django.db.models.base import Model
from rest_framework.serializers import ModelSerializer

from .models import CustomUser, Canvas, Note

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'last_login', 'date_joined', 'is_staff')


class CanvasSerializer(ModelSerializer):

    canvas_url = ModelSerializer.serializer_url_field(
        view_name = 'canvas_detail'
    )

    class Meta:
        model = Canvas
        fields = ('user', 'canvas_name', 'canvas_url',)


class NoteSerializer(ModelSerializer):

    note_url = ModelSerializer.serializer_url_field(
        view_name = 'note_detail'
    )

    class Meta:
        model = Note
        fields = ('canvas', 'content', 'note_url',)

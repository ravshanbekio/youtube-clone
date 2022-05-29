from rest_framework.serializers import ModelSerializer
from .models import User, Playlist, Video, Comment, Channel

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ChannelSerializer(ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
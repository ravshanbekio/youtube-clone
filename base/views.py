from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import PlaylistSerializer, UserSerializer, VideoSerializer, CommentSerializer, ChannelSerializer
from .models import User, Playlist, Video, Comment, Channel
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.generics import get_object_or_404
from rest_framework.throttling import ScopedRateThrottle

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'

    @action(detail=True, methods=["GET"])
    def playlists(self, request, pk):
        user = User.objects.get(id=pk)
        playlists = Playlist.objects.filter(user=user)
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def videos(self, request, pk):
        user = User.objects.get(id=pk)
        videos = Video.objects.filter(video_user=user)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id','name','age','country','city','username',]

class ChannelViewSet(ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'

    @action(detail=True, methods=["GET"])
    def videos(self, request, pk):
        playlist = Playlist.objects.get(id=pk)
        videos = Video.objects.filter(video_user=playlist)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id','playlist_name','playlist_text','playlist_date',]

class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'

    @action(detail=True, methods=["GET"])
    def comments(self, request, pk):
        video = Video.objects.get(id=pk)
        comments = Comment.objects.filter(video=video)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id','video_name','video_date',]

    def retrieve(self, request, pk=None,*args, **kwargs):
        queryset = Video.objects.all()
        video = get_object_or_404(queryset, pk=pk)
        video.video_views += 1
        video.save()
        serializer = VideoSerializer(video)
        return Response(serializer.data)

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'base'
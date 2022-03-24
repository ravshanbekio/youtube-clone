from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.PositiveSmallIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100,blank=True, null=True)
    age = models.IntegerField()
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    playlist_name = models.CharField(max_length=110)
    playlist_text = models.TextField(max_length=300)
    playlist_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.playlist_name

class Video(models.Model):
    video_name = models.CharField(max_length=130)
    video_text = models.TextField(max_length=1000)
    video_views = models.PositiveSmallIntegerField(default=0)
    video_date = models.DateTimeField(auto_now_add=True)
    video_user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_playlist = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True, blank=True)
    video = models.URLField()

    def __str__(self):
        return self.video_name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=300)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        self.comment_text
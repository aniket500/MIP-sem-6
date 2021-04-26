from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

    
class Community(models.Model):
    title =  models.CharField(max_length=100,unique=True)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Community, on_delete= models.CASCADE,null=True, blank=True)
    reports = models.ManyToManyField(User, related_name='blog_post')
    likes = models.ManyToManyField(User, related_name='likes')
    User.username = 'Viraj'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    #this is like a foriegn key that connects the comment model to post model
    name = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.post.title)

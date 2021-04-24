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
    reports= models.ManyToManyField(User, related_name='blog_post')
    User.username = 'Viraj' 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
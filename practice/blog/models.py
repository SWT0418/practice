from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post_id = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    reg_date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content

class Hashtag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
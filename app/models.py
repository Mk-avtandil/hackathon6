from django.db import models

class News(models.Model):
    CHOICES = (
        ('Travel', 'Travel'),
        ('LifeStyle', 'LifeStyle'),
        ('Healthy', 'Healthy'),
        ('Food', 'Food'))
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.FileField(upload_to='media/%Y/%m/%d')
    created = models.DateTimeField(auto_now_add=True)
    view_post = models.IntegerField()
    choice = models.CharField(max_length=255, choices=CHOICES)
    author = models.CharField(max_length=255)
    like = models.IntegerField()

    def __str__(self):
        return self.title


class PostComment(models.Model):
    CHOICES = (('like', 'like'),('dislike', 'dislike'))
    username = models.CharField(max_length=255)
    like = models.TextField(choices=CHOICES)
    comment = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE)
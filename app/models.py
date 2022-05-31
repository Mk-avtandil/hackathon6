from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    CHOICES = (
        ('Travel', 'Travel'),
        ('LifeStyle', 'LifeStyle'),
        ('Healthy', 'Healthy'),
        ('Food', 'Food'))
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    view_post = models.IntegerField(blank=True, default='0')
    choice = models.CharField(max_length=255, choices=CHOICES)
    author = models.CharField(max_length=255)
    like = models.IntegerField(default='0')
    tags = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class PostComment(models.Model):
    class Meta:
        verbose_name_plural = "Комменты и лайки"
        
    CHOICES = (('like', 'like'),('dislike', 'dislike'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.CharField(max_length=255, blank=True, choices=CHOICES)
    comment = models.TextField(blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Contact(models.Model):
    class Meta:
        verbose_name_plural = "Контакты"

    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,blank=True)
    message = models.TextField(max_length=2555, blank=True)

    def __str__(self):
        return self.subject


class Video(models.Model):
    class Meta:
        verbose_name_plural = "Видео"

    videofile = models.FileField(upload_to='media/%Y/%m/%d')
    title = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Email(models.Model):
    mail = models.EmailField(blank=True)


class Service(models.Model):
    class Meta:
        verbose_name_plural = "Сервисы"

    type = models.CharField(max_length=255)
    price = models.IntegerField()
    analytics_count = models.IntegerField()
    change_count = models.IntegerField()
    social_media = models.CharField(max_length=255)
    count_of_optimization = models.IntegerField()
    support = models.CharField(max_length=255)

    def __str__(self):
        return self.type 
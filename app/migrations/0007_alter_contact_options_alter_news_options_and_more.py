# Generated by Django 4.0.4 on 2022-05-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_news_like_alter_postcomment_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='postcomment',
            options={'verbose_name_plural': 'Комменты и лайки'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': 'Видео'},
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.FileField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='news',
            name='view_post',
            field=models.IntegerField(blank=True, default='0'),
        ),
    ]
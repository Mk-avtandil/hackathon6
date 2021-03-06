# Generated by Django 4.0.4 on 2022-05-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_email_alter_postcomment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('analytics_count', models.IntegerField()),
                ('change_count', models.IntegerField()),
                ('social_media', models.CharField(max_length=255)),
                ('count_of_optimization', models.IntegerField()),
                ('support', models.CharField(max_length=255)),
            ],
        ),
    ]

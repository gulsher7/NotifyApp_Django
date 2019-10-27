# Generated by Django 2.2.6 on 2019-10-27 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('user_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=50)),
                ('user_phone', models.CharField(max_length=50)),
                ('user_desc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=2000)),
                ('pic', models.ImageField(blank=True, upload_to='post_image')),
                ('tdate', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-04-17 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_userinfo_des'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_img',
            field=models.CharField(default='default.jpg', max_length=100),
        ),
    ]

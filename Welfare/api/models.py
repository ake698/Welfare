from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user_type_choice = (
        (1, "普通用户"),
        (2, "管理员"),
    )
    user_type = models.IntegerField(choices=user_type_choice, default=1)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_img = models.CharField(max_length=100, default="default.jpg")
    create_time = models.DateTimeField(auto_now_add=True, blank=True)


class UserToken(models.Model):
    user = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)


class Organization(models.Model):
    name = models.CharField(max_length=32)
    des = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)


class Activity(models.Model):
    name = models.CharField(max_length=32)
    des = models.CharField(max_length=2000)
    sponsor = models.ForeignKey(Organization, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)


class Applicant(models.Model):
    status = (
        (1, "申请中"),
        (2, "已同意"),
        (3, "已拒绝"),
    )
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status, default=1)
    create_time = models.DateTimeField(auto_now_add=True)


class Resource(models.Model):
    name = models.CharField(max_length=32)
    link = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)


class MessageBoard(models.Model):
    content = models.CharField(max_length=200)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    reply = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import *


class UserInfoSerializer(ModelSerializer):
    # 显示多选字段的字段备注
    user_type_name = serializers.CharField(source="get_user_type_display", required=False, read_only=True)
    user_type = serializers.IntegerField(required=False)
    password = serializers.CharField(max_length=32, min_length=6, required=False)
    user_img = serializers.CharField(max_length=100, required=False)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = UserInfo
        fields = "__all__"
        # exclude = ["password", ]
        read_only_fields = ("id","username",)


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
        read_only_fields = ("id",)


class ActivitySerializer(ModelSerializer):
    status_name = serializers.CharField(source="get_status_display", required=False)
    sponsor_name = serializers.CharField(source="sponsor.name", read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    class Meta:
        model = Activity
        fields = "__all__"
        read_only_fields = ("id",)


class ApplicantSerializer(ModelSerializer):
    status_name = serializers.CharField(source="get_status_display", required=False)
    user_name = serializers.CharField(source="user.username", read_only=True)
    activity_name = serializers.CharField(source="activity.name", read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    class Meta:
        model = Applicant
        fields = "__all__"
        read_only_fields = ("id","create_time")
        # write_only_fields = ("user","activity")


class ResourceSerializer(ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    class Meta:
        model = Resource
        fields = "__all__"
        read_only_fields = ("id",)


class MessageBoardSerializer(ModelSerializer):
    user_img = serializers.CharField(source="user.user_img", read_only=True)
    user_name = serializers.CharField(source="user.username", read_only=True)
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    activity_name = serializers.CharField(source="activity.name", read_only=True)
    class Meta:
        model = MessageBoard
        fields = "__all__"
        read_only_fields = ("id",)

from django.contrib import admin
from django.contrib.auth.models import User, Group
from api.models import *
# Register your models here.

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "user_type", "username", "password", "create_time")
    list_editable = ("user_type",)


class OrgAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "des")

class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sponsor", "create_time")

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Organization, OrgAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_header = "商城管理"
admin.site.site_title = "商城管理"
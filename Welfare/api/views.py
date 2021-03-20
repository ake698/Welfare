from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from api.serializers import *
from api.util.Authtication import *
from api.util.APIResponse import *
# from api.util.MyPagination import PageNumberPagination

# Create your views here.

#拦截器 用于检测用户是否为管理员
def check(group):
    def decorator(func):
        def wra(self, request,*arg,**kwargs):
            identity = request.user.user_type
            if not identity or int(identity) not in group:
                return Response(error("没有权限访问"))
            return func(self, request,*arg,**kwargs)
        return wra
    return decorator


class AuthView(APIView):
    def post(self, request):
        ret = {}
        try:
            user = request.data["username"]
            pwd = request.data["password"]
            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                return Response(error("账号密码错误！"))
            token = md5(user)
            UserToken.objects.update_or_create(user=obj, defaults={"token": token})
            ret["token"] = token
            ret["avatar"] = obj.user_img
            ret["user_type"] = obj.user_type
        except Exception as et:
            return Response(error("账号密码错误！"))
        return Response(success(ret))


class UserView(APIView):
    def get(self, request):
        users = UserInfo.objects.all()
        ser = UserInfoSerializer(instance=users, many=True)
        return Response(success(ser.data))

    def post(self, request):
        datas = request.data
        username = datas["username"]
        password = datas["password"]
        if not (username and password):
            return Response(error("账号密码不能为空！"))
        if UserInfo.objects.filter(username=username):
            return Response(error("该账号已存在！"))
        UserInfo.objects.create(username=username, password=password)
        return Response(success(datas))

    def put(self, request):
        data = request.data
        user = request.user
        if "oldpassword" in data.keys():
            print(data["oldpassword"], user.password)
            if data["oldpassword"] != user.password:
                return Response(error("账号密码错误！"))
        ser = UserInfoSerializer(instance=user, data=request.data, many=False)
        if ser.is_valid():
            ser.save()
            return Response(success(ser.data))
        else:
            return Response(error(ser.errors))


class UserViewPK(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request, id):
        user = UserInfo.objects.filter(id=id).first()
        ser = UserInfoSerializer(instance=user, many=False)
        return Response(success(ser.data))

    def put(self, request, id):
        user = UserInfo.objects.filter(id=id).first()
        ser = UserInfoSerializer(instance=user, data=request.data, many=False)
        if ser.is_valid():
            ser.save()
            return Response(success(ser.data))
        else:
            return Response(error(ser.errors))

    @check([2,])
    def delete(self, request, id):
        user = UserInfo.objects.filter(id=id)
        user.delete()
        return Response(success())


class OrgView(APIView):
    authentication_classes = [Authtication, ]
    def get(self, request):
        orgs = Organization.objects.all()
        ser = OrganizationSerializer(instance=orgs, many=True)
        return Response(success(ser.data))

    @check([2, ])
    def post(self, request):
        datas = request.data
        ser = OrganizationSerializer(data=datas)
        if ser.is_valid():
            ser.save()
        return Response(success(ser.data))


class OrgViewPK(APIView):
    authentication_classes = [Authtication, ]
    def get(self, request, pk):
        org = Organization.objects.filter(id=pk).first()
        ser = OrganizationSerializer(instance=org, many=False)
        return Response(success(ser.data))

    @check([2, ])
    def put(self, request, pk):
        org = Organization.objects.get(id=pk)
        ser = OrganizationSerializer(instance=org, data=request.data, many=False)
        if ser.is_valid():
            ser.save()
            return Response(success(ser.data))
        else:
            return Response(error(ser.errors))

    @check([2, ])
    def delete(self, request, pk):
        org = Organization.objects.filter(id=pk)
        org.delete()
        return Response(success())


class ActivityView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request):
        acts = Activity.objects.all().order_by("-id")
        page = PageNumberPagination()
        page_list = page.paginate_queryset(acts, request, view=self)
        ser = ActivitySerializer(instance=page_list, many=True)
        return Response(success_list(ser.data, acts.count(), page.page.number))

    @check([2, ])
    def post(self, request):
        datas = request.data
        ser = ActivitySerializer(data=datas)
        if ser.is_valid():
            ser.save()
        else:
            error_msg = format_error_msg(ser.errors)
            return Response(error(error_msg))
        return Response(success(ser.data))
    

class ActivityPKView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request, id):
        act = Activity.objects.filter(id=id).first()
        ser = ActivitySerializer(instance=act, many=False)
        return Response(success(ser.data))

    @check([2, ])
    def put(self, request, id):
        act = Activity.objects.filter(id=id).first()
        ser = ActivitySerializer(instance=act, data=request.data, many=False)
        if ser.is_valid():
            ser.save()
            return Response(success(ser.data))
        else:
            return Response(error(ser.errors))

    @check([2, ])
    def delete(self, request, id):
        act = Activity.objects.filter(id=id)
        act.delete()
        return Response(success())
    
    
class ApplicantView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request):
        apps = Applicant.objects.all().order_by("-id")
        if request.user.user_type == 1:
            apps = apps.filter(user=request.user)
        ser = ApplicantSerializer(instance=apps, many=True)
        return Response(success(ser.data))

    def post(self, request):
        activity_id = request.data["activity"]
        apps = Applicant.objects.filter(activity_id=activity_id).filter(user=request.user)
        if apps.count() > 0:
            return Response(error("您已经报名！"))
        datas = request.data
        datas["user"] = request.user.id
        ser = ApplicantSerializer(data=datas)
        if ser.is_valid():
            ser.save()
        else:
            error_msg = format_error_msg(ser.errors)
            return Response(error(error_msg))
        return Response(success(ser.data))


class ApplicantPKView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request, id):
        app = Applicant.objects.filter(id=id).first()
        ser = ApplicantSerializer(instance=app, many=False)
        return Response(success(ser.data))

    @check([2, ])
    def put(self, request, id):
        app = Applicant.objects.filter(id=id)
        try:
            status = request.data["status"]
        except:
            return Response(error("请填写status参数!"))
        app.update(status=status)
        return Response(success("更新成功！"))

    def delete(self, request, id):
        app = Applicant.objects.filter(id=id)
        app.delete()
        return Response(success())


class MessageBoardView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request):
        apps = MessageBoard.objects.all().order_by("-id")
        if request.user.user_type == 1:
            apps = apps.filter(user=request.user)
        data = request.query_params
        if "activity_id" in data.keys():
            apps = apps.filter(activity__id=int(data["activity_id"]))
        ser = MessageBoardSerializer(instance=apps, many=True)
        return Response(success(ser.data))

    def post(self, request):
        datas = request.data
        datas["user"] = request.user.id
        ser = MessageBoardSerializer(data=datas)
        if ser.is_valid():
            ser.save()
        else:
            error_msg = format_error_msg(ser.errors)
            return Response(error(error_msg))
        return Response(success(ser.data))


class MessageBoardPKView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request, id):
        app = MessageBoard.objects.filter(id=id).first()
        ser = MessageBoardSerializer(instance=app, many=False)
        return Response(success(ser.data))

    def put(self, request, id):
        app = MessageBoard.objects.filter(id=id).first()
        ser = MessageBoardSerializer(instance=app, data=request.data, many=False)
        if ser.is_valid():
            ser.save()
            return Response(success(ser.data))
        else:
            return Response(error(ser.errors))

    def delete(self, request, id):
        app = MessageBoard.objects.filter(id=id)
        app.delete()
        return Response(success())


class ResourceView(APIView):
    authentication_classes = [Authtication, ]

    def get(self, request):
        resources = Resource.objects.all().order_by("-id")
        ser = ResourceSerializer(instance=resources, many=True)
        return Response(success(ser.data))

    @check([2, ])
    def post(self, request):
        data = request.data
        ser = ResourceSerializer(data=data)
        if ser.is_valid():
            ser.save()
        else:
            error_msg = format_error_msg(ser.errors)
            return Response(error(error_msg))
        return Response(success(ser.data))


class ResourcePKView(APIView):
    authentication_classes = [Authtication, ]
    def get(self,request, id):
        resource = Resource.objects.filter(id=id)
        return Response(success(resource.first().link))


    def delete(self, request, id):
        resource = Resource.objects.filter(id=id)
        resource.delete()
        return Response(success())


class FileUpload(APIView):
    authentication_classes = [Authtication, ]

    def post(self, request):
        file_up = request.FILES.get('files')
        is_img = False
        if file_up != None and file_up != "":
            from Welfare.settings import MEDIA_ROOT
            import os, time
            filesp = file_up.name.split(".")
            fileType = filesp[-1]
            if (fileType in ["jpg", "png", "jpeg"]):
                is_img = True
            filesp.pop(-1)
            fileName = "%s_%s.%s" % ("".join(filesp), int(round(time.time() * 1000)), fileType)
            f = open(os.path.join(MEDIA_ROOT, "", fileName), 'wb')
            for chunk in file_up.chunks():
                f.write(chunk)
            f.close()
        if is_img:
            user = UserInfo.objects.get(id=request.user.id)
            user.user_img = fileName
            user.save()
        import json
        return HttpResponse(json.dumps(success({"file_path": fileName})), content_type="application/json")

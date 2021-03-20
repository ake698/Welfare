from rest_framework import status
from rest_framework.templatetags import rest_framework


def success(args=None):
    return {
        "status": status.HTTP_200_OK,
        "msg": "操作成功！",
        "detail":args
    }


def success_list(detail, count, index=1):
    return {
        "status": status.HTTP_200_OK,
        "msg": "操作成功！",
        "total":count,
        "pageIndex":index,
        "detail": detail
    }

def error(args, msg="操作异常", ):
    return {
        "status": status.HTTP_200_OK,
        "msg":msg,
        "detail":args
    }


def error(msg="操作失败",):
    return {
        "status": status.HTTP_400_BAD_REQUEST,
        "msg": msg,
        "detail": ""
    }


def format_error_msg(msg):
    key = [i for i in msg.keys()][0]
    return key + " " + msg[key][0]
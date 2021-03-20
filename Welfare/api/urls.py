from django.urls import path,re_path
from api import views

urlpatterns = [
    path("user", views.UserView.as_view()),
    path("login", views.AuthView.as_view()),
    re_path("user/(\d+)", views.UserViewPK.as_view()),
    path("org", views.OrgView.as_view()),
    re_path("org/(\d+)", views.OrgViewPK.as_view()),
    path("activity", views.ActivityView.as_view()),
    re_path("activity/(\d+)", views.ActivityPKView.as_view()),
    path("applicant", views.ApplicantView.as_view()),
    re_path("applicant/(\d+)", views.ApplicantPKView.as_view()),
    path("message", views.MessageBoardView.as_view()),
    re_path("message/(\d+)", views.MessageBoardPKView.as_view()),
    path("resource", views.ResourceView.as_view()),
    re_path("resource/(\d+)", views.ResourcePKView.as_view()),
]
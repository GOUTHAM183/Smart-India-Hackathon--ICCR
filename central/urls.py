from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView,
    PostCreateView,
    UserPostListView,
)

urlpatterns = [
    path("", views.landing, name="landing"),
    path("home/", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("regional/", views.regional, name="regional"),
    path("iccr/", views.iccr, name="iccr"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("usersrofile/", views.usersprofile, name="usersprofile"),
    path("pages-faq/", views.pagesfaq, name="pages-faq"),
    path("contact/", views.contact, name="contact"),
    path("landing/", views.landing, name="landing"),




]

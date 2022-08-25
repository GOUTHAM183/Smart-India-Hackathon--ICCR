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
    path("landing/", views.landing, name="landing"),



    path("about/", views.about, name="about"),
    path("regional/", views.regional, name="regional"),
    path("iccr/", views.iccr, name="iccr"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),

    path("usersprofile/", views.usersprofile, name="usersprofile"),
    # path("helpdesk/", 'helpdesk/', name="helpdesk"),
    # path("studentProfile/", views.studentprofile, name="studentProfile"),
    # path("activityList/", views.activityList, name="activityList"),
    #path("budgetAnalytics/", views.budgetAnalytics, name="budgetAnalytics"),
    #path("quaterly/", views.quaterly, name="quaterly"),
    #path("yearly/", views.yearly, name="yearly"),
    #path("stats/", views.stats, name="stats"),
    #path("scholarships/", views.scholarships, name="scholarships"),
    #path("roForm/", views.roForm, name="roForm"),

    #path("gallery/", views.gallery, name="gallery"),
    #path("team/", views.team, name="team"),
    #path("contact/", views.contact, name="contact"),
    #path("pages-faq/", views.pagesfaq, name="pages-faq"),


    path("pages-faq/", views.pagesfaq, name="pages-faq"),
    path("contact/", views.contact, name="contact"),
    path("landing/", views.landing, name="landing"),
    path("raisetickets/", views.raisetickets, name="raisetickets"),
    path("studentprofile/", views.studentprofile, name="studentprofile"),
    path("activitylist/", views.activitylist, name="activitylist"),
    path("budgetanalytics/", views.budgetanalytics, name="budgetanalytics"),
    path("quarterly/", views.quarterly, name="quarterly"),




]

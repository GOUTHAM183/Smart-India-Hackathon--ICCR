from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    CreateView,
    DetailView,
)
from .models import Post


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "central/home.html", context)


def regional(request):
    return render(request, "central/regional.html", {})


def iccr(request):
    return render(request, "central/ICCRDash.html", {})


def index(request):
    return render(request, "central/index.html", {})

def landing(request):
    return render(request, "central/landing.html", {})


def about(request):
    return render(request, "central/about.html", {"title": "About"})


def usersprofile(request):
    return render(request, "central/usersProfile.html", {})


def pagesfaq(request):
    return render(request, "central/pages-faq.html", {})


def contact(request):
    return render(request, "central/contact.html", {})


def landing(request):
    return render(request, "central/landing.html", {})






class PostListView(ListView):
    model = Post
    template_name = "central/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class UserPostListView(ListView):
    model = Post
    template_name = "central/user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

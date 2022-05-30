from unicodedata import category
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from rest_framework import generics
from .serializers import *
from .models import *
from .forms import *



def index(request):
    video_post = Video.objects.first()
    popular_post = News.objects.all().order_by('-like').first()
    if News.objects.count() >= 3:
        three_popular_post = News.objects.all().order_by('-view_post')[:3]
        three_post = News.objects.all().order_by('view_post')[:3]
    else:
        three_popular_post = News.objects.all()
        three_post = News.objects.all()

    context = {
        'popular_post': popular_post,
        'three_post': three_post,
        'video_post': video_post,
        'three_popular_post': three_popular_post
    }
    return render(request, 'index.html', context=context)


def about(request):
    video_post = Video.objects.first()
    popular_post = News.objects.all().order_by('-like').first()
    context = {'popular_post': popular_post, 'video_post': video_post,}
    return render(request, 'about.html', context=context)


def blog(request):
    video_post = Video.objects.first()
    category_post = request.GET.get('categories')
    print(category_post)
    if category_post in (None, 'AllCategories'):
        posts = News.objects.all()
    else:
        posts = News.objects.filter(choice=category_post)
    context = {'posts': posts, 'video_post': video_post,}
    return render(request, 'blog.html', context=context)


def blog_details(request, pk):
    video_post = Video.objects.first()
    popular_post = News.objects.order_by('-created')[:3]
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostCommentForm()
    post = News.objects.get(pk=pk)
    context = {
        'post': post,
        'form': form,
        'video_post': video_post,
        'popular_post': popular_post
    }
    return render(request, 'blog-details.html', context=context)


def service(request):
    video_post = Video.objects.first()
    if News.objects.count() >= 3:
        three_popular_post = News.objects.all().order_by('-view_post')[:3]
    else:
        three_popular_post = News.objects.all()
    context = {'three_popular_post': three_popular_post, 'video_post': video_post,}
    return render(request, 'service.html', context=context)


def contact(request):
    video_post = Video.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,
                  'contact.html',
                  context={'form': form, 'video_post': video_post,})


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsDetailSerializers


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializers


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializers


class VideoCreateView(generics.CreateAPIView):
    serializer_class = VideoDetailSerializers


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializers


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializers


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')

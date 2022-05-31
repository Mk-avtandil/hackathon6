from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from rest_framework import generics
from django.core.mail import send_mail
from django.core.paginator import Paginator
from app.forms import EmailForm
from .serializers import *
from .models import *
from .forms import *


def index(request):
    services = Service.objects.all()
    video_post = Video.objects.order_by('?').first()
    tags = News.objects.values_list('tags').distinct()
    popular_post = News.objects.order_by('-like').first()
    if News.objects.count() >= 3:
        three_popular_post = News.objects.order_by('-view_post')[:3]
        three_post = News.objects.order_by('view_post')[:3]
    else:
        three_popular_post = News.objects.all()
        three_post = News.objects.all()

    if request.method == 'POST':
        if 'mail' in request.POST:
            form = EmailForm(request.POST)
            mail = request.POST['mail']
            send_mail(
                'Ваша почту одобрена!!!',
                'Поздравляем ваша почта успешно потдверждена.',
                'seogram2022@gmail.com',
                [mail],
                fail_silently=False)
            if form.is_valid():
                form.save()
    form = EmailForm()

    context = {
        'popular_post': popular_post,
        'three_post': three_post,
        'video_post': video_post,
        'three_popular_post': three_popular_post,
        'tags': tags,
        'form':form,
        'services': services
    }
    return render(request, 'index.html', context=context)


def about(request):
    services = Service.objects.all()
    popular_post = News.objects.order_by('-like').first()
    context = {
        'popular_post': popular_post,
        'services': services
    }
    return render(request, 'about.html', context=context)


def blog(request):
    
    search_post = request.GET.get('query')
    category_post = request.GET.get('categories')
    if category_post in (None, 'AllCategories') and search_post in (None, ''):
        posts = News.objects.all()
    elif search_post != '':
        if search_post.isdigit():
            posts =  News.objects.filter(created__year=search_post)
        else:
            posts = News.objects.filter(title=search_post)
    else:
        posts = News.objects.filter(choice=category_post)

    bl_paginator = Paginator(posts, 3)
    page_num = request.GET.get('page')
    page = bl_paginator.get_page(page_num)

    context = {
        'posts': posts,
        'page': page,
        'count': bl_paginator.count
    }
    return render(request, 'blog.html', context=context)


def blog_details(request, pk):
    popular_post = News.objects.order_by('-created')[:3]
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = request.user
            form.instance.news = News.objects.get(id=pk)
            form.save()
            form = PostCommentForm()
    else:
        form = PostCommentForm()
    post = News.objects.get(pk=pk)
    context = {
        'post': post,
        'form': form,
        'popular_post': popular_post
    }
    return render(request, 'blog-details.html', context=context)


def service(request):
    if News.objects.count() >= 3:
        three_popular_post = News.objects.order_by('-view_post')[:3]
    else:
        three_popular_post = News.objects.all()
    context = {'three_popular_post': three_popular_post}
    return render(request, 'service.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', context={'form': form})


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


class ServiceCreateView(generics.CreateAPIView):
    serializer_class = ServiceDetailSerializers


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializers


class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializers


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

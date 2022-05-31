from django.urls import path, re_path
from .views import *


urlpatterns = [
    ################## Django rest framework ##############
    path('api/v1/news/create/', NewsCreateView.as_view()),
    path('api/v1/news/list/', NewsListView.as_view()),
    path('api/v1/news/<int:pk>', NewsDetailView.as_view()),

    path('api/v1/video/create/', VideoCreateView.as_view()),
    path('api/v1/video/list/', VideoListView.as_view()),
    path('api/v1/video/<int:pk>', VideoDetailView.as_view()),

    path('api/v1/service/create/', ServiceCreateView.as_view()),
    path('api/v1/service/list/', ServiceListView.as_view()),
    path('api/v1/service/<int:pk>', ServiceDetailView.as_view()),

    ################# Django ################################
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('blog-details/<int:pk>/', blog_details, name='blog_details'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
] 
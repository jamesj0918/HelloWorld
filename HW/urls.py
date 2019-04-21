"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


#각 template 에서 form의 action에서 보내는 url 정의

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'login/',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    path(
        'logout/',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),
    path('guestbook/', guestbook, name='guestbook'),
    path('home/', home, name='home'),
    path('album/', album, name = 'album'),
    path('setting/', setting, name = 'setting'),
    path('join/', join, name= 'join'),
    path('friend/', friend, name = 'friend'),
    path('friend_add/', friend_add, name = 'friend_add'),
    path('recieve_friend/', recieve_friend, name = 'recieve_friend'),
    path('guestcomment/', guestcomment, name = 'guestcomment'),
    path('guestbook_delete/', guestbook_delete, name = 'guestbook_delete'),
    path('comment_delete/', comment_delete, name = 'comment_delete'),
    path('profile_intro/', profile_intro, name = 'profile_intro'),
    path('profile_key/', profile_key, name = 'profile_key'),
    path('profile_QnA/', profile_QnA, name = 'profile_QnA'),
    path('profile_info/', profile_info, name = 'profile_info'),
    path('add_picture/', add_picture, name = 'add_picture'),
    path('basic_info/', basic_info, name = 'basic_info'),
    path('album_delete/', album_delete, name = 'album_delete'),
    path('album_comment/', album_comment, name = 'album_comment'),
    path('photo_comment_delete/', photo_comment_delete, name = 'photo_comment_delete'),
    path('add_profile_img/', add_profile_img, name = 'add_profile_img'),
    path('add_line_intro/', add_line_intro, name = 'add_line_intro'),
    path('add_self_intro/', add_self_intro, name = 'add_self_intro'),
    path('add_gender/', add_gender, name = 'add_gender'),
    path('add_bloodtype/', add_bloodtype, name = 'add_bloodtype'),
    path('add_age/', add_age, name = 'add_age'),
    path('add_bday/', add_bday, name = 'add_bday'),
    path('keyword/', keyword, name = 'keyword'),
    path('add_keyword/', add_keyword, name = 'add_keyword'),
    path('delete_keyword/', delete_keyword, name = 'delete_keyword'),
    path('add_height/', add_height, name = 'add_height'),
    path('add_weight/', add_weight, name = 'add_weight'),
    path('add_phone_num/', add_phone_num, name = 'add_phone_num'),
    path('select_music/', select_music, name = 'select_music'),
    path('add_QnA/', add_QnA, name = 'add_QnA'),
    path('submit_QnA/', submit_QnA, name = 'submit_QnA'),
    path('add_home_guest/', add_home_guest, name = 'add_home_guest'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from posts.views import *
from django.conf import settings
from django.conf.urls.static import static
from users.views import *

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('onlyauthor/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Re-added after ensuring installation
    path('', home_view, name='home'),
    path('post/create/', create_post_view, name='create-post'),
    path('post/delete/<id>/', delete_post_view, name='delete-post'),
    path('post/edit/<id>/', edit_post_view, name='edit-post'),
    path('post/<id>/', post_page_view, name='post'),
    path('post/like/<id>/', like_post, name='like-post'),
    path('search/', search, name='search'),
    path('list_search_users/', list_search_users, name='list-search-users'),
    path('profile/', profile_view, name='profile'),
    path('<username>/', profile_view, name='userprofile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/delete/', profile_delete_view, name='profile-delete'),
    path('profile/onboarding/', profile_edit_view, name='profile-onboarding'),
    path('profile/verify-email/', profile_verify_email, name='profile-verify-email'),
    path('commentsent/<id>/', comment_sent, name='comment-sent'),
    path('comment/delete/<id>/', delete_comment_view, name='comment-delete'),
    path('comment/like/<id>/', like_comment, name='like-comment'),
   
   #other apps
    path('', include("chat.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""microblogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import (LoginAPIView, SignUpAPIView, CreateTweetAPIView, CreateFollowAPIView, FetchTimeLinesAPIView)

urlpatterns = [
    path('login', LoginAPIView.as_view(), name='login'),
    path('signup', SignUpAPIView.as_view(), name='signup'),
    path('tweet/add', CreateTweetAPIView.as_view(), name='addTweet'),
    path('tweet/follow', CreateFollowAPIView.as_view(), name='addFollow'),
    path('tweet/timelines', FetchTimeLinesAPIView.as_view(), name='addTimeline'),
]

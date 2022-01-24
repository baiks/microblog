from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenObtainSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from .permissions import *
from .models import User, Tweets, Follows
from .serializers import UserSerializer, TweetsSerializer, FollowsSerializer
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password


class LoginAPIView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenObtainSerializer


class SignUpAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        serializer.save(password=make_password(self.request.data["password"]),
                        email=BaseUserManager.normalize_email(self.request.data["email"]))


class CreateTweetAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TweetsSerializer
    queryset = Tweets.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateFollowAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowsSerializer
    queryset = Follows.objects.all()

    def perform_create(self, serializer):
        if self.request.user.id == self.request.data["followed"]:
            raise serializers.ValidationError("You cannot follow yourself")
        elif Follows.objects.filter(followed_id=self.request.data["followed"], follower=self.request.user).exists():
            raise serializers.ValidationError("You have already followed this user")
        else:
            serializer.save(follower=self.request.user)


class FetchTimeLinesAPIView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TweetsSerializer

    def get_queryset(self):
        followed = Follows.objects.filter(follower=self.request.user)
        list_followed = []
        for data in list(followed.values()):
            list_followed.append(data["followed_id"])

        print("Followed: ", list_followed)
        return Tweets.objects.filter(id__in=list_followed)

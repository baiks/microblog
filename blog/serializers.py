from rest_framework import serializers
from .models import User, Tweets, Follows
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=100)
    image = serializers.FileField(write_only=False, required=True)

    class Meta:
        model = User
        fields = '__all__'


class TokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token


class TweetsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    tweet = serializers.CharField(max_length=140)

    class Meta:
        model = Tweets
        fields = '__all__'


class FollowsSerializer(serializers.ModelSerializer):
    followed = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    follower = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Follows
        fields = '__all__'

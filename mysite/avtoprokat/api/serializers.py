from rest_framework import serializers
from rest_framework.response import Response
from django.http import JsonResponse

from avtoprokat.models import User, Car

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'language', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        } 

    def save(self):
        user = User(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            language = self.validated_data['language'],
        )
        # check_account = User.objects.filter(email=self.validated_data['email']).first()
        # if check_account is not None:
        #     return JsonResponse ({'email': 'Пользователь с этим email уже существует.'})

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'passwords': 'Пароли должны совпадать.'})
        user.set_password(password)
        user.save()
        return user


class UserCarsSerializerEn(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'name_en', 'created', 'added'
        ]

class UserCarsSerializerRu(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'name_ru', 'created', 'added'
        ]

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email', 'username', 'language'
        ]
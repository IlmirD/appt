from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .serializers import RegistrationSerializer, UserCarsSerializerEn, UserCarsSerializerRu, UsersSerializer
from avtoprokat.models import User, Car

# Зарегистрировать пользователя
@api_view(['POST', ])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data = {'response': 'Регистрация прошла успешно.'}
    else:
        data = serializer.errors
    return Response(data)

# Получить машины пользователя
class GetUserCars(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            user_id = Token.objects.get(key=request.auth.key).user_id
            user = User.objects.get(id=user_id)
            if user.language == 'en':
                cars = Car.objects.filter(renter=user)
                serializer = UserCarsSerializerEn(cars, many=True, context={'request': request})
            if user.language == 'ru':
                cars = Car.objects.filter(renter=user)
                serializer = UserCarsSerializerRu(cars, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)


# Изменить данные пользователя
class EditUserData(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        if request.method == 'POST':
            user_id = Token.objects.get(key=request.auth.key).user_id
            user = User.objects.filter(id=user_id)
            data = request.POST

            user.update(
                email = data['email'],
                username = data['username'],
                language = data['language'],
            )
        
            data = {'response': 'Данные пользователя успешно обновлены.'}
            
        return Response(data)

# Получить всех пользователей
class GetAllUsers(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UsersSerializer(users, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
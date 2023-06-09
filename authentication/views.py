from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, NotFound, AuthenticationFailed
from authentication.serializers import UsersSerializer
from authentication.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    @action(methods=['POST'], detail=False,url_path='register')
    def register(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid( raise_exception=True)
        serializer.save()

        return Response({'message': 'success'})
    
    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
        if 'email' not in request.data:
            raise ValidationError({'error': 'email не может быть пустым'})
        if 'password' not in request.data:
            raise ValidationError({'error': 'пароль не может быть пустым'})

        try:
            user = User.objects.get(email=request.data['email'])
        except User.DoesNotExist:
            raise NotFound({'error': 'пользователь с таким email не найден'})
        
        if not user.check_password(request.data['password']):
            raise AuthenticationFailed({'error': 'неправильный пароль'})
        refresh = RefreshToken.for_user(user)
        response = Response() 
        response.data = {'access': str(refresh.access_token)}
        return response
    
    @action(methods=['GET'], detail=False,permission_classes=[IsAuthenticated], url_path ='me')
    def get_user(self, request):
        user = request.user
        data = self.serializer_class(user).data
        return Response(data)

from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignupForm, ProfileForm
from rest_framework import status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt import authentication
from .models import  User
from .serializers import UserSerializer

@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def me(request):
  

    return JsonResponse({
        'id': request.user.id,
        'name': request.user.name,
        'email': request.user.email,
        'avatar': request.user.get_avatar()

    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data=request.data
    message='success'
    form=SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
    })
    if form.is_valid():
       
        user=form.save()
        user.is_active=False
        user.save()

        url=f'{settings.WEBSITE_URL}/activateemail/?email={user.email}&id={user.id}'
        
        
        send_mail(
            "Please verify your email",
            f"The url for activation your account is:{url}",
             "disonobudho233@gmail.com",
             {user.email},
             fail_silently=False,
        )

        #send verification email later
        message='success'
        return JsonResponse({'message': message})
       
    else:
        message=form.errors.as_json()
        return JsonResponse({'message': message})
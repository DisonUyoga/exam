
from rest_framework import status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt import authentication
from account.models import User
import random
from random import randint
from django.shortcuts import render
from django.http import JsonResponse

from question_bank.models import Multi_Choice_Question, Judgement_Question, Short_Answer_Question, Blank_Question, Multi_Choice_Choice, Blank_Question_Choice,Judgement_Question_Choice,Short_Answer_Choice
from .serializers import Multi_Choice_Question_Serializer, Multi_Choice_Choice_Serializer, Judgement_Question_Serializer, Judgement_Question_Choice_Serializer, Blank_Question_Choice_Serializer, Blank_Question_Serializer, Short_Answer_Question_Serializer, Short_Answer_Question_Choice_Serializer

@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def generate_questions(request):
    m_choices=Multi_Choice_Question_Serializer.all().order_by('?')[:50]
    j_choices=Judgement_Question.objects.all().order_by('?')[:50]
    b_choices=Blank_Question.objects.all().order_by('?')[:50]
    s_choices=Short_Answer_Question.objects.all().order_by('?')[:50]
    
    
    m_serializer=Multi_Choice_Choice_Serializer(m_choices, many=True)
    j_serializer=Judgement_Question_Serializer(j_choices, many=True)
    b_serializer=Blank_Question_Serializer(b_choices, many=True)
    s_serializer=Short_Answer_Question_Serializer(s_choices, many=True)
   
    return JsonResponse({
        'multiple_questions': m_serializer.data,
        'judgement_questions': j_serializer.data,
        'short_answer_questions': s_serializer.data,
        'blank_questions': b_serializer.data,
        
    }, safe=False)

   


@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def m_generate_question_detail(request, pk):
    m_questions=Multi_Choice_Choice.objects.filter(pk=pk)
    serializer=Multi_Choice_Choice_Serializer(m_questions, many=True)

    return JsonResponse(serializer.data, safe=False)
    
@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def j_generate_question_detail(request, pk):
    j_questions=Judgement_Question_Choice.objects.filter(pk-pk)

    serializer=Judgement_Question_Choice_Serializer(j_questions,many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def s_generate_question_detail(request, pk):
    s_questions=Short_Answer_Choice.objects.filter(pk=pk)
    serializer=Short_Answer_Question_Choice_Serializer(s_questions, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@authentication_classes([authentication.JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def b_generate_question_detail(request, pk):
    b_questions=Blank_Question_Choice.objects.filter(pk=pk)
    serializer=Blank_Question_Serializer(b_questions, many=True)

    return JsonResponse(serializer.data, safe=False)
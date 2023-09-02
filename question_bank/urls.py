from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_questions, name='generate_questions'),
    path('m_question/', views.m_generate_question_detail, name='question_generator'),
    path('j_question/', views.j_generate_question_detail, name='question_generator2'),
    path('s_question/', views.s_generate_question_detail, name='question_generator3'),
    path('b_question/', views.b_generate_question_detail, name='question_generator4'),
]

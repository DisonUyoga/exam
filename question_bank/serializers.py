from rest_framework import serializers
from .models import Multi_Choice_Question, Judgement_Question, Short_Answer_Question, Blank_Question, Multi_Choice_Choice, Blank_Question_Choice,Judgement_Question_Choice,Short_Answer_Choice
from account.serializers import UserSerializer


class Multi_Choice_Question_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Multi_Choice_Question
        fields=('id','question_text','user')

class Multi_Choice_Choice_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    question=Multi_Choice_Question_Serializer(read_only=True)
    class Meta:
        model=Multi_Choice_Choice
        fields= ('id', 'choice_text','answer', 'score', 'question', 'user')


class Judgement_Question_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Judgement_Question
        fields=('id','question_text', 'user')

class Judgement_Question_Choice_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    question=Multi_Choice_Question_Serializer(read_only=True)
    class Meta:
        model=Judgement_Question_Choice
        fields= ('id', 'choice_text','answer','score', 'question', 'user')



class Blank_Question_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Blank_Question
        fields=('id','question_text', 'user')

class Blank_Question_Choice_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    question=Multi_Choice_Question_Serializer(read_only=True)
    class Meta:
        model=Blank_Question_Choice
        fields= ('id', 'choice_text','answer','score', 'question','user')


class Short_Answer_Question_Serializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Short_Answer_Question
        fields=('id','question_text','user')

class Short_Answer_Question_Choice_Serializer(serializers.ModelSerializer):
    question=Multi_Choice_Question_Serializer(read_only=True)
    class Meta:
        model=Short_Answer_Choice
        fields= ('id', 'choice_text','answer','score', 'question','user')
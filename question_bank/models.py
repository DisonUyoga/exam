from django.db import models
import uuid
from account.models import User


class Multi_Choice_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Multi Choice Question'
        verbose_name_plural = 'Multi Choice Questions'
    def __str__(self):
        return '{}'.format(self.question_text)

class Multi_Choice_Choice(models.Model):
    question=models.ForeignKey(Multi_Choice_Question, on_delete=models.CASCADE, related_name='m_choices')
    choice_text=models.CharField(max_length=255, null=True, blank=True)
    answer=models.CharField(max_length=255)
    score=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Multi Choices'
        verbose_name_plural = 'Multi Choices'


class Blank_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Blank Question'
        verbose_name_plural = 'Blank Questions'
    def __str__(self):
        return '{}'.format(self.question_text)

class Blank_Question_Choice(models.Model):
    question=models.ForeignKey(Blank_Question, on_delete=models.CASCADE, related_name='b_choices')
    answer=models.CharField(max_length=255)
    score=models.DecimalField(max_digits=3, decimal_places=2)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta: 
        verbose_name = 'Blank Question Choice'
        verbose_name_plural = 'Blank Question Choices'

class Judgement_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Judgement Question'
        verbose_name_plural = 'Judgement Questions'
    def __str__(self):
        return '{}'.format(self.question_text)

class Judgement_Question_Choice(models.Model):
    question=models.ForeignKey(Judgement_Question, on_delete=models.CASCADE, related_name='j_choices')
    choice_text=models.BooleanField(default=False)
    answer=models.BooleanField(default=False)
    score=models.DecimalField(max_digits=3, decimal_places=2)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Judgement Question Choice'
        verbose_name_plural = 'Judgement Question Choices'

class Short_Answer_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Short Answer Question'
        verbose_name_plural = 'Short Answer Questions'
    def __str__(self):
        return '{}'.format(self.question_text)

class Short_Answer_Choice(models.Model):
    question=models.ForeignKey(Short_Answer_Question, on_delete=models.CASCADE, related_name='s_choices')
    choice_text=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)
    score=models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta: 
        verbose_name = 'Short Answer Choice'
        verbose_name_plural = 'Short Answer Choices'

from django.db import models
import uuid


class Multi_Choice_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name = 'Multi Choice Question'
        verbose_name_plural = 'Multi Choice Questions'
    def __str__(self):
        return '%s'.format(self.question_text)

class Choice(models.Model):
    question=models.ForeignKey(Multi_Choice_Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)
    score=models.DecimalField(max_digits=3, decimal_places=2)


class Blank_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name = 'Blank Question'
        verbose_name_plural = 'Blank Questions'
    def __str__(self):
        return '%s'.format(self.question_text)

class Choice(models.Model):
    question=models.ForeignKey(Multi_Choice_Question, on_delete=models.CASCADE)
    answer=models.CharField(max_length=255)
    score=models.DecimalField(max_digits=3, decimal_places=2)

class Judgement_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name = 'Judgement Question'
        verbose_name_plural = 'Judgement Questions'
    def __str__(self):
        return '%s'.format(self.question_text)

class Choice(models.Model):
    question=models.ForeignKey(Multi_Choice_Question, on_delete=models.CASCADE)
    choice_text=models.BooleanField(default=False)
    answer=models.CharField(max_length=255)
    score=models.DecimalField(max_digits=3, decimal_places=2)

class Short_Answer_Question(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question_text=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True)
    class Meta: 
        verbose_name = 'Short Answer Question'
        verbose_name_plural = 'Short Answer Questions'
    def __str__(self):
        return '%s'.format(self.question_text)

class Choice(models.Model):
    question=models.ForeignKey(Multi_Choice_Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=255)
    answer=models.CharField(max_length=255)
    score=models.DecimalField(max_digits=3, decimal_places=2)
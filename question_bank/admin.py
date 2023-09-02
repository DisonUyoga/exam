from django.contrib import admin
from .models import Multi_Choice_Question, Judgement_Question, Blank_Question, Short_Answer_Question, Multi_Choice_Choice, Blank_Question_Choice,Judgement_Question_Choice,Short_Answer_Choice

# Register your models here.




class Multi_Choice_Choice_inline(admin.TabularInline):
    model= Multi_Choice_Choice
    extra=4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Multi Choice Questions', {
            "fields": (
                ['question_text']
            ),
        }),
       
    )
    inlines=[Multi_Choice_Choice_inline]

admin.site.register(Multi_Choice_Question, QuestionAdmin)


class Judgement_Question_inline(admin.TabularInline):
    model= Judgement_Question_Choice
    extra=4


class JudgementAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Judgement Questions', {
            "fields": (
                ['question_text']
            ),
        }),
       
    )
    inlines=[Judgement_Question_inline]

admin.site.register(Judgement_Question, JudgementAdmin)
    
class Blank_Question_inline(admin.TabularInline):
    model= Blank_Question_Choice
    extra=4


class BlankAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Blank Questions', {
            "fields": (
                ['question_text']
            ),
        }),
       
    )
    inlines=[Blank_Question_inline]

admin.site.register(Blank_Question, BlankAdmin)


class Short_Answer_inline(admin.TabularInline):
    model= Short_Answer_Choice
    extra=4


class ShortAnswerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Short Questions', {
            "fields": (
                ['question_text']
            ),
        }),
       
    )
    inlines=[Short_Answer_inline]

admin.site.register(Short_Answer_Question, ShortAnswerAdmin)
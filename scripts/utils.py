import django
import os
import sys
from collections import Counter
from datetime import timedelta
from django.utils import timezone

#run this file to populate data in the tables
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam1.settings")
django.setup()

import pandas as pd
from question_bank.models import Multi_Choice_Question, Judgement_Question, Short_Answer_Question, Blank_Question, Multi_Choice_Choice, Blank_Question_Choice,Judgement_Question_Choice,Short_Answer_Choice
df=pd.read_excel('data.xlsx')

questions=df.iloc[:,1]

def populate(data):
    for question in questions:
        data.append(question)
    return data

data=[]

results=populate(data)
questiontype=df.iloc[:,2]

#print(df.iloc[:,3])
print(df.iloc[:,4])

for _ in range(len(df)):
    for q in questiontype:
        for x in results:
            if (q == 'Multiple choice questions'):
                q=Multi_Choice_Question.objects.create(question_text=x)
                p=Multi_Choice_Question.objects.all()
                print(p[0])
                #for t in Multi_Choice_Question.objects.all():
                 #y=Multi_Choice_Question.objects.get(pk=t.id)
                    #choices=[df.iloc[:,4],df.iloc[:,5],df.iloc[:,6],df.iloc[:,7]]
                    #t=[items[1] for items in choices]
                    #y.m_choices.create(question=y, choice_text=choices, answer=df.iloc[:,3], score=2)
                    #print(t)
                    
                    
                    
                    
              
               
               
               
                    

                    
          
            
            
    

    
        

             



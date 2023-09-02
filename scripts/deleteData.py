import django
import os
import sys
from collections import Counter
from datetime import timedelta
from django.utils import timezone

# Run this file to delete all the data in the tables
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam1.settings")
django.setup()

import pandas as pd
from question_bank.models import Multi_Choice_Question, Judgement_Question, Short_Answer_Question, Blank_Question
df=pd.read_excel('data.xlsx')

questions=df.iloc[:,1]

def populate(data):
    for question in questions:
        data.append(question)
    return data
t=Multi_Choice_Question.objects.all()
data=[]

results=populate(data)
questiontype=df.iloc[:,2]

for _ in range(len(t)):
    for q in questiontype:
        for x in results:
            if (True):
                
               
           
                p=Judgement_Question.objects.all()
                p.delete()
            else:
                r=Blank_Question.objects.all()
                r.delete()

        
            
            

    
        





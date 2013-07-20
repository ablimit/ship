from django.db import models

# Create your models here.

class Questions(models.Model):
    qid = models.AutoField(primary_key=True)
    question_content = models.TextField()
    isLinkedin = models.BooleanField()
    hasAnswer = models.BooleanField() 
    category = models.CharField(max_length=100)
    
    def __unicode__(self):
        return str(self.question_content) 
  
class StoredAnswers(models.Model):
    aid = models.AutoField(primary_key=True)
    qid = models.ForeignKey('Questions')
    AnswerContent = models.TextField()    
    
    def __unicode__(self):
        return str(self.qid)
   
class UserAnswers(models.Model):    
    uid = models.AutoField(primary_key=True)
    qid = models.ForeignKey('Questions')
    sid = models.CharField(max_length=100)
    #sid = ForeignKey('Session')
    AnswerContent = models.TextField()
    
    def __unicode__(self):
        return str(self.qid)

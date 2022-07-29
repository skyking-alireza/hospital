from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class modelusers(AbstractUser):
    profileimage = models.ImageField(upload_to='profiles',null=True,blank=True)
    nationalcode = models.CharField(max_length=11)
    Medicalsystemnumber = models.CharField(max_length=5,null=True)
    specialtieschoise = (
                         (1,'قلب و عروق'),
                         (2,'متخصص زنان زایمان و نازایی'),
                         (3,'چشم'),
                         (4,'پوست و مو'),
                         (5,'کلیه و مجاری ادراری'),
                         (6,'ارتوپدی'),
                         )
    specialties = MultiSelectField(specialtieschoise,null=True)
    address = models.TextField(max_length=450,null=True)
    phone = models.CharField(max_length=11,null=True)
    Workexperience = models.CharField(max_length=2,null=True)
    address = models.TextField(max_length=450)
    phone = models.CharField(max_length=11)
    birthdate = models.CharField(max_length=4)
class modeltimedoctor(models.Model):
    docter = models.ForeignKey(modelusers,on_delete=models.CASCADE , related_name='docter')
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    longtime = models.TextField()
    patient = models.ForeignKey(modelusers,on_delete=models.CASCADE,null=True,blank=True,related_name='patient')
class modelmessages(models.Model):
    sender = models.ForeignKey(modelusers,on_delete=models.CASCADE , related_name='sender')
    time = models.DateTimeField(auto_now=True)
    text = models.TextField()
    reciver = models.ForeignKey(modelusers,on_delete=models.CASCADE,related_name='reciver')
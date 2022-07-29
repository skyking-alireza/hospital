from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from accounts.models import modelusers


class modelblogcategory(models.Model):
    name = models.SlugField(max_length=150)
    image = models.ImageField(upload_to='blogcategory')
    description = models.TextField()
    keywords = models.CharField(max_length=250)
    tags = models.CharField(max_length=150)
class modelblog(models.Model):
    category = models.ForeignKey(modelblogcategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog')
    name = models.CharField(max_length=150)
    text = HTMLField()
    description = models.TextField()
    keywords = models.CharField(max_length=250)
    tags = models.CharField(max_length=150)
class modelcommentblog(models.Model):
    blog = models.ForeignKey(modelblog,on_delete=models.CASCADE)
    user = models.ForeignKey(modelusers,on_delete=models.CASCADE)
    star = models.IntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField()


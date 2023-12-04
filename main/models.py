from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Article(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    createdAt = models.DateTimeField(auto_now_add= True)
    authors = models.ManyToManyField('Author')
    img = models.ImageField(upload_to='images/', max_length=250, null=True,blank=True, default=None)

    def __str__(self):
        return self.title
    
class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	


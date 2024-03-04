from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    images = models.ImageField(upload_to="images")

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class About_executive_team(models.Model):
    images = models.ImageField(upload_to="images")
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class About_functional_team(models.Model):
    images = models.ImageField(upload_to="images")
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class About_technical_team(models.Model):
    images = models.ImageField(upload_to="images")
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class About_technical2_team(models.Model):
    images = models.ImageField(upload_to="images")
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class About_executive2_team(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    description = models.TextField()

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class News(models.Model):
    images = models.ImageField(upload_to="images")
    name = models.CharField(max_length=150)
    
    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = " "

        return url
    
class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()

class Message(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()

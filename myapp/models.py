from django.db import models

# Create your models here.

class NewUser(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)

    def __str__(self):
        return self.fname

class notes(models.Model):
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    myfile=models.FileField(upload_to='upload')
    comment=models.CharField(max_length=500)

    def __str__(self):
        return self.title

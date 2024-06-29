from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,default="")
    password = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}/{self.email}"



'''
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(User,related_name='creados', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''
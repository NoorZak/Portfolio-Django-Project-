from django.db import models

# Create your models here.
class User(models.Model):

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imgUrl = models.CharField(max_length=255)


    #objects = UserManager()
    def __str__(self):
        return f"<User object: {self.first_name+self.last_name} ({self.id})>"

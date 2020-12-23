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

class Skill(models.Model):

    title = models.CharField(max_length=45)
    desc = models.TextField(default="default!")
    user = models.ForeignKey(User, related_name="skill_foruser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Skill object: {self.title+self.desc} ({self.id})>"


class Experience(models.Model):

    title = models.CharField(max_length=45)
    desc = models.TextField(default="default!")
    user = models.ForeignKey(User, related_name="experience_foruser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Skill object: {self.title+self.desc} ({self.id})>"


class Contact(models.Model):

    icon = models.CharField(max_length=45)
    value = models.TextField(default="default!")
    user = models.ForeignKey(User, related_name="contact_foruser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"<Contact object: {self.icon+self.value} ({self.id})>"

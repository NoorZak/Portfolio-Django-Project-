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

def insertUser(user):
    User.objects.create(first_name=user['first_name'],last_name=user['last_name'] , email=user['email'],password=user['password'])
    return "success"


def editUser(user,id):

    updated_user=User.objects.get(id=id)
    updated_user.first_name = user['first_name']
    updated_user.last_name = user['last_name']
    updated_user.email = user['email']
    updated_user.password = user['password']
    updated_user.save()
    return "success"


def getAllUsers():
    users=User.objects.all()
    return users




class Skill(models.Model):

    title = models.CharField(max_length=45)
    desc = models.TextField(default="default!")
    user = models.ForeignKey(User, related_name="skill_foruser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Skill object: {self.title+self.desc} ({self.id})>"



def insertSkill(skill,user_id):
    user = User.objects.get(id=user_id)
    Skill.objects.create(title = skill["title"], desc=skill["desc"], user=user)
    return "success"


def editSkill(skill,id):

    updated_skill=Skill.objects.get(id=id)
    updated_skill.title = skill['title']

    updated_skill.desc = skill['desc']
    updated_skill.save()
    return "success"


def getAllSkills(id):
    skills = Skill.objects.filter(id=id)
    return skills

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

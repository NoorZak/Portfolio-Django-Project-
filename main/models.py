from django.db import models
import re
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData["first_name"]) < 2:

            errors["first_name"] = "First name should be at least 2 characters"

        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"

        if len(postData['password']) < 8:
            errors["password"] = "Passwords should be more than 8 characters"

        if (postData["password"] !=postData['cpassword']) :
            errors["password"] = "Passwords should match"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):  # test whether a field matches the pattern
            errors['email'] = "Invalid email address!"
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['logged_email'])

        if not user:
            errors['email'] = "Please enter a valid email address."

        return  errors

class User(models.Model):

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    imgUrl = models.CharField(max_length=255)
    objects = UserManager()


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

def getUserById(id):
    users= User.objects.filter(id=id)
    return users

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


def getAllSkillsForUser(id):
    user = User.objects.get(id=id)
    skills = Skill.objects.filter(user=user)
    return skills


class Experience(models.Model):

    title = models.CharField(max_length=45)
    desc = models.TextField(default="default!")
    user = models.ForeignKey(User, related_name="experience_foruser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Experience object: {self.title+self.desc} ({self.id})>"

def insertExperience(experience,user_id):
    user = User.objects.get(id=user_id)
    Experience.objects.create(title = experience["title"], desc=experience["desc"], user=user)
    return "success"


def editExperience(experience,id):

    updated_experience=Experience.objects.get(id=id)
    updated_experience.title = experience['title']

    updated_experience.desc = experience['desc']
    updated_experience.save()
    return "success"


def getAllExperienceForUser(id):
    user = User.objects.get(id=id)
    experiences= Experience.objects.filter(user=user)
    return experiences


class Contact(models.Model):

    icon = models.CharField(max_length=45)
    value = models.TextField(default="default!")
    user = models.ForeignKey(User, related_name="contact_foruser", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"<Contact object: {self.icon+self.value} ({self.id})>"


def insertContact(contact,user_id):
    user = User.objects.get(id=user_id)
    Contact.objects.create(icon = contact["icon"], value=contact["val"], user=user)
    return "success"


def editContact(contact,id):
    updated_contact=Contact.objects.get(id=id)
    updated_contact.icon = contact['icon']

    updated_contact.value = contact['val']
    updated_contact.save()
    return "success"


def getAllContactsForUser(id):
    user = User.objects.get(id=id)

    contacts = Contact.objects.filter(user=user)
    return contacts

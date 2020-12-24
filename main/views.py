from django.shortcuts import render
from django.urls import path,include

# Create your views here.
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import *
import re	# the regex module
import bcrypt

# Create your views here.
from django.urls import reverse

from django.contrib import messages


# Create your views here.

def index(request):
    return  render(request,"index.html")

def root(request):
    context={
        "view": "empty"


    }
    return render(request,"temp.html",context)


def skillsView(request):
    if request.session["logged_id"]==8:
        skills= Skill.objects.all()
    else :
        skills = getAllSkillsForUser(request.session["logged_id"])

    if request.POST:
        skills= getAllSkillsForUser(request.POST["search"])

    context={

       "skills": skills,
       "view":"skills/view"
    }
    return render(request,"temp.html",context)

def skillsEdit(request,id):
    context={
        "view":"skills/edit",
        "id":id
    }
    return render(request,"temp.html",context)


def skillsInsert(request):
    context={
        "view":"skills/insert"

    }

    return render(request,"temp.html",context)


def skillsDoInsert(request):
    if request.session["logged_id"] == 8:
        skill = insertSkill(request.POST, request.POST["search"])

    else:
        skill = insertSkill(request.POST, request.session["logged_id"])

    return redirect(skillsView)



def skillsDoEdit(request,id):
    skill=editSkill(request.POST,id)
    return redirect(skillsView)


def skillsDelete(request,id):
    skill_to_delete = Skill.objects.get(id=id)
    skill_to_delete.delete()
    return redirect(skillsView)

def experienceView(request):

    if request.session["logged_id"]==8:
        experiences = Experience.objects.all()

    else:
        experiences = getAllExperienceForUser(request.session["logged_id"])

    if request.POST:
        experiences= getAllExperienceForUser(request.POST["search"])


    context={

       "experiences": experiences,
       "view":"experience/view"
    }
    return render(request,"temp.html",context)
 
def experienceEdit(request,id):
    context={
        "view":"experience/edit",
        "id":id
    }
    return render(request,"temp.html",context)


def experienceInsert(request):
    context={
        "view":"experience/insert"

    }

    return render(request,"temp.html",context)


def experienceDoInsert(request):

    if request.session["logged_id"] == 8:
        experience = insertExperience(request.POST, request.POST["search"])

    else:
        experience = insertExperience(request.POST, request.session["logged_id"])

    return redirect(experienceView)



def experienceDoEdit(request,id):
    experience=editExperience(request.POST,id)
    return redirect(experienceView)


def experienceDelete(request,id):
    experience_to_delete = Experience.objects.get(id=id)
    experience_to_delete.delete()

    return redirect(experienceView)


def contactsView(request):
    if request.session["logged_id"]==8:
        contacts = Contact.objects.all()
    else :
        contacts = getAllContactsForUser(request.session["logged_id"])

    if request.POST:
        contacts = getAllContactsForUser(request.POST["search"])

    context = {

        "contacts": contacts,
        "view": "contacts/view"
    }
    return render(request, "temp.html", context)


def contactsEdit(request,id):
    context={
        "view":"contacts/edit",
        "id":id
    }
    return render(request,"temp.html",context)


def contactsInsert(request):
    context={
        "view":"contacts/insert"

    }

    return render(request,"temp.html",context)


def contactsDoInsert(request):
    if request.session["logged_id"] == 8:
        contact = insertContact(request.POST, request.POST["search"])

    else:
        contact = insertContact(request.POST, request.session["logged_id"])


    return redirect(contactsView)




def contactsDelete(request,id):
    contact_to_delete = Contact.objects.get(id=id)
    contact_to_delete.delete()

    return redirect(contactsView)


def contactsDoEdit(request,id):
    contact=editContact(request.POST,id)
    return redirect(contactsView)


def usersView(request):

    if request.session["logged_id"]==8:
        users = getAllUsers()
    else :
        users = getUserById(request.session["logged_id"])

    if request.POST:
        users = User.objects.filter(id=request.POST["search"])

    context={
        "view":"users/view",
        "users" : users

            }
    return render(request,"temp.html",context)


def usersEdit(request,id):
    context={
        "view":"users/edit",
        "id":id
            }

    return render(request,"temp.html",context)

def usersDelete(request,id):
    user =User.objects.get(id=id)
    user.delete()

    return redirect(usersView)


def usersInsert(request):
    context={
        "view":"users/insert"
    }
    return render(request,"temp.html",context)

def usersDoInsert(request):
    user=insertUser(request.POST)
    return redirect(usersView)


def usersDoEdit(request,id):
    user=editUser(request.POST,id)
    return redirect(usersView)



def resumeForUser(request,id):
    user=User.objects.get(id=id)
    skills=Skill.objects.filter(user=user)
    experiences=Experience.objects.filter(user=user)
    contacts=Contact.objects.filter(user=user)

    context={
        "skills":skills,
        "experiecns":experiences,
         "contacts":contacts,

    }
    return render(request,"resumeForUser.html",context)



def register(request):
    if request.POST:
        #print(request.POST)
        # errors = User.objects.register_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #
        #     return render(request,"index.html")
        # else:

            user =User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST["email"],password=request.POST["password"])
            request.session["logged_id"] = user.id
            request.session["Reg"] = "Register"

            return redirect(root)


def login(request):
    if request.POST:
        #errors = User.objects.login_validator(request.POST)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #
        #     return render(request, "index.html")

        try :
                user=User.objects.get(email =request.POST["logged_email"])

                if (request.POST['logged_pwd']== user.password):
                    request.session["logged_id"] = user.id
                    if "Reg" in request.session:
                        del request.session["Reg"]
                    return redirect(root)

                else:
                    return redirect(index)

        except:
                return redirect(index)



def logout(request):
    if "logged_id" in request.session:
        del request.session["logged_id"]
    return redirect(index)


def validator(request):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(request.POST["first_name"]) < 2:

            errors["fname_error"] = "First name should be at least 2 characters"

        if len(request.POST["last_name"]) < 2:
            errors["lname_error"] = "Last name should be at least 2 characters"

        if len(request.POST['password']) < 8:
            errors["pwd_error"] = "Passwords should be more than 8 characters"

        if (request.POST["cpassword"] !=request.POST['password']) :
            errors["pwd_error"] = "Passwords should match"
            errors["cpwd_error"] = "Passwords should match"

        #EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        #if not EMAIL_REGEX.match(postData['email']):  # test whether a field matches the pattern
         #   errors['email'] = "Invalid email address!"
        context={
            "errors":errors,
            "view":"users/insert"
        }

        return render(request,"temp.html",context)



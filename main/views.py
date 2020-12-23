from django.shortcuts import render
from django.urls import path,include

# Create your views here.
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import *

# Create your views here.

def resumeForUser(request):
    return  render(request,"resumeForUser.html")

def index(request):
    return  render(request,"index.html")
def root(request):
    context={
        "view": "empty"


    }
    return render(request,"temp.html",context)


def skillsView(request):
    skills= Skill.objects.all()

    if request.POST:
        skills= Skill.objects.filter(id=request.POST["search"])

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
    skill=insertSkill(request.POST,request.POST["search"])

    return redirect(skillsView)



def skillsDoEdit(request,id):
    skill=editSkill(request.POST,id)
    return redirect(skillsView)


def experienceView(request):
    context={
        "view":"experience/view"
    }

    return render(request,"temp.html",context)


def experienceEdit(request):
    context={
        "view":"experience/edit"
    }
    return render(request,"temp.html",context)


def experienceInsert(request):
    context={
        "view":"experience/insert"
            }
    return render(request,"temp.html",context)



def contactsView(request):
    context={
        "view":"contacts/view"
            }
    return render(request,"temp.html",context)


def contactsEdit(request):
    context={
        "view":"contacts/edit"
            }
    return render(request,"temp.html",context)


def contactsInsert(request):
    context={
        "view":"contacts/insert"
    }
    return render(request,"temp.html",context)



def usersView(request):
    users = getAllUsers()

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



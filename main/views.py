from django.shortcuts import render
from django.urls import path,include

# Create your views here.
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from .models import *
import re	# the regex module
import bcrypt
from django.core.files.storage import FileSystemStorage
import json
from django.http import JsonResponse
# Create your views here.
from django.urls import reverse

from django.contrib import messages


# Create your views here.

def index(request):
    return  render(request,"index.html")

def root(request):

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view": "empty"


    }
    context['logged_user'] = User.objects.get(id=request.session["logged_id"])
    return render(request,"temp.html",context)


def skillsView(request):

    if "logged_id" not in request.session:
        return redirect(index)

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

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"skills/edit",
        "id":id
    }
    return render(request,"temp.html",context)


def skillsInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"skills/insert"

    }

    return render(request,"temp.html",context)


def skillsDoInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)

    if request.session["logged_id"] == 8:
        skill = insertSkill(request.POST, request.POST["search"])

    else:
        skill = insertSkill(request.POST, request.session["logged_id"])

    return redirect(skillsView)



def skillsDoEdit(request,id):

    if "logged_id" not in request.session:
        return redirect(index)

    skill=editSkill(request.POST,id)
    return redirect(skillsView)


def skillsDelete(request,id):

    if "logged_id" not in request.session:
        return redirect(index)

    skill_to_delete = Skill.objects.get(id=id)
    skill_to_delete.delete()
    return redirect(skillsView)

def experienceView(request):

    if "logged_id" not in request.session:
        return redirect(index)


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

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"experience/edit",
        "id":id
    }
    return render(request,"temp.html",context)


def experienceInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"experience/insert"

    }

    return render(request,"temp.html",context)


def experienceDoInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)


    if request.session["logged_id"] == 8:
        experience = insertExperience(request.POST, request.POST["search"])

    else:
        experience = insertExperience(request.POST, request.session["logged_id"])

    return redirect(experienceView)



def experienceDoEdit(request,id):

    if "logged_id" not in request.session:
        return redirect(index)

    experience=editExperience(request.POST,id)
    return redirect(experienceView)


def experienceDelete(request,id):
    experience_to_delete = Experience.objects.get(id=id)
    experience_to_delete.delete()

    return redirect(experienceView)


def contactsView(request):

    if "logged_id" not in request.session:
        return redirect(index)

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

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"contacts/edit",
        "id":id
    }
    return render(request,"temp.html",context)


def contactsInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)

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

    if "logged_id" not in request.session:
        return redirect(index)

    contact_to_delete = Contact.objects.get(id=id)
    contact_to_delete.delete()

    return redirect(contactsView)


def contactsDoEdit(request,id):
    contact=editContact(request.POST,id)
    return redirect(contactsView)


def usersView(request):

    if "logged_id" not in request.session:
        return redirect(index)


    if request.session["logged_id"]==8:
        users = getAllUsers()
    else :
        users = getUserById(request.session["logged_id"])


    context={
        "view":"users/view",
        "users" : users

            }
    return render(request,"temp.html",context)


def usersEdit(request,id):

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"users/edit",
        "id":id
            }

    return render(request,"temp.html",context)

def usersDelete(request,id):

    if "logged_id" not in request.session:
        return redirect(index)

    user =User.objects.get(id=id)
    user.delete()

    return redirect(usersView)


def usersInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)

    context={
        "view":"users/insert"
    }
    return render(request,"temp.html",context)

def usersDoInsert(request):

    if "logged_id" not in request.session:
        return redirect(index)

    user=insertUser(request.POST)
    return redirect(usersView)


def usersDoEdit(request,id):

    if "logged_id" not in request.session:
        return redirect(index)

    user=editUser(request.POST,id)
    return redirect(usersView)



def resumeForUser(request,id=None):
    if request.method =="POST":
        user = User.objects.get(id=request.POST["search"])
    else:
        user=User.objects.get(id=id)
    skills=Skill.objects.filter(user=user)
    experiences=Experience.objects.filter(user=user)
    contacts=Contact.objects.filter(user=user)

    context={
        "skills":skills,
        "experiences":experiences,
         "contacts":contacts,
        "user":user
    }
    return render(request,"resumeForUser.html",context)



def register(request):
    if request.POST:
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return render(request,"index.html")
        else:

            user =User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST["email"],password=request.POST["password"])
            request.session["logged_id"] = user.id
            request.session["logged_name"] = user.first_name+" "+user.last_name

            request.session["Reg"] = "Register"

            return redirect(root)


def login(request):
    if request.POST:
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return render(request, "index.html")

        try :
                user=User.objects.get(email =request.POST["logged_email"])

                if (request.POST['logged_pwd']== user.password):
                    request.session["logged_id"] = user.id
                    request.session["logged_name"] = user.first_name + " " + user.last_name
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




def upload(request):
    if "logged_id" not in request.session:
        return redirect(index)

    context = {
        "view": "upload"
    }
    return  render(request ,"temp.html",context)


def doUpload(request):
    if "logged_id" not in request.session:
        return redirect(index)

    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']

        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        context['view']="empty"
        context['logged_user'] = User.objects.get(id=request.session["logged_id"])

        #    if request.session["logged_id"]==8:
 #       users = getAllUsers()
  #  else :
        if "id" in request.POST:
            user = User.objects.get(id=request.POST["id"])
        else:
            user = User.objects.get(id=request.session["logged_id"])
        user.imgUrl=fs.url(name)
        user.save()
    return render(request, 'temp.html', context)


def searchUsers(request):
    if request.method=='POST':
         search_str= json.loads(request.body)["searchText"]

         if search_str.isnumeric():
             users = User.objects.filter(id=search_str)
         else:
             users=User.objects.filter(first_name__startswith = search_str) |User.objects.filter(last_name__startswith=search_str) | User.objects.filter(email__startswith=search_str)
          #
         data = users.values()


    return JsonResponse(list(data), safe=False)

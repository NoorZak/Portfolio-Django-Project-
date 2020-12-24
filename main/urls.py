from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('i', views.index),
    path('r', views.resumeForUser),
    #path('experience/view', views.experienceView),
    #path('experience/edit', views.experienceEdit),
    #path('experience/insert', views.experienceInsert),

    path('users/view', views.usersView),
    path('users/edit/<int:id>', views.usersEdit),

    path('users/delete/<int:id>', views.usersDelete),
    path('users/insert', views.usersInsert),
    path('users/validator', views.validator),
    path('users/usersDoInsert', views.usersDoInsert),
    path('users/edit/usersDoEdit/<int:id>', views.usersDoEdit),
    
    path('skills/view', views.skillsView),
    path('skills/edit/<int:id>', views.skillsEdit),
    path('skills/delete/<int:id>', views.skillsDelete),

    path('skills/insert', views.skillsInsert),
    path('skills/skillsDoInsert', views.skillsDoInsert),
    path('skills/edit/skillsDoEdit/<int:id>', views.skillsDoEdit),
    
    path('experience/view', views.experienceView),
    path('experience/edit/<int:id>', views.experienceEdit),
    path('experience/delete/<int:id>', views.experienceDelete),

    path('experience/insert', views.experienceInsert),
    path('experience/experienceDoInsert', views.experienceDoInsert),
    path('experience/edit/experienceDoEdit/<int:id>', views.experienceDoEdit),

    path('contacts/view', views.contactsView),
    path('contacts/edit/<int:id>', views.contactsEdit),

    path('contacts/delete/<int:id>', views.contactsDelete),
    path('contacts/insert', views.contactsInsert),
    path('contacts/contactsDoInsert', views.contactsDoInsert),
    path('contacts/edit/contactsDoEdit/<int:id>', views.contactsDoEdit),
    path('resumeForUser/<int:id>',views.resumeForUser),
    #path('skills/edit/usersDoEdit/<int:id>', views.usersDoEdit)
    path('register', views.register),
    path('login', views.login),
path('logout', views.logout),

]
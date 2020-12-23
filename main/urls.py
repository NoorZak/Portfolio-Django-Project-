from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('i', views.index),
    path('r', views.resumeForUser),
    path('experience/view', views.experienceView),
    path('experience/edit', views.experienceEdit),
    path('experience/insert', views.experienceInsert),
    path('contacts/view', views.contactsView),
    path('contacts/edit', views.contactsEdit),
    path('contacts/insert', views.contactsInsert),
    path('users/view', views.usersView),
    path('users/edit/<int:id>', views.usersEdit),
    path('users/insert', views.usersInsert),

    path('users/validator', views.validator)
    ,

    path('users/usersDoInsert', views.usersDoInsert),

    path('users/edit/usersDoEdit/<int:id>', views.usersDoEdit),
    path('skills/view', views.skillsView),
    path('skills/edit/<int:id>', views.skillsEdit),
    path('skills/insert', views.skillsInsert),
    path('skills/skillsDoInsert', views.skillsDoInsert),
    path('skills/edit/skillsDoEdit/<int:id>', views.skillsDoEdit),

    #path('skills/edit/usersDoEdit/<int:id>', views.usersDoEdit)

]
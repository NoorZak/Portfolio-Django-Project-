from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('i', views.index),
    path('r', views.resumeForUser),
    path('skills/view',views.skillsView) ,
    path('skills/edit',views.skillsEdit) ,
    path('skills/insert',views.skillsEdit),
    path('experience/view', views.experienceView),
    path('experience/edit', views.experienceEdit),
    path('experience/insert', views.experienceInsert),
    path('contacts/view', views.contactsView),
    path('contacts/edit', views.contactsEdit),
    path('contacts/insert', views.contactsInsert),
    path('users/view', views.usersView),
    path('users/edit', views.usersEdit),
    path('users/insert', views.usersInsert),

    path('users/validator', views.validator),

]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('r', views.root),
    path('', views.index),
    #path('experience/view', views.experienceView),
    #path('experience/edit', views.experienceEdit),
    #path('experience/insert', views.experienceInsert),

    path('users/view', views.usersView),
    path('users/edit/<int:id>', views.usersEdit),
    path('users/delete/<int:id>', views.usersDelete),
    path('users/insert', views.usersInsert),
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
    path('resumeForUser', views.resumeForUser),

    #path('skills/edit/usersDoEdit/<int:id>', views.usersDoEdit)
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),

    path('upload',views.upload),
    path('doUpload', views.doUpload),
    path('searchUsers', csrf_exempt(views.searchUsers)),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
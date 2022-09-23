from user import views
from django.urls import path


urlpatterns =[ 

    path('userlist/', views.userlist, name="userlist"),
    path('userlist/adduser/', views.adduser, name="adduser"),#1
    path('userlist/adduser/addusersend/', views.addusersend, name="addusersend"),#2
    path('identify/', views.identify, name="identify"),
    path('checkuserlogin/', views.checkuserlogin, name="checkuserlogin"),
    
]
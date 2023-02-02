
from django.urls import path
from .views import *
urlpatterns = [
    path("",home,name="home"),
    # path("login/",login_view),
    path("login_firebase/",firebase_login ),
     path("home/",homepage),

   

   
]

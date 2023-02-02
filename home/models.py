import json
from django.db import models
from froala_editor.fields import FroalaField
from django.contrib.auth.models import User
from .helpers import *
from .helpers import generate_slug


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    upload_to = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        print(self.slug)
        print(self.image)
        from firebase import Firebase
        config = {
             "apiKey": "AIzaSyA2rPzyKAwGPhtkSiCOewaIP79axf4fC38",
            "authDomain": "enstro-68247.firebaseapp.com",
            "databaseURL": "https://enstro-68247-default-rtdb.firebaseio.com",
            "projectId": "enstro-68247",
            "storageBucket": "enstro-68247.appspot.com",
            "messagingSenderId": "904641560773",
            "appId": "1:904641560773:web:f0d6dceb3bba315e5630ac",
            "measurementId": "G-KYQ2X9XP8P"
        }
        firebase = Firebase(config)
        import requests
        response = requests.get("http://api.open-notify.org/astros.json")
        print(response)
        import facebook
        graph = facebook.GraphAPI(access_token="EAAJMabd54c4BAKx9IlkZAOlyK0gMNrKdmYcyjIHW0rImkdPNSTQtmDae10hmFyuHcsZCJSrH25t2km8svQKNLVpnW7cnyds40ncWGo49erupZC5OrAnYPfncAGEL7efQC33GGyXDJpiZChayUZBnQOFDhBtCpVa3gZBw4MLwjBVqVBpZCXKoM3J8ZApNMSd3eZAkjdNmBekbbvGzEvCvjGbTQ0cbvQ9MQVjCzjsg5oP5ceZBCZBQejbpB29ZCw1ZB7LPdj5AZD", version="2.12")
        groups = graph.get_object('me?fields=groups{id}')

        maindata= groups["groups"]["data"]
        for x in maindata:
            if(x['id']=="392934177836346"):
                print(x)
                # graph.put_object("392934177836346", "feed", message="flutter bht hard ha bhai")

        





        super(BlogModel, self).save(*args, **kwargs)

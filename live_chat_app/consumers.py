import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from .forms import UserForm,LoginForm,post_comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Comment
from .long_word import kelime_sil
user_name="harun"
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user_id = text_data_json["user_id"]
        text=  kelime_sil(message)
        if text =='':
            pass
        else:
            user = User.objects.get(id=user_id)
            global user_name
            user_name=user.username
            new_comment = Comment(user=user, text=text)  
            new_comment.save()


        async_to_sync(self.channel_layer.group_send)(
            
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                

            }
        )

    def chat_message(self, event):
        message = event['message']
    
        
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'user_name':user_name
        }))

    
from . import views
from django.urls import path



urlpatterns=[

path("main", views.ana_sayfa, name="ana_sayfa"),
path("log-in page",views.log_in,name="log_in"),
path("log-out page",views.log_out,name="log_out"),
path("sign-up page",views.sign_up,name="sign_up"),
path("chat page",views.chat,name="chat"),

]

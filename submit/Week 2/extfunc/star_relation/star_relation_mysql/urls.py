from django.urls import path
from .views import redirect,login,index,modify,query
urlpatterns = [
    path('',redirect),
    path('login',login),
    path('new',index),
    path('modify',modify),
    path('query',query),
]
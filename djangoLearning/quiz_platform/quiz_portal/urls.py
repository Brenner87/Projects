from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^(?P<id>\d+)/', views.viewSelectedQuiz, name='viewSelectedQuiz'),
url(r'^create_item', views.createOwnQuiz, name='createOwnQuiz'),

]

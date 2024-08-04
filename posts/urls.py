from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<str:pk>', views.post, name='post'),
    path('editpost/<str:pk>', views.editPost, name='editPost'),
    path('post/<str:pk>/delete', views.delete, name='delete'),
    path('newPost', views.newPost, name= 'newPost'),
]
handler404 = 'posts.views.error'
handler500 = 'posts.views.error'
